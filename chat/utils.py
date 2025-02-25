from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from django.conf import settings

def get_search_client():
    endpoint = settings.SEARCH_ENDPOINT
    index_name = settings.SEARCH_INDEX_NAME
    api_key = settings.SEARCH_API_KEY
    credential = AzureKeyCredential(api_key)
    return SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)

def ask_indexer(query):
    client = get_search_client()
    results = client.search(query)
    return [result for result in results]

