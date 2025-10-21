from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length = 100)
    full_name = models.CharField(max_length = 250)
    course = models.CharField(max_length = 100)
    year_level = models.IntegerField()

def __str__(self):
    return f"{self.student_id}{self.full_name}"