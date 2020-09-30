from rest_framework import serializers
from .models import JobOffer
from django.utils.timezone import now


class JobOfferSerializer(serializers.ModelSerializer):

    time_since_pubblication = serializers.SerializerMethodField()

    class Meta:
        model = JobOffer
        exclude = ("id",)

    def get_time_since_pubblication(self, object):
        created_at = object.created_at
        return (now() - created_at).days

    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                            "Salary must be a positive number!")
        return value

    def validate_job_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                            "Description must contain at least 10 characters!")
        return value

    def validate(self, data):
        if data["job_title"] == data["job_description"]:
            raise serializers.ValidationError(
                            "Title and description must be different!")
        return data
