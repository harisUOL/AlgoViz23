from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class AlgorithmCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    code = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(AlgorithmCategory, on_delete=models.CASCADE)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('algorithm-details', kwargs={'pk': self.pk})
