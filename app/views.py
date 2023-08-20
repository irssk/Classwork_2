from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

# Create your views here.

# POST , GET , PUT , DELETE
# !HW create Book view  : title , rating , desc , slug


def get_data(amount, req, outer_model, outer_serializer):
    match(amount):
        case 'singular':
            model = outer_model

            serialized_model = outer_serializer(model)

            serialized_model_data = serialized_model.data

            return Response(serialized_model_data, status=status.HTTP_200_OK)

        case 'plural':
            model = outer_model

            serialized_model = outer_serializer(model, many=True)

            serialized_model_data = serialized_model.data

            return Response(serialized_model_data, status=status.HTTP_200_OK)

        case _:
            return Response({"msg": "Something went wrong!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movies(req):
    if req.method == "GET":
        return get_data(
            'plural',
            req,
            models.Movie.objects.all(),
            serializers.SerializedMovie
        )

    if req.method == "POST":
        models.Movie.objects.create(**req.data)

        return Response(serializers.SerializedMovie(models.Movie.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movie(req, movie_id):
    if req.method == "GET":
        return get_data(
            'singular',
            req,
            models.Movie.objects.get(id=movie_id),
            serializers.SerializedMovie
        )

    if req.method == "PUT":
        old_model = models.Movie.objects.get(id=movie_id)

        updated_item = serializers.SerializedMovie(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedMovie(models.Movie.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Movie.objects.get(id=movie_id)

        old_model.delete()

        return Response(serializers.SerializedMovie(models.Movie.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def customers(req):
    pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def customer(req):
    pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def books(req):
    if req.method == "GET":
        return get_data(
            'plural',
            req,
            models.Book.objects.all(),
            serializers.SerializedBook
        )

    if req.method == "POST":
        models.Book.objects.create(**req.data)

        return Response(serializers.SerializedBook(models.Book.objects.all(), many=True).data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def book(req, book_id):
    if req.method == "GET":
        return get_data(
            'singular',
            req,
            models.Book.objects.get(id=book_id),
            serializers.SerializedBook
        )

    if req.method == "PUT":
        old_model = models.Book.objects.get(id=book_id)

        updated_item = serializers.SerializedBook(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedBook(models.Book.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Book.objects.get(id=book_id)

        old_model.delete()

        return Response(serializers.SerializedBook(models.Book.objects.all(), many=True).data)