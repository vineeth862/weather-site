from django.shortcuts import render
import json
import requests
# Create your views here.
def weather(request):
    if "location" in request.GET:
        city = request.GET.get('location')
        url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0f9d4ce9c441a0f7febbe97458dcb0e4"
        x = requests.get(url)
        y = x.json()
        context={
            'city_name' : f"city_name:{y['name']}",
            'Temp': f"Temperature:{y['main']['temp']}",
            'Pressure': f"Pressure:{y['main']['pressure']}",
            'Humidity': f"Humidity:{y['main']['humidity']}",
            'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
        }
        return render(request,"home.html",context)

    return render(request,"home.html")