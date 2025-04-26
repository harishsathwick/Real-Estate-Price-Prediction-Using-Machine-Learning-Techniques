import os
from django.shortcuts import get_object_or_404, render, redirect
from . models import RealEstateData, UserRegisterTable
from django.conf import settings
from django.contrib import messages
# ---------------------------------------------------------------------------------
def AdminBasePage(request):
    return render(request,'base/main.html')
#-----------------------------------------------------------------------------------

def UserLoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserRegisterTable.objects.get(username=username, password=password)
            if user.is_active:
               request.session['username'] = user.username
               request.session['email'] = user.email
               request.session['address'] = user.address
               user = request.session['username']
               return render(request, 'users/userbase.html',{'user':user})
            else:
                messages.error(request, 'Your Account is not Activated, Please Activate and Try again.')
        except UserRegisterTable.DoesNotExist:
            messages.error(request, 'Invalid username or password.') 

    return render(request, 'admins/userlogin.html')
#------------------------------------------------------------------------------------

def AdminLoginPage(request):
    if request.method == 'POST':
       usrid = request.POST.get('username')
       pswd = request.POST.get('password')
       print("User ID is = ", usrid)
       if usrid == 'admin' and pswd == 'admin':
           return render(request, 'admins/adminbase.html')
       else:
           messages.error(request, 'Please Check Your Login Details')
    return render(request, 'admins/adminlogin.html')

#------------------------------------------------------------------------------------
def UserRegisterPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']

        if UserRegisterTable.objects.filter(username=username).exists():
            messages.error(request,'Username already exists')
            return render(request, 'admins/register.html')
        if UserRegisterTable.objects.filter(email=email).exists():
            messages.error(request,'Email already exists')
            return render(request, 'admins/register.html') 
        user = UserRegisterTable.objects.create(
            username=username,
            email=email,
            phone=phone,
            password=password,  
            address=address,
        )
        user.save()
        print('data saved ...........................')
        return render(request, 'admins/register.html')

    return render(request, 'admins/register.html')

#----------------------------------------------------------------------------------------------------------------

def UsersViewPage(request):
    users = UserRegisterTable.objects.all()
    return render(request, 'admins/userlist.html', {'users':users})

#----------------------------------------------------------------------------------------------------------------

def ActivateUser(request):
    if request.method == 'GET' and 'id' in request.GET:
        uid = request.GET.get('id')
        print(uid)  # Optional: Print for debugging purposes
        try:
            UserRegisterTable.objects.filter(id=uid).update(is_active=True)
            users = UserRegisterTable.objects.all()
        except Exception as e:
            print(e)    
    return render(request, 'admins/userlist.html', {'users': users})
#----------------------------------------------------------------------------------------------------------------
def DeactivateUser(request):
    if request.method == 'GET' and 'id' in request.GET:
        uid = request.GET.get('id')
        print(uid)  # Optional: Print for debugging purposes
        try:
            UserRegisterTable.objects.filter(id=uid).update(is_active=False)
            users = UserRegisterTable.objects.all()
        except Exception as e:
            print(e)    
    return render(request, 'admins/userlist.html', {'users': users})

#--------------------------------------------------------------------------------------------------------------------

def adminhome(request):
    return render(request, 'admins/adminbase.html')

#------------------------------------------------------------------------------------------------------------

def home(request):
    return render(request, 'base/main.html')


def userAddedValuesApprovel(request):
    properties = RealEstateData.objects.all()
    return render(request, 'admins/userValuesApproves.html', {'properties': properties})


import pandas as pd
def approve_property(request):
    id=request.GET['property_id']
    print(id)
    property_obj = RealEstateData.objects.get(id=id)
    print(property_obj.address)
    # Define the CSV file path
    file_path = os.path.abspath('media/train.csv')
    print("File Path:", file_path)

    # Convert the approved property to a dictionary
    property_data_2d = [[
    property_obj.posted_by,
    property_obj.under_construction,
    property_obj.rera,
    property_obj.bhk_no,
    property_obj.bhk_or,
    property_obj.square_ft,
    property_obj.ready_to_move,
    property_obj.resale,
    property_obj.address,
    property_obj.longitude,
    property_obj.latitude,
    property_obj.target_price
        ]]


    # Convert to DataFrame
    df = pd.DataFrame(property_data_2d)
    print(df)
    try:
        # Append to CSV
        df.to_csv(file_path, mode='a', header=False , index=False)
        property_obj.delete()
        messages.success(request, "Property approved and added to dataset successfully!")
        properties = RealEstateData.objects.all()
        return render(request, 'admins/userValuesApproves.html', {'properties': properties})
    except PermissionError:
        messages.error(request, "Permission denied: Cannot write to train.csv. Check file permissions.")
        properties = RealEstateData.objects.all()
        return render(request, 'admins/userValuesApproves.html', {'properties': properties})

    # Delete the approved property from the database
   



def delete_property(request):
    id=request.GET['property_id']
    prt=RealEstateData.objects.get(id=id)
    prt.delete()
    properties = RealEstateData.objects.all()
    return render(request, 'admins/userValuesApproves.html', {'properties': properties})

