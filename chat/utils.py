from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from django.conf import settings
from openai import AzureOpenAI

def get_search_client():
    endpoint = settings.SEARCH_ENDPOINT
    index_name = settings.SEARCH_INDEX_NAME
    api_key = settings.SEARCH_API_KEY
    credential = AzureKeyCredential(api_key)
    return SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)

def ask_indexer(query):
    """
    Queries the search client with the given query and returns the search results.

    Args:
        query (str): The query string to search for.

    Returns:
        list: A list of search results.
    """
    client = get_search_client()
    results = client.search(query)
    return [result for result in results]

def get_openai_client():
    endpoint = settings.OPENAI_ENDPOINT
    api_key = settings.OPENAI_API_KEY
    api_version = settings.OPENAI_API_VERSION
    return AzureOpenAI(api_key=api_key, azure_endpoint=endpoint, api_version=api_version)

def get_openai_response(user_prompt):
    client = get_openai_client()
    response = client.chat.completions.create(
        model=settings.OPENAI_DEPLOYMENT,
        messages=[
            {"role": "system", "content": 
                """
                You are a helpful assistant that recieves a raw text obtained from a restaurant's menu file.
                You clean the raw text to display the daily menu (if there's no daily menu, you will display the whole menu), 
                and if there's vegan or vegetarian options.
                You must return only the daily menu or the whole menu, not both.
                The daily menu must be a list of dishes, separated between first and second courses, then the dessert.
                In case the daily menu doesn't specify the courses, you must return the dishes in the order they appear.
                If there's no dishes for a course, you will say that they must ask the restaurant for the daily menu.
                Also if there's vegan or vegetarian options, you must specify it and create a menu based on the vegan or vegetarian dishes.
                Separate the pharagraphs with a new line. Answer in the same language of the prompt.
                """},
             {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content


