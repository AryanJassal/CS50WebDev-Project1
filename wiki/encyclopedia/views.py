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
    #entries = util.listEntries()

    #randomInt = random.radint(0, len(entries) - 1)
    #randomEntry = entries[randomInt] 

    #entryName = util.getEntry(randomEntry)

    return displayEntry(request, random.choice(util.listEntries()))

    #return HttpResponseRedirect(displayEntry(), args=[request, "CSS"])