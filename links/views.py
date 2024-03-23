from django.shortcuts import render
from .models import Links


def links_me(request):
    """
    Renders the Links page
    """
    links = Links.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "links/links.html",
        {"links": links},
    )