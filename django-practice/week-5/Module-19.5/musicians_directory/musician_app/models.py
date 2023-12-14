from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=12)
    instruments = [
        ("Guitar", "Guitar"),
        ("Piano", "Piano"),
        ("Violin", "Violin"),
        ("Cello", "Cello"),
        ("Brass instrument", "Brass instrument"),
    ]
    instrument_type = models.CharField(max_length=100, choices=instruments)
    timestamps = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email


class Album(models.Model):
    album_name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)
    ratings = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(max_length=1, choices=ratings)

    def __str__(self) -> str:
        return self.album_name
