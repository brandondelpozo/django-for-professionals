import uuid
from django.contrib.auth import get_user_model  # new
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)  # new

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': str(self.pk)})


class Review(models.Model):  # new
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """test comm 13"""
        return self.review
"""
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
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
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
git remote set-url origin https://<USERNAME>:<PASSWORD>@bitbucket.org/path/to/repo.git
https://github.com/brandondelpozo/django-for-professionals.git
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
"""