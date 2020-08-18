from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:title>/", views.displayEntry, name = "displayEntry"),
    path("pages/random/", views.randomPage, name = "randomEntry"),
    path("pages/search/", views.searchEntries, name = "searchEntries"),
    path("pages/create/", views.newPage, name = "createNewPage"),
    path("<str:title>/edit/", views.editPage, name = "editPage")
]