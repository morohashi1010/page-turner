from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_image_url = models.URLField(max_length=500, blank=True, default="")

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reviews"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review_text = models.TextField()
    star_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return f"Review of '{self.book}' by {self.author}"
