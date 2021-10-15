# Tails on Trails 

Tails on Trails is a website to provide registered users to share information on dog-friendly nature trails in Ireland.

[View the live project here.](https://tailsontrails.herokuapp.com/)

Mock up screenshot will be inserted here.

This site is created as a portfolio project for Code Institute's Software Development course.

## The purpose for this site

This site is created to share/seek the information about dog-friendly nature trails in Ireland.
There are numerous nature trails and their information widely available online however there are not as many information about the suitability of the walk with man’s best friend.
The information on dog-friendly nature trails is not easy to find at present so here I created a forum to share the information and experience of the nature walk with dogs.
This site's use is mainly intended for registered users however unregistered users can view the summary list. The reason for this is to give unregistered user a chance to preview the service before they make a decision whether or not the site is suited for their needs. 


## User Experience

### USER STORIES
=== User Stories in here ===

### STRATEGY

* Focus:
  The focus of this project is to provide a safe information sharing space for dog owners who would like to gain/share the knowledge of available dog-friendly nature trails in Ireland

* Definition:
  Tails on Trails is a forum like web site for the registered member to share the information and experience of the nature trails in Ireland

* Value:
  The registered users can make posts about their information on dog-friendly nature trails and view/comments on others posts to communicate within the registered user community

### SCOPE

**Features:**

  **Navigation menu** - The navigation menu is clear and consistent throughout the site to provide the users for easy navigation

  **Profile Page** - Registered users can share their brief information about themselves for other registered user to view

  **Post list** - Provide both registered and unregistered user to view the list of the post summaries 

  **Post detail page** -  The users who are registered and logged in can view the detailed of the post and interact by making a comment or press Like

  **Admin page** - This page is restricted to the site administrator and is used to approve the posts and comments to ensure all the posts and comments appears in the site is not inappropriate for the safe use.

 **Planned Features:**
  * The site should be responsive and user-friendly on all devices.
  * Intuitive and user-friendly navigation
  * Intuitive and user-friendly layout
  * There should be an about page to states which information is accessible for registered and unregistered users
  * The landing page should provide clear purpose of the website for any site vistors
  * Users should be able to easily register/login/logout
  * Only registered user can view the details of the posts and leave comment and press Likes
  * Unregistered users can view the post lists that only provide the summary of the posts
  * Registered users can see the location of the posts

### Structure
  1.	The site visitor will first be presented with landing page where they can read the purpose for this site. They get a choice to register first or view the forum page by pressing the button. 
  2.	In the Forum page, only registered users can display the detail page by clicking on the post title. Upon pressing the post title links in the page, unregistered users will be prompted that they have no access to those pages.
  3.	The Profile page will have image and a brief introduction on themselves and their beloved dogs.
  4.	The Review page, accessible to the user once they have purchased an item, allows them to add a review and rate a product.
  5.	(SuperUsers) Approve posts and comments
  6.	(SuperUsers) Manage users

### SKELETON
  Wireframe:
  The mockup for this site was done on Balsamiq Wireframes and can be viewed below
  Database:
  Database schema

## SURFACE
  **Colours:**
  **Typography:**
  **Effects:**

### Technologies

  * HTML5 
  * CSS3 
  * Python
  * Django 
  * Cloudinary 
  * Bootstrap 
  * FontAwesome 
  * Google Fonts
  * GitPod 
  * GitHub 
  * DevTools 
  * Heroku 




## Testing

### Automated testing

  [Link to the automated testing document](static/documentation/TESTING.md)



### Errors encountered during development

* Editing post page not displaying:
  The links to edit post page was added in the forum posts and made only visible for the post author, howoever clicking the link threw 404 error.
  Issue was caused by request user and author not matching, resulting the Http404 raised in the views.py.
  John in Tutor support in Code Institute helped me tackle this issue and suggested few ways to narrow down the cause and approaches to fix it. The successful attempt was to place resuest.user first in the if statement. Here is the problem part of the code, commentd out part shown unsuccessful attempt and final solution which I probably would never have come up by myself.
  (Post.author and request.user not matching error)[static/documentation/ss/404error_with_request_user.png]




## Setting up Django environment.

1. pip3 install django gunicorn   
   gunicorn is required to instal django in Heroku.

2. pip3 install dj_database_url psycopg2
   libraries required

3. pip3 install dj3-cloudinary-storage

4. pip3 freeze --local > requirements.txt
    Saving all requirement list to requirement.txt

5. django-admin startproject tails_on_trails .
   Creating project in current repo

6. python3 manage.py startapp forum

7. In setting.py file under the project directory(tails_on_trails), 
   add the forum app just created previous step.

8. python3 manage.py migrate
   Run server by typing below and make sure that the django message displays in opened browser window.
   python3 manage.py runserver

## Deployment

1. In the Heroku dashboard, click new then enter the app name and specipy the region.

2. In Add-on section in the resources tab, search postgres then select Heroku Postgres and submit order from button in the popup window.

3. In the setting tab, click on Reveal Config Vars button then copy the value for DATABASE_URL key.

4. Create env.py directly under the repo directory same lavel as manage.py and make sure the file name is included in .gitignore
Create DATABASE_URL with the value of Heroku config vars and SECRET_KEY generated by Django Secret Key Generator. 
Go back to Heroku Config vars and add SECRET_KEY and its value.

5. In setting.py include followings:
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
modify SECRET_KEY line to SECRET_KEY = os.environ.get('SECRET_KEY')

Replace DATABASES as
DATABASES = {

    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

6. In the terminal, migrate the change by
python3 manage.py migrate. Check the resource tab in heroku and choose 
Heroku Postgres then ensure the changes are reflected in the database

7. login to Cloudinary and copy the API Environment variable and paste in env.py and also Config Vars in Heroku.

8. DISABLE_COLLECTSTATIC set to 1 in Config Vars as the initial deployment does not contain static files yet.

9. Add Cloudinary Libraries to installed apps in setting.py.
   'cloudinary_storage', before 'django.contrib.staticfiles', and 'cloudinary' after it.

10. Set STATICFILES_DIRS, STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL and DEFAULT_FILE_STORAGE in setting.py so that Django can use the directories approproately.

11. Set TEMPLATES_DIR just below BASE_DIR and insert TEMPLATES_DIR in TEMPLATES array
'DIRS': []

12. Set ALLOWED_HOSTS array as 'tailsontrails.herokuapp.com', 'localhost'

13. Create Procfile

14. In the deployment tab in Heroku page, connect to GitHub and search for the repository then Connect.
  Click on Deploy Branch



## Credit


Django Secret Key Generator https://miniwebtool.com/django-secret-key-generator/

Solution for Login_required error  https://www.buzzphp.com/posts/login-required-decorator-gives-object-has-no-attribute-user-error

Solution for auto-generating slug field  [stack overflow](https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4)