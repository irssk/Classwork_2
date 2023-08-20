from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# !HW create Review model  : user , text , date
# !HW create Book model  : title , rating , desc , slug
class Ticket(models.Model):
    movie = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.FloatField()

class User(models.Model):
    user_name = models.CharField(max_length=50)
    tickets = models.ManyToManyField(Ticket)
    number_of_tickets = models.IntegerField(null=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    text = models.TextField()
    date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=23)
    rating = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self) -> str:
        return f"{self.title} : {self.rating}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Movie(models.Model):
    title = models.CharField(max_length=23)
    raitng = models.FloatField()
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self) -> str:
        return f"{self.title} : {self.raitng}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Place(models.Model):
    amount = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)