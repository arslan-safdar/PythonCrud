from django.db import models

class Receipes(models.Model):
   receipe_name = models.CharField(max_length=200)
   receipe_description = models.TextField()
   receipe_image = models.ImageField()