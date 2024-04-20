from django import forms
from .models import Object

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['user', 'image_location']
        
        
"""
Why do we use Model forms class when using a Model with db and what is this syntax.  

A model form is a subclass of Django’s Form class that automatically matches the attributes of  
a given database table to create input elements.
Text based input elements are saved in request.POST and to retrive in views we normally do model.attribute = request.POST[attribute] where 
attribute inside POSt is what we save in names label in html file for that input in form. When making model forms we need to ensure 
that those name attributes match with attributes of django model so it will automatically assign them without any need of assigning each.

About FileField (Image field is a subclass of filefiled) it by itself manages uploading files in a particular folder and you dont have to do this logic.
Else if you are saving path in model as CharField or not using model then you have to do this for file upload
def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
            
I have used usernames stored in default username tables of django as foreign key for Object model.
When migrating, there were problems so I deleted my migrations folders and dbsqlite and then again did migrations command.
"""