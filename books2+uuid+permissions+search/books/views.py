from django.db.models import Q # new
from re import template
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    
    def get_queryset(self): # new
        return Book.objects.filter(
            Q(title__icontains='beginners') | Q(title__icontains='api')
        )

"""
In chapter 13: Permissions we cover this mixins (for class based views)
    LoginRequiredMixin
    PermissionRequiredMixin
    UserPassesTestMixin
"""