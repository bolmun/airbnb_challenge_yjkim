from django.urls import path
from . import views

app_name = "favs"

urlpatterns = [
    path("toggle/<int:pk>", views.resolve_add, name="add"),
    path("list/", views.SeeFavsView.as_view(), name="see-favs"),
]
