from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:            
             # Check USer
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email being used ')
                    return redirect('register')
                else: 
                    # good and Create new user
                    user = User.objects.create_user(username=username,password=password,email=email,
                    first_name=first_name,last_name=last_name)
                    # log in after registration
                    # auth.login(reuest, user)
                    # messages.SUCCESS(request, 'You have now looged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = auth.authentication(username=username,password=password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            # messages.SUCCESS(request, 'You have successfully logged in')
            messages.success(request, 'You are now registered and can log in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid User')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)
