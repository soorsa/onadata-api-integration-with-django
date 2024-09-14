import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

ONADATA_API_URL = 'https://api.ona.io/api/v1/data'

def fetch_form_data(request, form_id):
    try:
        # Construct the URL to fetch form data from the Onadata API
        api_url = f"{ONADATA_API_URL}/{form_id}"
        
        # Make a GET request to the Onadata API
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return render(request, ('onadata_app/form_data.html'), {'data':data,'form_id':form_id})
            # return JsonResponse(data, safe=False)
        elif response.status_code == 404:

            return render(request, ('onadata_app/form_data.html'), {'data':"Form Not Found",'form_id':form_id})
            # return HttpResponse("Form not found.", status=404)
        else:
            return HttpResponse("An error occurred while fetching the data.", status=response.status_code)

    except requests.exceptions.RequestException as e:
        # Handle network errors
        return render(request, ('onadata_app/form_data.html'), {'data':"Network Error: {e}",'form_id':form_id})
        # return HttpResponse(f"Network error: {e}", status=500)
