from django.shortcuts import render
from django.shortcuts import redirect, reverse
from books import models as book_models
from . import forms


def create_review_book(request, book):

    if request.method == "GET":
        form = forms.CreateReviewForm()
        return render(
            request,
            "reviews/review_form.html",
            {"form": form},
        )

    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        book = book_models.Book.objects.get_or_none(pk=book)
        if not book:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.book = book
            review.created_by = request.user
            review.save()
            return redirect(reverse("books:book", kwargs={"pk": book.pk}))
