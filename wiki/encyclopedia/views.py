from django.shortcuts import render
from django.http import HttpResponseRedirect
from markdown2 import Markdown
import random

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
    return displayEntry(request, random.choice(util.listEntries()))