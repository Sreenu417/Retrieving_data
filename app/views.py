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
    #ORDERING DATA
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.all().order_by('name')

    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.filter(topic_name='Kabaddi').order_by('-name')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all()
    
    #Field_lookups

    QSW=Webpage.objects.filter(name__startswith='m')
    QSW=Webpage.objects.filter(name__endswith='i')
    QSW=Webpage.objects.filter(name__contains='m')
    QSW=Webpage.objects.filter(name__in=['MS Dhoni','Virat Kohli'])
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(url__contains='https')
    QSW=Webpage.objects.filter(topic_name__in=['Foot Ball'])
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='MS Dhoni'))
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='Virat Kohli'))
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(url__startswith='https'))
    QSW=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name__endswith='o'))
    QSW=Webpage.objects.filter(Q(topic_name='Rugby') | Q(url__startswith='http'))
    
    
    

    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    QSA=AccessRecord.objects.all()

    # ORDERING DATA
    QSA=AccessRecord.objects.all().order_by(Length('name').desc())
    QSA=AccessRecord.objects.all().order_by(Length('name'))
    QSA=AccessRecord.objects.filter().order_by('date')
    QSA=AccessRecord.objects.all().order_by()

    # FIELD_LOOKUPS

    QSA=AccessRecord.objects.filter(date__year='1981')
    QSA=AccessRecord.objects.filter(date__month='11')
    QSA=AccessRecord.objects.filter(date__day='07')
    QSA=AccessRecord.objects.filter(date__year__gte='1994')
    QSA=AccessRecord.objects.filter(date__year__gt='1988')
    QSA=AccessRecord.objects.filter(date__year__lte='1961')
    QSA=AccessRecord.objects.filter(date__year__lt='1981')
    d={'accessrecords':QSA}
    return render(request,'display_accessrecords.html',d)