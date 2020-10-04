from .views import eBookDetail, eBookListCreate, ReviewCreate, ReviewDetail
from django.urls import path


urlpatterns = [
    path('ebooks/',
         eBookListCreate.as_view(),
         name="ebook-list"),

    path('ebooks/<int:pk>/',
         eBookDetail.as_view(),
         name="ebook-detail"),

    path('ebooks/<int:ebook_pk>/reviews/',
         ReviewCreate.as_view(),
         name="reviews-ebook"),

    path('ebooks/<int:ebook_pk>/reviews/<int:pk>',
         ReviewDetail.as_view(),
         name="review-detail"),
]
