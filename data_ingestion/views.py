from django.shortcuts import render, redirect
from .models import Company, Files
from .forms import CompanyForm
from .utils import upload_file_to_blob_storage, blob_exists
import os

def upload_file(request):
    if request.method == 'POST':
        company_id = request.POST.get('company')
        file = request.FILES['pdf_file']
        company = Company.objects.get(id=company_id)
        
        # Upload file directly to blob storage
        blob_name = file.name
        if blob_exists(blob_name):
            error_message = f"File {blob_name} already exists in blob storage."
            companies = Company.objects.all()
            return render(request, 'upload_file.html', {'companies': companies, 'error_message': error_message})
        
        upload_file_to_blob_storage(file, blob_name)
        
        # Create Files record
        Files.objects.create(file_path=blob_name, company=company)
        
        return redirect('upload_file')
    
    companies = Company.objects.all()
    return render(request, 'upload_file.html', {'companies': companies})

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_file')  # Assuming you have a view to list companies
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form})