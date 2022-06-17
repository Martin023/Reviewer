# Reviewer
A peer review website.

# Description  
This project allows users to post their projects for other users to rate according to design, usability and content 
##  Live Link  
 Click [View Site](https://awwwardz.herokuapp.com/)  to visit the site
  

## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.  
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://awwwardz.herokuapp.com/
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Revviewer pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv env - source env/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip3 install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host in a environment variable file, then make migrate  
 ```bash 
python manage.py makemigrations awards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  

 
 
## Technology used  
  
* [Python3.10](https://www.python.org/)  
* [Django 4.0](https://docs.djangoproject.com/en/)  
* [Heroku](https://heroku.com) 
*  
## To do's
Incorporate a django-rest api for accessing the different items in the application

## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please contact me through my socials or my website as pinned above.  
  


# LICENCE
[MIT]([Python3](https://www.python.org/)  ) 

# &COPY;Revviewer 2022


