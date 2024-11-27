from tempfile import template

from django.shortcuts import render
from django.shortcuts import render



# Create your views here.
def about(request):
    template = 'static/about.html'
    return render(request, template)


def rules(request):
    template = 'static/rules.html'
    return render(request, template)