from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup, Participant
from .forms import RegistrationForm

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
        if request.method == 'POST' :
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participant)
                
                #didn't do anything for video 27 
                # return redirect('confirm-registration', meetup_slug=meetup_slug)

        else:
            registration_form = RegistrationForm()

        return render(request, 'challenges/meetup_details.html', {
            'meetup_found' : True,
            'selected_meetup': selected_meetup,
            'form': registration_form,
        })
            
    except Exception as exc:
        return render(request, 'challenges/meetup_details.html', {
            'meetup_found' : False,
        })