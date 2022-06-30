"""We are creating an API so other websites or mobile apps can get the list of our movies in Json format that is pure data

we first need to start with installing the django framework django-tastypie by pipenv install django-tastypie

afterwards we need to create an api app in our project by the command "python manage.py startapp api" 

we than need to make sure to add the api app to our installed apps in the settings module... for to the settings.py module for further notes 
"""

from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie 

class MovieResource(ModelResource): # Here we are creating a movie resources, it is used to represent all the data that we have for our movies, we than inherit the class ModelResource from the tastypie framework

    class Meta: #within ModelResource we have another class called Meta
        queryset = Movie.objects.all() # here we are setting the query to get the list of all our movies, to do so we need to import out Movie class in our movies app under models
        resource_name = 'movies'
        excludes = ['date_created'] # this variable is used when we dont want a certain data to be on the json file
       
"""in the world of API we refer to our models as resources , it defines our applications can talk to each other over http protocol
we do this by the URLs(uniform resource locator), 
"""