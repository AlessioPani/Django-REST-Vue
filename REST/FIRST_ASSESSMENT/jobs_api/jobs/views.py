from .models import JobOffer
from .serializers import JobOfferSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


class JobOfferListCreateAPIView(APIView):

    def get(self, request):
        job_offer = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(job_offer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)


class JobOfferDetailAPIView(APIView):

    def get_object(self, pk):
        job_offer = get_object_or_404(JobOffer, pk=pk)
        return job_offer

    def get(self, request, pk):
        job_offer = self.get_object(pk=pk)
        serializer = JobOfferSerializer(job_offer)
        return Response(serializer.data)

    def put(self, request, pk):
        job_offer = self.get_object(pk=pk)
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job_offer = self.get_object(pk=pk)
        job_offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
