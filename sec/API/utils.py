from django.shortcuts import render
from django.http import JsonResponse
import requests

def my_view(request):
    # Make a GET request to the API endpoint using requests library
    response = requests.get('https://restcountries.com/v3.1/all')
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return render(request, 'index.html', {'data': data})
    else:
        # If the request was not successful, return an error message
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=500)
