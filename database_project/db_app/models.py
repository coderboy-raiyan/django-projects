from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(null=True)

    def __str__(self) -> str:
        return f'Roll - {self.roll} : Name : - {self.name}'
