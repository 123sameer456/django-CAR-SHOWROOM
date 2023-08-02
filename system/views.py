from django.shortcuts import render  , HttpResponse
from .models import Brand , Staff , Modell
from django.db.models import Q

def home(request):
    brand_names = Brand.objects.all()
    
    return render(request , "system/home.html" , {"brand_names" : brand_names })
    
def team(request ):
    members = Staff.objects.all()
    
    return render(request , "system/team.html" , {"members":members})

def team_member(request , id):
    team_member = Staff.objects.get(id = id)
    print(team_member)
    return render(request , "system/team_member.html" , {"member":team_member})


def brand_list(request , brand_id):
    brand_id = Brand.objects.get(pk = brand_id)
    return render(request , "system/list.html" , {"brand_id":brand_id})

def brand_details(request  , b):
    
    # print(b)
    brand_info = Modell.objects.filter( Q(brand = b.lower()) )
    print(brand_info)
    return render(request ,    'system/brand_details.html' ,  {'brand_info': brand_info })
    
    