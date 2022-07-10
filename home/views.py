from django.shortcuts import render
from django.http import HttpResponse
from home.models import Menu, cuisine


# Create your views here.
def index(request):
    return render(request, 'choose.html')
    # return HttpResponse("This is Homepage")


def menu(request):
    m = Menu.objects.all()
    c = cuisine.objects.all()
    context = {'me': m, 'cu': c}
    return render(request, 'menupage.html', context)
