from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article

# Create your views here.


def Home(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/home.html", context)


