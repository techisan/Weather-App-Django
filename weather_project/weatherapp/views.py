from django.shortcuts import render
from django.contrib import messages
from .forms import CityForm
from .models import Cities
import requests

# Create your views here.

def index(request):

    API_key = <MY API KEY>
    city_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        print(form)
        
        if form.is_valid():
            form.save()

    form = CityForm()

    city_names = Cities.objects.values_list('city', flat=True)
    #print ('City Names', city_names)

    city_new = request.POST.get('city')
    
    weather_data = []

    for city_name in city_names:

        if city_new == city_name:
            url_construct = f'https://api.openweathermap.org/data/2.5/weather?q={city_new}&appid={API_key}&units=metric'

            response_ = requests.get(url_construct)
            e = response_.json()
        
            if e['cod'] == "404" or city_new == "":
                messages.info(request, 'Incorrect city name, try again.') # or print something 
            else:

                data = {
                    'city_name': e['name'], 
                    'weather':e['weather'][0]['main'],
                    'description' : e['weather'][0]['description'],
                    'temperature' : e['main']['temp'],
                    'pressure':e['main']['pressure'],
                    'humidity':e['main']['humidity'],
                    'visibility':e['visibility'],
                    'wind_speed':e['wind']['speed'],
                    'wind_deg':e['wind']['deg'],
                    'icon':e['weather'][0]['icon']
                    }
                city_data.append(data)
                #print(city_data)

        else:
            url_construct = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

            response_ = requests.get(url_construct)
            e = response_.json()
        
            if e['cod'] == "404" or city_name == "":
                messages.info(request, 'Incorrect city name, try again.') # or print something 
            else:
                weather = {
                'city_name': e['name'], 
                'weather':e['weather'][0]['main'],
                'description' : e['weather'][0]['description'],
                'temperature' : e['main']['temp'],
                'icon':e['weather'][0]['icon']
                }

            weather_data.append(weather)
    context = { 'weather_data': weather_data, 'city_data': city_data, 'form' : form}
    #print(context)
    return render(request, "index.html", context)