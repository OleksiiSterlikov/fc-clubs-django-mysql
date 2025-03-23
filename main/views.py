from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'main/index.html', {'menu_items': menu_items})