from django.shortcuts import render
from .models import Person, Sign

def home(request):
	homeText = "Welcome to the home page."
	context = {'homeText':homeText}
	return render(request, 'home.html', context=context)

def about(request):
	#person = Person.objects.get(first_name='Falon')
	#personAdd = Person.objects.create(first_name= "Petty", last_name= "Wap")

	aboutText = """ My areas of specialization are community art, activism
	fashion and music subculture.
	"""
	person = Person.objects.all()
	sign = Sign.objects.all()

	#Libra = Sign.objects.get(astrology_sign="Libra")
	#Gemini = Sign.objects.get(astrology_sign="Gemini")
	#Sagittarius = Sign.objects.get(astrology_sign="Sagittarius")

	#signList = Sign.objects.all()

	#personAdd.save()

	#context = {'aboutText':aboutText, "Libra":Libra, "Gemini":Gemini,"Sagittarius":Sagittarius, "signList":signList, 'person': person
	#}
	context = {'aboutText':aboutText, 'person':person, 'sign':sign,
	}

	return render(request=request, template_name='about.html', context=context)

	

def events(request):
	
	events_information = "These are upcoming events that I have organized."
	context = {'events_information': events_information}

	return render(request, 'events.html', context=context)