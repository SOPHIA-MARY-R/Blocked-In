from django.db import models

# Create your models here.

class Site(models.Model):
    domain=models.CharField(max_length=50)
    link=models.URLField(max_length=1000)
    def __str__(self):
        return self.domain
