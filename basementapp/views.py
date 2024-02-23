from django.shortcuts import render, get_object_or_404
from .models import mastermodel, home_page, about_page

# Create your views here.
def Residents_collection_view(request):
    Residents = mastermodel.objects.all()
    return render(request, 'basementapp/accommodation.html', {'Residents': Residents})

def basement_accommodation_view(request):
    basements_Dlangezwa = home_page.objects.all()
    return render(request, 'basementapp/basements_accommodations.html', {'basements_Dlangezwa':basements_Dlangezwa})

def about_view(request):
    about_us = about_page.objects.all()
    return render(request, 'basementapp/basements_about.html', {'about_us':about_us})


def Resident_details_view(request, Resident_id):
    Resident = get_object_or_404(mastermodel, pk=Resident_id)
    return render(request, 'basementapp/basement_details.html', {'Resident':Resident})




