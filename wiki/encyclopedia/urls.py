from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:title>", views.displayEntry, name = "displayEntry"),
    path("random/", views.randomPage, name = "randomEntry"),
    path("search/", views.searchEntries, name = "searchEntries"),
    path("create/", views.newPage, name = "createNewPage")
]