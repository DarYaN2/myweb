from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')



def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')