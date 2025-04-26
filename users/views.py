import os
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from django.contrib import messages
from admins.models import RealEstateData
def userAddedValues(request):
    if request.method == 'POST':

        # Extract data from the POST request
        posted_by = request.POST.get('posted_by')
        under_construction = int(request.POST.get('under_construction'))
        rera = float(request.POST.get('rera'))
        bhk_no = int(request.POST.get('bhk_no'))
        bhk_or = request.POST.get('bhk_or')
        square_ft = float(request.POST.get('square_ft'))
        ready_to_move = int(request.POST.get('ready_to_move'))
        resale = int(request.POST.get('resale'))
        address = request.POST.get('address')
        longitude = float(request.POST.get('longitude'))
        latitude = float(request.POST.get('latitude'))
        target_price = float(request.POST.get('target_price'))
        try:
        # Create a DataFrame

            uva = RealEstateData(
                posted_by=posted_by,
                under_construction=under_construction,
                rera=rera,
                bhk_no=bhk_no,
                bhk_or=bhk_or,
                square_ft=square_ft,
                ready_to_move=ready_to_move,
                resale=resale,
                address=address,
                longitude=longitude,
                latitude=latitude,
                target_price=target_price,
                is_approved=False  # Default value
            )

            if uva.full_clean:
                uva.save()  # Saves the object in the database
                messages.success(request,'Values Added once admin approves')
                return render(request,'users/userValues.html')
            else:
                messages.success(request,'Values not added properly please try again')
                return render(request,'users/userValues.html')

        except Exception as E:
            messages.success(request,f'{E}')
            return render(request,'users/userValues.html')


    return render(request,'users/userValues.html')

def UserBasePage(request):
    user = request.session['username']
    print(user)
    return render(request,'users/userbase.html',{'user':user})

def userhome(request):
    return render(request,'users/userbase.html')


from .utility.classification import execute_real_estate_prediction

def model_values(request):
    results=execute_real_estate_prediction()
    return render(request,'users/model_values.html',results)

from django.shortcuts import render
from .utility.classification import predict_price

def prediction_view(request):
    if request.method == 'POST':  
        try:
            # Extract form data from POST request
            rera = float(request.POST.get('rera'))
            bhk_no = int(request.POST.get('bhk_no'))
            square_ft = float(request.POST.get('square_ft'))
            ready_to_move = int(request.POST.get('ready_to_move'))
            resale = int(request.POST.get('resale'))
            longitude = float(request.POST.get('longitude'))
            latitude = float(request.POST.get('latitude'))
            model_type = int(request.POST.get('tbModel'))  # Model selection

            # Call the prediction function
            predicted_price = predict_price(rera, bhk_no, square_ft, ready_to_move, resale, longitude, latitude, model_type)

            # Render output.html with predicted price
            return render(request, 'users/output.html', {'predicted_price': round(predicted_price, 2)})
        
        except Exception as e:
            print(f"Error: {e}")
            return render(request, 'users/output.html', {'predicted_price': None})

    return render(request, 'users/prediction.html')  # Redirect to form if no POST request
