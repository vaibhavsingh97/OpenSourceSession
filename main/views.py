from django.shortcuts import render
from main.forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    form_class = RegisterForm
    
    return render(request, 'register.html', {
        'form': form_class,
    })