from rest_framework import serializers
from news.models import Article, Journalist
from datetime import datetime
from django.utils.timesince import timesince
# Model-based Serializer


class ArticleSerializer(serializers.ModelSerializer):

    time_since_pubblication = serializers.SerializerMethodField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"
        # fields = ["author", "title", "description", "body"]

    def get_time_since_pubblication(self, object):
        pubblication_date = object.pubblication_date
        now = datetime.now()
        time_delta = timesince(pubblication_date, now)
        return time_delta

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Titolo e Descrizione devono essere diversi!")
        return data

    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError("Scrivi un titolo che abbia almeno 60 caratteri!")
        return value


class JournalistSerializer(serializers.ModelSerializer):

    # articles = related name of author field in Article
    # articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = Journalist
        # exclude = ("id",)
        fields = "__all__"
        # fields = ["author", "title", "description", "body"]


# Basic Serializer
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     pubblication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         """ Create and return a new instance of Article
#             based on validated data.
#         """
#         print(validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """ Updated and return an updated instance of Article
#             based on validated data.
#         """
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description',
#                                                   instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.pubblication_date = validated_data.get('pubblication_date',
#                                                         instance.pubblication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # Object-level validation
#     def validate(self, data):
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and description must be different!")
#         return data

#     # Field-level validation
#     def validate_title(self, value):
#         if len(value) < 60:
#             raise serializers.ValidationError("Title must have at least 60 characters!")
#         return data
