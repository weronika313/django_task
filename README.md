# Django_task
 simple crud app to manage list of users
 
 ## Technologies used

* **[Python3](https://www.python.org/downloads/)** - A programming language
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[Django](https://www.djangoproject.com/)** –  A high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Running and installation

   * clone repository from github

    $ git clone https://github.com/weronikazochowiec/django_task
   
   * create a virtualenv
   
   * install requriments
    
    $ pip install requirements.txt
    
   * run migrations
   
    $ python manage.py migrate
    
   * run server
   
    $ python manage.py runserver
   
   
   * after those steps we should see working Django project in the browser

## App functionality 

  * displays a list of added users (with columns: BizzFuzz and Eligible)
  * ability to add, delete, edit, show details about user
  * ability to download a csv file with the list of users 



