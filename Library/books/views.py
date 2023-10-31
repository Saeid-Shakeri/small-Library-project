from django.shortcuts import render
from .models import book, Author
from django.http import HttpResponse
from django.template import loader



def list(request):
    query = book.objects.all()
    template = loader.get_template('all.html')
    return HttpResponse(template.render({'all_books': query}, request))



def book_detail(request,book_id):
    query = book.objects.get(pk=book_id)
    query2 = query.author.get()
    template = loader.get_template('book_detail.html')
    return HttpResponse(template.render({'book': query,'author': query2}, request))


def author_detail(request,author_id):
    query = Author.objects.get(pk=author_id)
    template = loader.get_template('author_detail.html')
    return HttpResponse(template.render({'author': query}, request))



def author_books_list(request,author_id):
    print(author_id)
    query = Author.objects.get(pk=author_id)
    query = query.book_set.all()



    template = loader.get_template('author_books_list.html')
    return HttpResponse(template.render({'author': query}, request))

