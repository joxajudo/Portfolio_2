from django.shortcuts import render, redirect

# Create your views here.
from app.models import Contact


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.text = text
        contact.save()
        return redirect('index')
    return render(request, 'index.html')
