from django.db import models
from django.contrib.auth.models import User


class Receipes(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
   receipe_name = models.CharField(max_length=200)
   receipe_description = models.TextField()
   receipe_image = models.ImageField()

class StudentID(models.Model):
   student_id = models.CharField(max_length=100)

   def __str__(self) -> str:
      return self.student_id
   
class Subject(models.Model):
   subject_name = models.CharField(max_length=100)

   def __str__(self) -> str:
      return self.subject_name
   
class Department(models.Model):
   department = models.CharField(max_length=100)

   def __str__(self) -> str:
      return self.department
   
class Student(models.Model):
   student_id = models.ForeignKey(StudentID,related_name="student",on_delete=models.CASCADE)
   department = models.ForeignKey(Department,related_name="dept",on_delete=models.CASCADE)
   student_name = models.CharField(max_length=60)
   student_age = models.IntegerField(default=18)
   student_email = models.EmailField(unique=True)
   student_address = models.TextField()

   def __str__(self) -> str:
      return self.student_name

class StudentMarks(models.Model):
   student = models.ForeignKey(Student ,related_name="subjectmarks", on_delete=models.CASCADE)
   subject = models.ForeignKey(Subject  , on_delete=models.CASCADE)
   marks = models.IntegerField()

   def __str__(self) -> str:
      return f'{self.student.student_name}, {self.subject.subject_name}'
   
   # class Meta:
   #    unique_together = ['student','subject']
   



