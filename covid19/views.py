from django.shortcuts import render
from datetime import datetime
from covid import Covid
import COVID19Py

def dashboard(request):

    now = datetime.now() 
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")


    covid19 = COVID19Py.COVID19()
    my_location = covid19.getLocationByCountryCode("BD")


    context = { 'id_of_country' : my_location[0]['id'],
                'last_updated' : date_time,
                'country' : my_location[0]['country'],
                'confirmed' : my_location[0]['latest']['confirmed'],
                'deaths' : my_location[0]['latest']['deaths'],
                'recovered' :  my_location[0]['latest']['recovered'] }
                	

    return render(request, 'index.html', context)


def worldwide(request):

    covid = Covid()

    active_case = covid.get_total_active_cases()
   
    recover = covid.get_total_recovered()
   
    death_case = covid.get_total_deaths()
    
    confirmed_case = covid.get_total_confirmed_cases()
    
    context = { 
                'active' : active_case,
                'recovered' :  recover,
                'confirmed' : confirmed_case,
                'deaths' :  death_case}

    return render(request, 'worldwide.html',context)


