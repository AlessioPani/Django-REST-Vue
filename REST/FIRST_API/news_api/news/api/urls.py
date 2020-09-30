from django.urls import path
from news.api.views import ArticleDetailAPI, ArticleListCreateAPI, JournalistListCreateAPI
# from news.api.views import article_detail_api_view, article_list_create_api_view


urlpatterns = [
    # path('articles/', article_list_create_api_view, name="article-list"),
    # path('articles/<int:pk>/', article_detail_api_view, name="article-detail"),
    path('articles/', ArticleListCreateAPI.as_view(), name="article-list"),
    path('articles/<int:pk>/', ArticleDetailAPI.as_view(), name="article-detail"),
    path('journalists/', JournalistListCreateAPI.as_view(), name="journalist-list")

]