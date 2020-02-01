# Social-Media Application
https://hammad-blog-app.herokuapp.com

I am currently developing a full-featured web application using Django framework and Python. It is a social media styled application where different users can post e.g. blog posts, twitter updates and similar posts. It also uses HTML and CSS for the front-end.

I was inspired to do this project when I saw my friend's blog made with Wix, it had limited functionality and could easily be exploited e.g. opening the site with a private browser allowed to like the post every time.

The posts will have

* The Title

* The content

* The date posted

* The author.

There  is an authentication system, a user needs to register and then log in in order to post or see the other posts.

Each user will also have a profile , with their details such as

* Username

* Email address

* Profile picture

* Posts

The posts and the user details will be stored in a database using Django models and sqlite3.

Pagination has been implemented so that if there are a lot of posts it
doesn't slow down the website. By default five posts are shown in the front
page and then a links are given at the end of the page allowing the user to
navigate to other pages:

* First page

* Previous page

* Plus and minus three pages from the current page number

* Next page

* Last page

Reset a password feature has been implemented, an email is sent to the user with the instructions on how to reset the password associated with their account. (Having some issues with it, will be fixed soon)

# Deploying the application
Link: https://hammad-blog-app.herokuapp.com

Heroku is a platform that abstracts away a lot of the low-level system administration and allows us to easily deploy, update, and rollback changes for our application.

Uses AWS S3 to store data.

Changed to use Postgres instead of sqlite3





# Current System

Setting up an virtual environment to use it:

    sudo apt-get install python3-pip

    sudo apt-get install python3-venv

    python3 -m venv <path>/venv

    source venv/bin/activate

    //Download the dependencies

    pip install -r requirements.txt


requirements.txt:

    asgiref==3.2.3

    boto3==1.11.9

    botocore==1.14.9

    dj-database-url==0.5.0

    Django==3.0.2

    django-crispy-forms==1.8.1

    django-heroku==0.3.1

    django-storages==1.8

    docutils==0.15.2

    gunicorn==20.0.4

    jmespath==0.9.4

    mysqlclient==1.4.6

    Pillow==7.0.0

    psycopg2==2.8.4

    python-dateutil==2.8.1

    pytz==2019.3

    s3transfer==0.3.2

    six==1.12.0

    sqlparse==0.3.0

    urllib3==1.25.8

    whitenoise==5.0.1


# Further improvements

Deploying to a Linux Server using Linode

Use SSH key based authentication to login instead of passwords, by default only the password is requried in order to log in into the system. Key based authentication is more secure and more convenient because it uses keys that can't be brute force and also allows us to log in without putting in a password every single time. Get a public key and put it into the server in a file called authorised_keys.

In the configuration change the PermitRootLogin to no and the PasswordAuthentication to no.

Set up a firewall:

    sudo apt-get install ufw //ufw is uncomplicated firewall

    sudo ufw default allow outgoing

    sudo ufw default deny incoming

    sudo ufw allow ssh

    sudo ufw allow 8000 // The port being used

    sudo ufw enable

    sudo ufw status // Shows what has been enabled
