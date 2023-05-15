from django.db import models


class Student(models.Model):
        Name = models.CharField(max_length=150)
        Age = models.IntegerField(default=18)
        def __str__(self) -> str:
                return self.Name

        
