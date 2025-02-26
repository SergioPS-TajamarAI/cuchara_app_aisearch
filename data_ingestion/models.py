from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    website = models.URLField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Files(models.Model):
    file_path = models.CharField(max_length=200) #path to the blob storage file
    uploaded_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.file.name