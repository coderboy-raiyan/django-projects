from django.db import models
from authors.models import Author
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=120)
    about = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name