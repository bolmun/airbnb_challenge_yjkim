from django.views.generic import ListView, DetailView, CreateView, UpdateView
from movies.models import Movie
from reviews.forms import CreateReviewForm


class MoviesView(ListView):

    model = Movie
    paginate_by = 12
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Movies"
        return context


class MovieDetail(DetailView):
    model = Movie
    context_object_name = "movie"


class CreateMovie(CreateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )


class UpdateMovie(UpdateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
