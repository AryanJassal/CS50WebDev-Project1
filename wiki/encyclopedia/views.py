from django.shortcuts import render
from django import forms
#from django.http import HttpResponse
from markdown2 import Markdown
import random

from . import util

class searchForm(forms.Form):
    q = forms.CharField(label = "", widget = forms.TextInput(attrs={"placeholder": "Search Encyclopedia..."}))

class newEntryForm(forms.Form):
    title = forms.CharField(label = "", widget = forms.TextInput(attrs={"placeholder": "Title", "class": "form-control col-md-8 col-lg-10"}))
    content = forms.CharField(label = "", widget = forms.Textarea(attrs={"placeholder": "Enter content in Markdown...", "class": "form-control col-md-8 col-lg-10", "rows": 30}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.listEntries(),
        "form": searchForm()
    })

def displayEntry(request, title):
    entry = util.getEntry(title)
    htmlConverted = Markdown().convert(entry)
    return render(request, "encyclopedia/displayEntry.html", {
        "mainBody": htmlConverted,
        "title": title,
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

def newPage(request):
    if request.method == "POST":
        newPage = newEntryForm(request.POST)

        if newPage.is_valid():
            title = newPage.cleaned_data["title"]
            content = newPage.cleaned_data["content"]
        else:
            title, content = "", ""

        if util.getEntry(title) == None:
            util.saveEntry(title, content)
        else:
            return render(request, "encyclopedia/error.html", {
                "form": searchForm(),
                "errorText": "Entry with this name already exists."
            })

        return displayEntry(request, title)

    else:
        return render(request, "encyclopedia/newPage.html", {
            "newPageForm": newEntryForm(),
            "form": searchForm()
        })

def editPage(request, title):
    pageContent = util.getEntry(title)

    entry = newEntryForm()
    entry.fields["title"].initial = title
    entry.fields["content"].initial = pageContent

    return render(request, "encyclopedia/editPage.html", {
        "editPage": entry,
        "title": title,
        "form": searchForm()
    })