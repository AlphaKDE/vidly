from django.http import HttpResponse

from django.shortcuts import render # we use this function  render a function 
from .models import Movie 

#here is where we define our view function, a view function takes a request and returns a response, which could be anything you want to show on your website 
# Create your views here.
def index(request): # this function represents the main page of an app 
    movies = Movie.objects.all() # here we are getting the movie object in our database, from the Movie class we created in the models module in our file
    

# it takes an http request object as a parameter(it can be any name) and django will take care of calling the function 
    return render(request,'movies/index.html', {'movies': movies}) #every view function should return an http response, we than call make an Http response object using the HttpResponse Class

"""now we need to map our function to a url, we need to add a new files in the movies directory called "urls.py" 
.....refer to the urls.py module in the movies directory for more notes/explanation"""
