from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_topics(request):
    QST=Topic.objects.filter(topic_name='Cricket')
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='valley ball')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.all().order_by('name')

    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.filter(topic_name='Kabaddi').order_by('-name')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all()
    
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.all().order_by(Length('name').desc())
    QSA=AccessRecord.objects.all().order_by(Length('name'))
    QSA=AccessRecord.objects.filter().order_by('date')
    QSA=AccessRecord.objects.all().order_by()
    d={'accessrecords':QSA}
    return render(request,'display_accessrecords.html',d)