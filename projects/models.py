from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images",  blank=True)
