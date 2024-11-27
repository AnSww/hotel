from django.shortcuts import render


def about(request):
    template = 'static/about.html'
    return render(request, template)


def rules(request):
    template = 'static/rules.html'
    return render(request, template)
