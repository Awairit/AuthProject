from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'testapp/home.html')

from django.contrib.auth.decorators import login_required
@login_required
def java_page_view(request):
    return render(request, 'testapp/java.html')

def python_page_view(request):
    return render(request, 'testapp/python.html')

def aptitude_page_view(request):
    return render(request, 'testapp/aptitude.html')