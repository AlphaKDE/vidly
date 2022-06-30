"""in this file we are going to a variable called "urlpatterns"(exactly as is) which we will set to a list, 
in this list we will add objects that map url endpoints or view functions """



from django.urls import path # to map url endpoints we use the path function from django.urls and to crate a path object
from . import views # we than import the index function we made earlier, we cannot regularly do " import views" we need to use a relative import statement

app_name = 'movie'
##this is called a url configuration, all apps should have a url configuratio
urlpatterns = [
path('', views.index, name= 'index'),# as a first argument we need to specify our url endpoints, here we specify an empty string to represent the root of the app,as a second arguement we pass it a reference to the view function
#and for the third argurment we use a keyword to name the url endpoint
path('<int:movie_id>', views.detail, name= 'detail')
]

#for instance in our movies app we will have:
#movies/ as the root 
#movies/1/details  which represents another page of our app

"""we are now done configuring the url for this app however our main app vidly has no knowledge of the movies app.. under the vidly directory
go to the "urls.py" module for continuation of the notes """