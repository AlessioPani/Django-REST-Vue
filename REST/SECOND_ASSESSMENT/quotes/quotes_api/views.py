from django.shortcuts import render
from rest_framework import views
from rest_framework import generics
from rest_framework import permissions
from .serializer import QuoteSerializer
from .models import Quote
from .permissions import isAdminOrReadOnly
from .pagination import QuoteList

# Create your views here.


class QuoteListCreate(generics.ListCreateAPIView):

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [isAdminOrReadOnly]
    pagination_class = QuoteList

    def perform_create(self, serializer):
        author_id = self.request.user
        serializer.save(author=author_id)


class QuoteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAdminUser]
