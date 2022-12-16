from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.


def index(request):
    if request.method == 'POST':
        add_book = forms.bookform(request.POST, request.FILES)
        if add_book.is_valid():
            myform = add_book.save()

    if request.method == 'POST':
        add_category = forms.categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    category = models.category.objects.all()
    book = models.book.objects.all()
    total_books = models.book.objects.all().count()
    sold_books = models.book.objects.filter(status='sold').count()
    rental_books = models.book.objects.filter(status='rental').count()
    avaliable_books = models.book.objects.filter(status='avaliable').count()
    context = {
        'category': category,
        'books': book,
        'form1': forms.bookform,
        'form2': forms.categoryform(),
        'count': total_books,
        'sold': sold_books,
        'rental': rental_books,
        'avaliable': avaliable_books,
    }
    return render(request, 'pages/index.html', context)


def books(request):

    if request.method == 'POST':
        add_category = forms.categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    category = models.category.objects.all()
    book = models.book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        book = book.filter(title__contains=title)
    context = {
        'category': category,
        'books': book,
        'form1': forms.bookform(),
        'form2': forms.categoryform(),
    }
    return render(request, 'pages/books.html', context)


def delete(request, pk):
    book_delete = models.book.objects.get(pk=pk)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')

    if request.method == 'POST':
        add_category = forms.categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    category = models.category.objects.all()
    book = models.book.objects.all()
    context = {
        'category': category,
        'books': book,
        'form1': forms.bookform(),
        'form2': forms.categoryform(),
    }
    return render(request, 'pages/delete.html', context)


def update(request, pk):
    book_id = models.book.objects.get(pk=pk)
    if request.method == 'POST':
        book_save = forms.bookform(
            request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = forms.bookform(instance=book_id)

    if request.method == 'POST':
        add_category = forms.categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    category = models.category.objects.all()
    book = models.book.objects.all()
    context = {
        'category': category,
        'books': book,
        'form1': forms.bookform(),
        'form2': forms.categoryform(),
        'form3': book_save,
    }
    return render(request, 'pages/update.html', context)
