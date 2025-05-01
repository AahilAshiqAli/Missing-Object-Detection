from django.contrib.auth.models import User
from django.db import models

class Object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reverse_relationship')
    image_location = models.ImageField(upload_to='media')

    def __str__(self):
        return f"Object for {self.user.username}"
    
'''
TO ADD A CUSTOM USER
settings.py
AUTH_USER_MODEL = 'appname.CustomUser'

models.py
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    add custom fields here

in views.py
from django.contrib.auth import get_user_model
User = get_user_model()
This will return the custom user model specified in the AUTH_USER_MODEL setting, allowing you to work with the custom user model in your Django project.


objects is many to one relationship, like if I make a table of Objects and make a relationship of Many to One with User so, automatically django makes a descriptor that reverses the realtionship to extract data in reverse way like through User class I would get all Objects



You always have to register your model in admin
TO add a model in database, dont do 
python manage.py makemigrations
but
python manage.py makemigrations tablename

These are class attributes. In python OOP, there are two kinds of attributes. One is class attributes, which are shared by all instances of class
and if one instance makes a chnage, that change is reflected in all instances. These are written outside of constructor in class
Other are instance attributes, which are seperate for each instance and so are defined and initialized inside the constructor


In django, class attributes are used to define field names in a database.

But, logically, each element in database has unique value then why class attributes?

The answer to it is that it is only used to define schema. Things are actually not stored in it.
'''