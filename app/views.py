from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notebook

def index(request):
    # Handle the form submission
    if request.method=='POST':
        title = request.POST.get('title')
        notes = request.POST.get('notes')
        #prepare the ntoes for saving to the database
        notebook = Notebook(title=title, notes=notes)
        notebook.save()
        #redirect to home page after saving
        return redirect('/')

    # All the Get method will be handled here
    notes = Notebook.objects()
    return render(request,"index.html",{"context":notes},)
