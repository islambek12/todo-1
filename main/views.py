from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def books(request):
    # return HttpResponse("test 2 page")
    todo_list = ToDo.objects.all()
    return render(request, "books.html", {"todo_list": todo_list})

def third(request):
    return HttpResponse("This is page test3")

def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


def get_absolute_url(self):
    """
    Returns the url to access a particular book instance.
    """
    return reverse('book-detail', args=[str(self.id)])

def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)

def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


def __str__(self):
    """
    String for representing the Model object.
    """
    return '%s, %s' % (self.last_name, self.first_name)
