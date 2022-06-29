from django.http import HttpResponse, Http404

from django.shortcuts import render,get_object_or_404 # we use this function  render a function 
from .models import Movie 

#here is where we define our view function, a view function takes a request and returns a response, which could be anything you want to show on your website 
# Create your views here.
def index(request): # this function represents the main page of an app 
    movies = Movie.objects.all()
    return render(request,'movies/index.html', {'movies': movies}) #every view function should return an http response, we than call make an Http response object using the HttpResponse Class
 # here we are getting the movie object in our database, from the Movie class we created in the models module in our file
# it takes an http request object as a parameter(it can be any name) and django will take care of calling the function 
    
def detail(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id) # the get_object_or_404 is used like a try block, if the user enters an invalid id it will prompt http error 404
    return render(request,'movies/detail.html',{'movie': movie}) #here we are rendering the html to the server and passing it the Movie model so it knows to take information from the database
   

  

"""now we need to map our function to a url, we need to add a new files in the movies directory called "urls.py" 
.....refer to the urls.py module in the movies directory for more notes/explanation"""
