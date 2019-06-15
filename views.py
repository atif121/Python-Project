from django.shortcuts import render, get_object_or_404
from .models import Category, Book
from django.db.models import Q



def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    
    books = Book.objects.filter(available=True)
    query = request.GET.get("q")
    if query:
        books = books.filter(name__icontains=query)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'books': books,
       
    }
    return render(request, 'store/book/list.html', context)
def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    context = {
        'book': book
    }
    return render(request, 'store/book/detail.html', context)

def about1(request):
    return render(request,'store/about1.html')