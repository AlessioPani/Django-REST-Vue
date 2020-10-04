from django.shortcuts import get_object_or_404, render
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from .models import eBook, Review
from .serializers import eBookSerializer, ReviewSerializer
from .permissions import isAdminUserOrReadOnly, isReviewAuthorOrReadOnly
from .pagination import SmallSetPagination
# Create your views here.

# VIEW THAT EXTENDS CONCRETE GENERIC API VIEWS


class eBookListCreate(generics.ListCreateAPIView):
    queryset = eBook.objects.all().order_by("pk")
    serializer_class = eBookSerializer
    permission_classes = [isAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class eBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = eBook.objects.all()
    serializer_class = eBookSerializer
    permission_classes = [isAdminUserOrReadOnly]


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(eBook, pk=ebook_pk)
        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook,
                                                review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this ebook.")
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [isReviewAuthorOrReadOnly]


# VIEW THAT EXTENDS GENERICAPIVIEW AND THE RELATED MIXINS


# class eBookListCreate(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       generics.GenericAPIView):

#     queryset = eBook.objects.all()
#     serializer_class = eBookSerializer

#     def get(self, request, *args, **kargs):
#         return self.list(request, *args, **kargs)

#     def post(self, request, *args, **kargs):
#         return self.create(request, *args, **kargs)
