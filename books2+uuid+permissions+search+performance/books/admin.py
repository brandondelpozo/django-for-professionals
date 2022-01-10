from django.contrib import admin
from .models import Book, Review, Test


class ReviewInLine(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ("title", "author", "price")

admin.site.register(Book, BookAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ("name", "lasname",)

admin.site.register(Test)