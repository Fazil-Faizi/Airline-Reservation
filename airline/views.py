from django.shortcuts import render
from .forms import FlightSearch
from .models import Flight


def airline(request):
    return render(request, 'airline/home.html')

def search_flight(request):
    form = FlightSearch(request.POST or None)
    context={

        'form':form,
    }

    if request.method == 'POST':
        	flights = Flight.objects.filter(departure__icontains=form['departure'].value(),
        									arrival__icontains=form['arrival'].value()
        									)
        	context = {
        	"form": form,
        	"flights": flights,
            }


    return render(request,"airline/search_flight.html",context)


def search_output(request):
    return render(request, 'airline/search_output.html')
