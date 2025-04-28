from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to="images",  blank=True)
    img = models.ImageField(upload_to="img",  blank=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

   