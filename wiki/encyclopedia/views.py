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
    #entries = util.listEntries()                   #Version2

    #randomInt = random.radint(0, len(entries) - 1) #Version2
    #randomEntry = entries[randomInt]               #Version2

    #return util.displayEntry(randomEntry)          #Version2
    return util.displayEntry(random.choice(util.listEntries()))   #Version1
    