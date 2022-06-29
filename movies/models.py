"""the next step is to create the models for the movies app, these models are python classes we use 
to represent our application data"""


from django.db import models # this django mpackage encapsulates all the functionality around working with data bases, from the django package we have a module called models 
from django.utils import timezone

class Genre(models.Model): # we are creating a class called genre, which will inherit all the functionality of the Model class in the models module,
    name = models. CharField(max_length=255) # we are now creating a class attribute and set it to a field class in a data base, we are setting it to a Character field and passing the keyword arg max_length to give it a max character
    
    def __str__(self): # we are overidding the magic method str to show the name of our genre
        return self.name    # we want to customize how our genre object is shown on the administrationn website so we can represent it as a string,(although it shows up as an error, the server will run correctly)
    """now we need to go to the admin.py module for continued notes """



class Movie(models.Model):# we are creating a second class for the Movies inside the models module, we also need to derive it from the models.Model class since we will work with a db
    # a movie has to have a title a release_year etc...


    title = models.CharField(max_length= 255) # we are also using the field class Char field since our field in the db will have a character


    release_year = models.IntegerField() # we are using the Interger Field class because the release_year field in the data base is an integer

    number_in_stock = models.IntegerField() # we are using the Interger Field class because the release_year field in the data base is an integer
    
    daily_rate = models.FloatField() # we are using the FloatField class here so we can store the daily rate as $4.56 etc...

    """each movie needs to be associated with a genre, to do this we need to create a relationship between the Movies class and Genre class"""

    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    #using the models.ForeignKey Class we will make this relationship,its first argument is the Genre class for the relationship,
    #for the second argument we use the on_delete = keyword, the on_delete keyword tells django what should happen when a genre is deleted,if the "comedy" genre is deleted, all the movies 
    # with that genre should also be deleted, therefore we pass it the CASCADE functions as the keyword.

    date_created = models.DateTimeField(default=timezone.now) # this adds a new attrubute to the movies class which displays the day a fueld was created

    """we can always come back to this step to add a new class or modify our old classes, The next step is to
    tell django to synchronize our database with the models we have in our movies app... go over to DB browser for SQLite and open the sqlite3 file that is in our project Vidly,
    django automatically conifgures the tables in a database for us based on our models, django supports all the data base engines such as mySQL, microsoft SQL server etc...""" 


    """Migrations in Django:
      Everytime we create or modify new model classes, we tell django to compare our model classes with the database
      it will look at our models and the database and check to see what is missing and to pass on the whats missing, it will create a migration. 
      a migration is basically a python file that includes code, when we run that code it will synchronize all our model classes with the data base


      to run the migration we will have to run the migration module via the terminal by; python manage.py makemigrations, but first we will have to register our movies app with django
    ...to do so we will need to go to the settings files inside the vidly directory... note continues inside the setting module...
    

    API - application programming interface

    Data Abstraction API: a data abstraction api unifies communication between a computer application and databases such as SQL server, mySQL etc..
    for example take a look at our Movies class above, we are inheriting the Model class inside the models.py module(models.Model) this Model class is a data abstraction API in django 
    that automatically takes care of writing the commands needed in an SQL data base, it takes care of deleting, adding, Modifying etc
    
    """

  
