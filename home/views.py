from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    if request.method == "POST":
        image = request.FILES.get('image')

        Image.objects.create(image=image)

    return render(request, 'home.html')