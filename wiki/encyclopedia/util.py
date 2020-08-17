import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def listEntries():
    _, filenames = default_storage.listdir("entries")

    return list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))

def saveEntry(title, content):
    filename = f"entries/{title}.md"

    if default_storage.exists(filename):
        default_storage.delete(filename)

    default_storage.save(filename, ContentFile(content))

def getEntry(title):
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")

    except FileNotFoundError:
        return None