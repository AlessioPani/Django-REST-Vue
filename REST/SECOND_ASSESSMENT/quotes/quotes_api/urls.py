from django.urls import path
from .views import QuoteListCreate, QuoteUpdateDelete


urlpatterns = [
    path('quotes/', QuoteListCreate.as_view(), name='quotes-list'),
    path('quotes/<int:pk>', QuoteUpdateDelete.as_view(), name='quotes-detail'),
]