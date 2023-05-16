from django.db import models
from django.contrib.auth.models import User

class Receipes(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
   receipe_name = models.CharField(max_length=200)
   receipe_description = models.TextField()
   receipe_image = models.ImageField()