from django.shortcuts import render
from django.shortcuts import redirect, reverse
from books import models as book_models
from movies import models as movie_models
from . import forms


def create_review(request, pk):

    if request.method == "GET":
        form = forms.CreateReviewForm()
        return render(
            request,
            "reviews/review_form.html",
            {"form": form},
        )

    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        type = request.GET.get("type")
        if type == "book":
            book = book_models.Book.objects.get_or_none(pk=pk)
            if not book:
                return redirect(reverse("core:home"))
            if form.is_valid():
                review = form.save()
                review.book = book
                review.created_by = request.user
                review.save()
                return redirect(reverse("books:book", kwargs={"pk": book.pk}))
        if type == "movie":
            movie = movie_models.Movie.objects.get_or_none(pk=pk)
            if not movie:
                return redirect(reverse("core:home"))
            if form.is_valid():
                review = form.save()
                review.movie = movie
                review.created_by = request.user
                review.save()
                return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))
