#register your models here
"""now that we have our data base set up the next thing is to allow the staff in at our imaginary video rental store
to populate the list of movies to do this we need to create an administration panel for them, howver we do not have to do this manually 
since django already comes with a powerful administration interface using the /admin in our django brower will direct us to an administration login site
which comes from the auth app in the settungs.py file of our package,


next we need to create a superuser to create a login to access the admin website, to do so we need to use the "python manage.py createsuperuser" commmand in terminal 
this will prompt you to create a usrname, an email address and a password, after that you will be able to access the website using the password created, there we can manage the 
list of users and groups
 """
from django.contrib import admin
from  .models import Genre, Movie # to be able to manage our genre and movies we need to import the Genre and Movie classes from the models module in the current folder(denoted by a "." in beginning)
class GenreAdmin(admin.ModelAdmin): #here we are created a class to be able to customize our model 
    list_display = ('id','name') # we are overriding the list_display attribute to display what we want to show

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','number_in_stock', 'daily_rate')
    exclude = ('date_created',)

# these lines are telling django  to register the models in the administration interface
admin.site.register(Genre,GenreAdmin) # now we need to pass the second argument as the class we created for the changes to register on the website
admin.site.register(Movie,MovieAdmin)


"""1. now we need to customize the admin to make it more user friendly go to the models.py module under the Classes for more notes 

 2. next we need display the list of our movies in the public area of the website """


