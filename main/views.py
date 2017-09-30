from django.shortcuts import render
from main.forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'You successfully registered.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
