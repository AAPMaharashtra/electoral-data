from django.shortcuts import render, redirect
from electoral_data.models import LokSabhaSeat,AssemblyConstituency,PollingStation,Society,Citizen,CitizenInterestForm, SocietyProcessedForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def index(request):
	if request.user.is_staff:
		return redirect("/admin/")
	else:		
		return redirect("/view/societies/"+str(request.user.get_profile().polling_station.id))

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
	if request.method == 'POST':
		society = Society.objects.get(society_no=society_id)
		form = SocietyProcessedForm(request.POST, instance=society)
		form.save()
		polling_id = society.polling_station.id
		return redirect('/view/societies/'+str(polling_id))
	else:
		form = SocietyProcessedForm(instance=citizens_list[0])
		context = {'citizens_list': citizens_list,'society_id': society_id,'form': form}
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
	
