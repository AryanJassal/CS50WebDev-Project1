from django.shortcuts import render
from markdown2 import Markdown
from random import choice

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.listEntries()
    })

def displayEntry(request, title):
    title = util.getEntry(title)
    htmlConverted = Markdown().convert(title)
    return render(request, "encyclopedia/displayEntry.html", {
        "mainBody": htmlConverted
    })

def randomPage(request):
    a = []
    for entry in entries:
        a.append(entry)

    randomEntry = random.choice(a)
    displayEntry(randomEntry)
    