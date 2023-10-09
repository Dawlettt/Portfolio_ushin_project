from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
)
from django.views.generic.edit import UpdateView, DeleteView
from .models import Articles
from django.urls import reverse_lazy, reverse


# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article_detail.html"


class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = "article_update.html"
    fields = ["title", "summary", "photo", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("articles")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Articles
    template_name = "article_create.html"
    fields = [
        "title",
        "summary",
        "body",
        "photo",
    ]

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
