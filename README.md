# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![Diagram](https://github.com/GOWTHAM54577/ORM/assets/144589420/d35a116a-38ed-4062-8d34-5374b78e6049)
## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
-Models
```
from django.db import models
from django.contrib import admin
class Books_DB(models.Model):
    serial=models.IntegerField(primary_key=True);
    title=models.CharField(max_length=20);
    author=models.CharField(max_length=20);
    price=models.IntegerField( );
    genre=models.CharField(max_length=20);
class Books_DBAdmin(admin.ModelAdmin):
    list_display=("serial","title","author","price","genre");
```
-Admin
```
from django.contrib import admin
from .models import Books_DB,Books_DBAdmin 
admin.site.register(Books_DB,Books_DBAdmin)
```

## OUTPUT
![output](https://github.com/GOWTHAM54577/ORM/assets/144589420/762d85e1-dd91-43ae-83cc-0b5e388cfcc1)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
