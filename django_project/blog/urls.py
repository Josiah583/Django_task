from django.urls import path
from . import views

# this is linking to the function home we just created in views 
urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about' ),
]
