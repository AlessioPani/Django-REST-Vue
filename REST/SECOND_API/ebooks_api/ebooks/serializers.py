from rest_framework import serializers
from .models import eBook, Review


class ReviewSerializer(serializers.ModelSerializer):

    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ["ebook"]  # Passed automatically via perform_create


class eBookSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = eBook
        fields = "__all__"
