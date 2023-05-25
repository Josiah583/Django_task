from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')

    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})



#message.debug
#message.info
#message.success
#message.warning
#message.error



