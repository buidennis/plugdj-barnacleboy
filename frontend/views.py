from django.shortcuts import render

# Create your views here.


# Takes the templates directory and move up
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
