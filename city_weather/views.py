
from django.shortcuts import render, redirect
import requests
from .models import City


# Create your views here.
def home(request):
    if request.method=="POST":
        n=request.POST['city']
        print(n)
        City(name=n).save()

    cities=City.objects.all()

    weather_data=[]
    for city in cities:
        api_key="bd01c15dd50c18752b9bf70dd778572a"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={api_key}"
        data = requests.get(url).json()
        des = data['weather'][0]['description']
        temp = data['main']['temp']
        icon = data['weather'][0]['icon']
        context={'name':city.name,
                "description":des,
                "temperature": temp,
                "icon": icon}
        weather_data.append(context)
    x={"data":weather_data}
    return render(request,"index.html", x)

def remove(request,pk):
    r=City.objects.filter(id=pk)
    r[0].delete()
    return redirect('home')

# def city_change(request):
#     city_name=request.POST['city']
#     api_key="bd01c15dd50c18752b9bf70dd778572a"
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
#     data = requests.get(url).json()
#     des = data['weather'][0]['description']
#     temp = data['main']['temp']
#     icon = data['weather'][0]['icon']
#     context={'name':city_name,
#             "description":des,
#             "temperature": temp,
#             "icon": icon}
#     return render(request,"index.html", context)