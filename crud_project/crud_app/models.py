from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.EmailField()
    gender = models.CharField(max_length=10, choices=[("M","Male"), ("F","Female")])
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name