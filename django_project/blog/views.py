from django.shortcuts import render
from .models import Post  # the dot simple means from the model class in the curret package or directory import our current class 

# Create your views here.

# function to handle traffic from the home page for our blog and will handle a request argument
# logic to handle certain routes
# these function handles the home page

def home(request):
    context = {
        'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context)


# the function bellow handles the about page
def about(request):
    return render(request, 'blog/about.html')