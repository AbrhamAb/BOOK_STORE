from django.shortcuts import render
from .models import book   
# Create your views here.

def index(request):
    books = book.objects.all()
    return render(request, 'book_outlet/index.html', {'books': books})
def book_detail(request, slug):
    book_instance = book.objects.get(slug=slug)
    return render(request, 'book_outlet/book_detail.html', {'book': book_instance})