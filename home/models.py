from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    file = models.FileField()
    image = models.ImageField()

class Car(models.Model):
    name = models.CharField(max_length=500)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} (Speed: {self.speed})"
