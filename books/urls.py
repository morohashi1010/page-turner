from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/review/', views.submit_review, name='submit_review'),
]
