from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ToDo, BooksShop

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3")


def booksShop(request):
    book_list = BooksShop.objects.all()
    return render(request, "books.html", {"book_list": book_list})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]    # print(form)
    todo = ToDo(text=text)      # print(text)
    todo.save()
    return redirect(test)       # HttpResponse("Forma poluchena")



# def __str__(self):
#     return self.name

# def __str__(self):
#     return self.title


# def get_absolute_url(self):
#     return reverse('book-detail', args=[str(self.id)])

# def __str__(self):
#     return '%s (%s)' % (self.id,self.book.title)

# def get_absolute_url(self):
#     return reverse('author-detail', args=[str(self.id)])


# def __str__(self):
#     return '%s, %s' % (self.last_name, self.first_name)

# def __str__(self):
#     return self.headline 
    