from django.shortcuts import render
from django import forms
#from django.http import HttpResponse
from markdown2 import Markdown
import random

from . import util

class searchForm(forms.Form):
    q = forms.CharField(label = "", widget = forms.TextInput(attrs={"placeholder": "Search Encyclopedia..."}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.listEntries(),
        "form": searchForm()
    })

def displayEntry(request, title):
    title = util.getEntry(title)
    htmlConverted = Markdown().convert(title)
    return render(request, "encyclopedia/displayEntry.html", {
        "mainBody": htmlConverted,
        "form": searchForm()
    })

def randomPage(request):
    return displayEntry(request, random.choice(util.listEntries()))

def searchEntries(request):
    if request.method == "POST":
        form = searchForm(request.POST)

        if form.is_valid():
            searchString = form.cleaned_data["q"]
        else:
            searchString = ""

    entries = util.listEntries()

    if searchString in entries:
        return displayEntry(request, searchString)

    elif any(searchString.lower() in s.lower() for s in entries):
        matches = [s for s in entries if searchString.lower() in s.lower()]

        return render(request, "encyclopedia/searchResults.html", {
            "matches": matches,
            "foundResults": True,
            "form": searchForm()
        })

    else:
        return render(request, "encyclopedia/searchResults.html", {
            "matches": None,
            "foundResults": False,
            "form": searchForm()
        })