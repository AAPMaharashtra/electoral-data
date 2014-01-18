from django.shortcuts import render
from electoral_data.models import LokSabhaSeat,AssemblyConstituency,PollingStation,Society,Citizen,CitizenInterestForm


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is the AAP electoral data page")

# Show LS seats
def ls(request):
	ls_seats_list = LokSabhaSeat.objects.all()
	context = {'ls_seats_list': ls_seats_list}
	return render(request, 'electoral_data/ls.html', context)
	
# Show Assembly seats for LS
def assembly(request,ls_id):
	assembly_list = AssemblyConstituency.objects.filter(lok_sabha_seat=ls_id)
	context = {'assembly_list': assembly_list}
	return render(request, 'electoral_data/assembly.html', context)

# Show Polling booths for the Assembly seat
def polling(request,assembly_id):
	polling_list = PollingStation.objects.filter(constituency=assembly_id)
	context = {'polling_list': polling_list}
	return render(request, 'electoral_data/polling.html', context)

# Show societies for the Polling Station
def societies(request,polling_id):
	societies_list = Society.objects.filter(polling_station=polling_id)
	context = {'societies_list': societies_list}
	return render(request, 'electoral_data/society.html', context)

# Show Citizens in the Society
def citizens(request,society_id):
	citizens_list = Citizen.objects.filter(society=society_id)
	context = {'citizens_list': citizens_list}
	return render(request, 'electoral_data/citizen.html', context)

# Show Citizen details
def detail(request,citizen_id):
	if request.method == 'POST':
		inst = Citizen.objects.get(pk=citizen_id)
		form = CitizenInterestForm(request.POST, instance=inst)
		form.save()
	else:
		citizen_details = Citizen.objects.filter(id=citizen_id)
		form = CitizenInterestForm(instance=citizen_details[0])
		context = {'citizen_details': citizen_details,'form': form}
		return render(request, 'electoral_data/detail.html', context)
	
