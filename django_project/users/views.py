from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.

# these function is responsible for creating our form in our register.html page that is under "users" app
def register(request):

        # these means that if we a get a POST request it should 
        # instatiate a user creation form with that form data most likely from our form else we will just create a blank form
         #when we submit our form it comes in as post request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # the second if statement is responsible for validation
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})

# a decorator add fuctionality to an existing function
# an in these case it add functionality to our profile view where a user must login to view the profile

@login_required
def profile(request):
    return render(request, 'users/profile.html')




#message.debug
#message.info
#message.success
#message.warning
#message.error



