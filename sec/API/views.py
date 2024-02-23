from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    # Make a GET request to the API endpoint using requests library
    response = requests.get('https://restcountries.com/v3.1/all')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return render(request, 'index.html', {'countries_data': data})
    else:
        # If the request was not successful, return an error message
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=500)



from django.shortcuts import render
from .models import Country

def home_page(request):
    countries = Country.objects.all()
    return render(request, 'toapp/home.html', {'countries': countries})

