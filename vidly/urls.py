"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include # we also import the include function to be able to recieve the url config we made in the movies app
from api.models import MovieResource
from . import views 

movie_resource = MovieResource() # we need to create an instance of the MovieResource class to be able to include it in our api

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls), # every django app has an administrative panel which is a path that maps anything that starts with admit to admin.site.urls
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls)) # here we are creating another pass where we tell django any urls that start with api should be handed off to another app
    
    
#we than add a new path object, that tells our vidly app that any path that starts with movies(first arg) should be handed off to the url configaration in the movies app(second arg) 
#we dont add "movies.py" inside the inlcude function because django automatically append the extension and load the module,
#whenever we send a request that starts with "movies" django will chop off the prefex(movies/) and send the remaining string to the "movies.urls" module, which is why we use an empty string to represent the root of the app

]

"""now on the terminal we can run the server using "python" manage.py runserver,
initially when we run our server we will get a page not found error but if we use /movies and enter we will see our message "Hello World" 
which means we have sucessfully mapped a url endpoint to a view function"""