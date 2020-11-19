from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


def hello(request):
    return HttpResponse("Hello, world. b180da15 is the polls index.")
