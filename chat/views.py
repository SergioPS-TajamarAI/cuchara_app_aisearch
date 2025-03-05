from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .utils import ask_indexer, get_openai_response
from data_ingestion.utils import get_pdf
from geopy.distance import geodesic

def search_view(request):
    query = ''
    results = []
    context = {'results': results, 'query': query}
    
    if request.method == 'POST':
        query = request.POST.get('q', '')
        user_latitude = request.POST.get('latitude')
        user_longitude = request.POST.get('longitude')
        
        # Check if location was provided
        if not user_latitude or not user_longitude:
            messages.error(request, "Por favor, selecciona tu ubicación en el mapa antes de buscar.")
            context['query'] = query
            return render(request, 'chat.html', context)
        
        # Only search if query is provided
        if query:
            results = ask_indexer(query)
            user_location = (float(user_latitude), float(user_longitude))
            
            # Calculate distance for each result
            for result in results:
                company_location = (result['latitude'], result['longitude'])
                result['distance'] = geodesic(user_location, company_location).km
            
            # Sort results by distance
            results = sorted(results, key=lambda x: x['distance'])
            
        context = {
            'results': results, 
            'query': query,
            'user_latitude': user_latitude,
            'user_longitude': user_longitude
        }
        
    return render(request, 'chat.html', context)

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