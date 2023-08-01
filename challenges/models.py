from django.db import models

#create your models here

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    images = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title} - {self.slug}'