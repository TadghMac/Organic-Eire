from django.shortcuts import render
from .models import Links


def links_me(request):
    """
    Renders the Links page
    """
    links = Links.objects.all()

    return render(
        request,
        "links/links.html",
        {"links": links},
    )