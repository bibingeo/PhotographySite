from django.shortcuts import render
from .forms import ContactForm ,BooknowForm
from .models import contactinfo

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def photo(request):
    return render(request,'gallery.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html',{'form' : form})

def booknow(request):
    form = BooknowForm()
    if request.method == 'POST':
        form = BooknowForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'booknow.html', {'form': form})

