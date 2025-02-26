from django.shortcuts import render
from django.http import HttpResponse
from .utils import ask_indexer, get_openai_response
from data_ingestion.utils import get_pdf
from geopy.distance import geodesic

def search_view(request):
    query = ''
    results = []
    if request.method == 'POST':
        query = request.POST.get('q', '')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        user_location = (float(latitude), float(longitude)) if latitude and longitude else None
        results = ask_indexer(query) if query else []
  

        if user_location:
            for result in results:
                print(result.keys())
                company_location = (result['latitude'], result['longitude'])
                result['distance'] = geodesic(user_location, company_location).km
            results = sorted(results, key=lambda x: x['distance'])

    return render(request, 'chat.html', {'results': results, 'query': query})

def get_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        file_content = get_pdf(file_name)
        response = HttpResponse(file_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    return HttpResponse(status=400)

def menu_description(request):
    if request.method == 'POST':
        raw_content = request.POST.get('raw_content', '')
        description = get_openai_response(raw_content)
        return render(request, 'menu_description.html', {'description': description})
    return HttpResponse(status=400)