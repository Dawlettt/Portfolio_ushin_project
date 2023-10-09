from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("post/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("post/<int:pk>/edit", ArticleUpdateView.as_view(), name="article_update"),
    path("post/<int:pk>/delete", ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_create"),
]
