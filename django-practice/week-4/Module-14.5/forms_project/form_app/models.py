from django.db import models

# Create your models here.


class ContactModel(models.Model):
    album_name = models.CharField(max_length=200)
    email = models.EmailField()
    release_date = models.DateField(auto_now_add=True)
    ratings = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(max_length=1, choices=ratings)
