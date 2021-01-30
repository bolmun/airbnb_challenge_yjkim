from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [path("create/<int:book>", views.create_review_book, name="create-book")]
