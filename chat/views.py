from django.shortcuts import render
from django.http import HttpResponse
from .utils import ask_indexer
from data_ingestion.utils import get_pdf

def search_view(request):
    query = ''
    results = []
    if request.method == 'POST':
        query = request.POST.get('q', '')
        results = ask_indexer(query) if query else []
    return render(request, 'chat.html', {'results': results, 'query': query})

def get_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        file_content = get_pdf(file_name)
        response = HttpResponse(file_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    return HttpResponse(status=400)
