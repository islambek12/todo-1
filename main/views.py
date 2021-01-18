from django.shortcuts import render, HttpResponse
from .models import ToDo

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


# Methods
def get_absolute_url(self):
    """
    Returns the url to access a particular instance of MyModelName.
    """
    return reverse('model-detail-view', args=[str(self.id)] 'book-detail', args=[str(self.id)] 'author-detail', args=[str(self.id)])

def __str__(self):
    """
    String for representing the MyModelName object (in Admin site etc.)
    """
    return self.field_name self.title '%s, %s' % (self.last_name, self.first_name)
    