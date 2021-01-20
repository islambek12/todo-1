from django.db import models
# from django.urls import reverse
# import uuid # Required for unique book instances

class ToDo(models.Model):
    text = models.CharField(max_length=100, verbose_name='Задача')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_closed = models.BooleanField(default=False, verbose_name='Выполнена')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранная')
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class BooksShop(models.Model):
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=50, verbose_name='Подзаголовок')
    description = models.CharField(max_length=650, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    genre = models.CharField(max_length=60, verbose_name='Жанр')
    author = models.CharField(max_length=35, verbose_name='Автор')
    year = models.DateField(verbose_name='Год выпуска книги')
    date = models.DateField(auto_now_add=True, verbose_name='Добавление книги на сайт')

    class Meta:
        verbose_name = 'Книжный магазин'
        verbose_name_plural = 'Книжные магазины'


# class Genre(models.Model):
#     """
#     Model representing a book genre (e.g. Science Fiction, Non Fiction).
#     """
#     name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

# class Book(models.Model):
#     """
#     Model representing a book (but not a specific copy of a book).
#     """
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
#     # Foreign Key used because book can only have one author, but authors can have multiple books
#     # Author as a string rather than object because it hasn't been declared yet in the file.
#     # summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
#     # isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
#     genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

# class BookInstance(models.Model):
#     """
#     Model representing a specific copy of a book (i.e. that can be borrowed from the library).
#     """
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
#     book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#     imprint = models.CharField(max_length=200)
#     due_back = models.DateField(null=True, blank=True)

#     LOAN_STATUS = (
#         ('m', 'Maintenance'),
#         ('o', 'On loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )

#     status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

#     class Meta:
#         ordering = ["due_back"]

# class Author(models.Model):
#     """
#     Model representing an author.
#     """
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('Died', null=True, blank=True)

# class Entry(models.Model):
#     blog = models.ForeignKey(Book, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
    