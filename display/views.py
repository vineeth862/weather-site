from django.shortcuts import render
from django.http import JsonResponse
from .models import whole_city
import json
import requests
def weather(request):
    if 'term' in request.GET:
        cities = whole_city.objects.filter(city_names__istartswith=request.GET.get("term"))
        list1=[]
        for c in cities:
            list1.append(c.city_names)
        return JsonResponse(list1,safe=False)
    if 'location' in request.GET:
        city = request.GET.get('location')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid= your api here"
        # demonstrate how to use the 'params' parameter:
        x = requests.get(url)
        #Converts response object to dictionary
        y = x.json()
        context = {
            'c_name' : f"City_name:{y['name']}",
            'Temperature': f"Temperature: {y['main']['temp']} F",
            'Pressure': f"Pressure: {y['main']['pressure']}",
            'Humidity': f"Humidity: {y['main']['humidity']}",
            'Weather_condition': f"Weather_Condition: {y['weather'][0]['description'].upper()}"
        }

        return render(request, 'home.html', context)
    return render(request, 'home.html')
