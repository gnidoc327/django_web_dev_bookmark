from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


#  ListVies
class BookmarkLV(ListView):
    model = Bookmark


#   DetailView
class BookmarkDV(DetailView):
    model = Bookmark