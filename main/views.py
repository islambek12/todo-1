from django.shortcuts import render, HttpResponse
from .models import ToDo, BooksShop

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def book(request):
    # return HttpResponse("test 2 page")
    book_list = BooksShop.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def third(request):
    return HttpResponse("This is page test3")

def __str__(self):
    return self.name

def __str__(self):
    return self.title


def get_absolute_url(self):
    return reverse('book-detail', args=[str(self.id)])

def __str__(self):
    return '%s (%s)' % (self.id,self.book.title)

def get_absolute_url(self):
    return reverse('author-detail', args=[str(self.id)])


def __str__(self):
    return '%s, %s' % (self.last_name, self.first_name)

def __str__(self):
    return self.headline 
    