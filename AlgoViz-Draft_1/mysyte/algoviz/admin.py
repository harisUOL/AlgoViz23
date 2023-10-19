from django.contrib import admin
from .models import Algorithm, AlgorithmCategory

admin.site.register(AlgorithmCategory)
admin.site.register(Algorithm)