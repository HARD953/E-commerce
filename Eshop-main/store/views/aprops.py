from django.shortcuts import render
from store.models.product import Products

def apropos(request):
    return render(request,'aprops.html')
