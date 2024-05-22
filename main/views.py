from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Book
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
import os
from django.views.decorators.csrf import csrf_protect

def home(request):
    newest_book = Book.objects.all().order_by("-id")[0]
    context = {
        "newest_book": newest_book	
    }
    return render(request, "index.html", context)

@login_required
@csrf_protect
def upload(request):
    if request.method == "POST":
        title = request.POST["title"]
        book = request.FILES["book"]
        if title and book:
            Book.objects.create(title=title, file=book)
            return redirect("home")
    return render(request, "upload.html")

def download(request, id):
    book = Book.objects.get(id=id)
    file_path = book.file.path
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    else:
        raise Http404("File does not exist")

@csrf_protect
def login_u(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")