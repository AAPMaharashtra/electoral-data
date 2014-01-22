from django.shortcuts import render, redirect
from electoral_data.models import LokSabhaSeat,AssemblyConstituency,PollingStation,Society,Citizen,CitizenInterestForm, SocietyProcessedForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def index(request):
	if request.user.is_staff:
		return redirect("/admin/")
	else:		
		return redirect("/societies/"+str(request.user.get_profile().polling_station.id))

# Show LS seats
@login_required(login_url='/login')
def ls(request):
	if request.user.is_staff:
		ls_seats_list = LokSabhaSeat.objects.all()
		context = {'ls_seats_list': ls_seats_list}
		return render(request, 'electoral_data/ls.html', context)
	else:
		return redirect("/societies/"+str(request.user.get_profile().polling_station.id))
	
# Show Assembly seats for LS
@login_required(login_url='/login')
def assembly(request,ls_id):
	if request.user.is_staff:
		assembly_list = AssemblyConstituency.objects.filter(lok_sabha_seat=ls_id)
		context = {'assembly_list': assembly_list}
		return render(request, 'electoral_data/assembly.html', context)
	else:
		return redirect("/societies/"+str(request.user.get_profile().polling_station.id))

# Show Polling booths for the Assembly seat
@login_required(login_url='/login')
def polling(request,assembly_id):
	if request.user.is_staff:
		polling_list = PollingStation.objects.filter(constituency=assembly_id)
		context = {'polling_list': polling_list}
		return render(request, 'electoral_data/polling.html', context)
	else:
		return redirect("/societies/"+str(request.user.get_profile().polling_station.id))

# Show societies for the Polling Station
@login_required(login_url='/login')
def societies(request,polling_id):
	societies_list = Society.objects.filter(polling_station=polling_id)
	polling_station = PollingStation.objects.get(id=polling_id)
	context = {'societies_list': societies_list,'polling_station': polling_station}
	return render(request, 'electoral_data/society.html', context)

# Show Citizens in the Society
@login_required(login_url='/login')
def citizens(request,society_id):
	citizens_list = Citizen.objects.filter(society=society_id)
	if request.method == 'POST':
		society = Society.objects.get(society_no=society_id)
		form = SocietyProcessedForm(request.POST, instance=society)
		form.save()
		polling_id = society.polling_station.id
		return redirect('/societies/'+str(polling_id))
	else:
		form = SocietyProcessedForm(instance=citizens_list[0])
		context = {'citizens_list': citizens_list,'society_id': society_id,'form': form}
		return render(request, 'electoral_data/citizen.html', context)


# Show Citizen details
@login_required(login_url='/login')
def detail(request,citizen_id):
	citizen_details = Citizen.objects.filter(id=citizen_id)
	if request.method == 'POST':
		form = CitizenInterestForm(request.POST, instance=citizen_details[0])
		form.save()
		society_id = citizen_details[0].society.society_no
		return redirect('/citizens/'+society_id)
	else:
		form = CitizenInterestForm(instance=citizen_details[0])
		context = {'citizen_details': citizen_details,'form': form}
		return render(request, 'electoral_data/detail.html', context)
		
	
