from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .models import Blog
# Create your views here.

def introduction(request):
    return render(request, 'tutorials/1introduction.html')

def installation(request):
    return render(request, 'tutorials/2installation.html')

def first_program(request):
    return render(request, 'tutorials/3first_program.html')

def syntax(request):
    return render(request, 'tutorials/4syntax.html')

def variable(request):
    return render(request, 'tutorials/5variable.html')

def data_types(request):
    return render(request, 'tutorials/6data_types.html')

def numbers(request):
    return render(request, 'tutorials/7numbers.html')
    
def casting(request):
    return render(request, 'tutorials/8casting.html')

def strings(request):
    return render(request, 'tutorials/9strings.html')
#done
def booleans(request):
    return render(request, 'tutorials/10booleans.html')

def operators(request):
    return render(request, 'tutorials/11operators.html')

def lists(request):
    return render(request, 'tutorials/12lists.html')

def tuples(request):
    return render(request, 'tutorials/13tuples.html')

def sets(request):
    return render(request, 'tutorials/14sets.html')

def dictionaries(request):
    return render(request, 'tutorials/15dictionaries.html')

def if_else(request):
    return render(request, 'tutorials/16if_else.html')

# Other Functions
def about(request):
    return render(request, 'others/about.html')