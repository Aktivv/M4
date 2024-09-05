from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def text_view(request):
    return HttpResponse("httpresponse")


def main_page_view(request):
    return render(request, 'base.html')
