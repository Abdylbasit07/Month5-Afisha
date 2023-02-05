from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

class DirectorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
         model = Movie
         fields = 'id title'.split()


class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title duration description'.split()


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'text'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieReviewSerilizer(serializers.ModelSerializer):
    movies_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title movies_reviews rating'.split()