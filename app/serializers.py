from rest_framework import serializers

from . import models


class SerializedMovie(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['title', 'raitng', 'description', 'slug']


class SerializedTicket(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['movie', 'price']


class SerializedPlace(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ['amount', 'owner']

class SerializedReview(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['user', 'text', 'date']

class SerializedBook(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['title', 'rating', 'description', 'slug']


# !HW create Review serialized Model  : user , text , date
# !HW create Book serialized Model  : title , rating , desc , slug