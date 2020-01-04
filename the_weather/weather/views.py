import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2dd09e0ccee69bd91e03c3f87f423a6c'
    city = 'Osaka'
    r = requests.get(url.format(city)).json()


    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']

    }
    context = {'city_weather': city_weather}
    print(city_weather)
    return render(request, 'weather/weather.htm',context)
