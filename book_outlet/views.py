from django.shortcuts import render
from .models import book   
# Create your views here.

def index(request):
    books = book.objects.all()
    return render(request, 'book_outlet/index.html', {'books': books})
def book_detail(request, book_id):
    book_instance = book.objects.get(id=book_id)
    return render(request, 'book_outlet/book_detail.html', {'book': book_instance})