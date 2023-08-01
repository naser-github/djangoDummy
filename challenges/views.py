from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup

# Create your views here.


def index(request):
    # return HttpResponse('Hello World')

    meetups = Meetup.objects.all()

    return render(request, 'challenges/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)

        return render(request, 'challenges/meetup_details.html', {
            'meetup_found' : True,
            'selected_meetup': selected_meetup 
        })
    except Exception as exc:
        return render(request, 'challenges/meetup_details.html', {
            'meetup_found' : False,
        })