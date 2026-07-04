# Database Design

## Overview

This document describes the initial database schema for **Page Turner**, a Django book review application.

## Models

### Book

| Field             | Type      | Constraints                   |
|-------------------|-----------|-------------------------------|
| `id`              | BigAutoField | Primary key                |
| `title`           | CharField | max_length=255                |
| `cover_image_url` | URLField  | max_length=500, blank=True, default="" |

### Review

| Field         | Type        | Constraints                        |
|---------------|-------------|------------------------------------|
| `id`          | BigAutoField | Primary key                      |
| `book`        | ForeignKey  | → `Book`, CASCADE, related_name="reviews" |
| `author`      | ForeignKey  | → `AUTH_USER_MODEL`, CASCADE, related_name="reviews" |
| `review_text` | TextField   |                                    |
| `star_rating` | IntegerField| 0 ≤ value ≤ 10 (MinValueValidator / MaxValueValidator) |

## Relationships

- **Book 1 ── N Review**: A book can have many reviews. Deleting a book cascades to its reviews.
- **User 1 ── N Review**: A user (author) can write many reviews. Deleting a user cascades to their reviews.

## Constraints

- `star_rating` is enforced at the model level via Django validators (not database CHECK constraints).
- `cover_image_url` is optional (blank allowed, defaults to empty string).
