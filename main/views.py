from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookShop

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


def books(request):
    book_list = BookShop.objects.all()
    return render(request, "books.html", {"book_list": book_list})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]    # print(form)
    todo = ToDo(text=text)      # print(text)
    todo.save()
    return redirect(test)       # HttpResponse("Forma poluchena")


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)


def add_books(request):
    return render(request, 'add_books.html')


def book_add(request):
    form = request.POST
    book = BookShop(title=form['book-title'], subtitle=form['book-subtitle'],
                         description=form['book-description'], price=form['book-price'],
                         genre=form['book-genre'], author=form['book-author'], year=form['book-year'])
    book.save()

    return redirect(books)


def delete_book(request, id):
    book = BookShop.objects.get(id=id)
    book.delete()

    return redirect(books)


def favorite_book(request, id):
    book = BookShop.objects.get(id=id)
    if book.is_favorite:
        book.is_favorite = False
    else:
        book.is_favorite = True
    book.save()
    return redirect(books)


def book_info(request, id):
    book = BookShop.objects.get(id=id)
    return render(request, 'books_detail.html', {'book': book})


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)




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
    