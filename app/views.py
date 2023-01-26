from django.shortcuts import render
from app.models import *

# Create your views here.

def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    QSA=AccessRecord.objects.all()
    d={'accessrecords':QSA}
    return render(request,'display_accessrecords.html',d)