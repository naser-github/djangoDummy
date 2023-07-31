from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('Hello World')

    meetups = [
        {'title': 'First Meetup', 'location': 'Banani', 'slug': 'first'},
        {'title': 'Second Meetup', 'location': 'Istanbul', 'slug': 'second'},
    ]

    return render(request, 'challenges/index.html', {
        'showMeetup': True,
        'meetups': meetups
    })


def meetup_details(request):
    selected_meetup = {'title': 'First Meetup', 'location': 'Banani', 'slug': 'first', 'description': 'sdf khjsd;fj dsjfkl jdsa;f ' },

    return render(request, 'challenges/meetup_details.html', {
        'selected_meetup': selected_meetup
    })