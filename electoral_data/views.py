from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from electoral_data.models import LokSabhaSeat,AssemblyConstituency,PollingStation,Society,Citizen,CitizenInterestForm


# Create your views here.
@login_required(login_url='/login')
def index(request):
	if request.user.is_staff:
		return HttpResponseRedirect("/admin/")
	else:		
		return HttpResponseRedirect("/view/societies/"+str(request.user.get_profile().polling_station.id))

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
	context = {'citizens_list': citizens_list,'society_id': society_id[:-3]}
	return render(request, 'electoral_data/citizen.html', context)

# Show Citizen details
def detail(request,citizen_id):
	citizen_details = Citizen.objects.filter(id=citizen_id)
	if request.method == 'POST':
		form = CitizenInterestForm(request.POST, instance=citizen_details[0])
		form.save()
	else:
		form = CitizenInterestForm(instance=citizen_details[0])
		
	context = {'citizen_details': citizen_details,'form': form}
	return render(request, 'electoral_data/detail.html', context)
	
