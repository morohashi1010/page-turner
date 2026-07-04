import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Book, Review

User = get_user_model()


@pytest.mark.django_db
class TestBookModel:
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            cover_image_url="https://example.com/cover.jpg",
        )
        assert book.title == "Test Book"
        assert book.cover_image_url == "https://example.com/cover.jpg"
        assert str(book) == "Test Book"

    def test_book_cover_image_url_defaults_to_blank(self):
        book = Book.objects.create(title="No Cover")
        assert book.cover_image_url == ""


@pytest.mark.django_db
class TestReviewModel:
    def test_create_review(self):
        user = User.objects.create_user(username="reviewer")
        book = Book.objects.create(title="Reviewable Book")
        review = Review.objects.create(
            book=book,
            author=user,
            review_text="Great book!",
            star_rating=8,
        )
        assert review.book == book
        assert review.author == user
        assert review.review_text == "Great book!"
        assert review.star_rating == 8
        assert str(review) == "Review of 'Reviewable Book' by reviewer"

    def test_star_rating_min_value(self):
        user = User.objects.create_user(username="critic")
        book = Book.objects.create(title="Test")
        review = Review(
            book=book,
            author=user,
            review_text="Too low",
            star_rating=-1,
        )
        with pytest.raises(ValidationError):
            review.full_clean()

    def test_star_rating_max_value(self):
        user = User.objects.create_user(username="fan")
        book = Book.objects.create(title="Test")
        review = Review(
            book=book,
            author=user,
            review_text="Too high",
            star_rating=11,
        )
        with pytest.raises(ValidationError):
            review.full_clean()

    def test_star_rating_boundary_values(self):
        user = User.objects.create_user(username="rater")
        book = Book.objects.create(title="Boundaries")

        review_0 = Review.objects.create(
            book=book, author=user, review_text="zero", star_rating=0
        )
        review_10 = Review.objects.create(
            book=book, author=user, review_text="ten", star_rating=10
        )
        assert review_0.star_rating == 0
        assert review_10.star_rating == 10

    def test_cascade_delete_book(self):
        user = User.objects.create_user(username="author")
        book = Book.objects.create(title="Delete Me")
        Review.objects.create(
            book=book,
            author=user,
            review_text="Will be deleted",
            star_rating=5,
        )
        book.delete()
        assert Review.objects.count() == 0

    def test_cascade_delete_user(self):
        user = User.objects.create_user(username="goner")
        book = Book.objects.create(title="Orphaned?")
        Review.objects.create(
            book=book,
            author=user,
            review_text="Author gone",
            star_rating=5,
        )
        user.delete()
        assert Review.objects.count() == 0
