from django.shortcuts import render


def home_view(request):
    """ A view to return home page"""
    context = {}
    return render(request, "home.html")
