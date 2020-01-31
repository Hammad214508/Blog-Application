# Social-Media Application

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


# Current System

Setting up an virtual environment to use it:
    sudo apt-get install python3-pip
    sudo apt-get install python3-venv
    python3 -m venv <path>/venv
    source venv/bin/activate
    //Download the dependencies
    pip freeze > requirements.txt
    pip install -r requirements.txt

requirements.txt:
    asgiref==3.2.3
    Django==3.0.2
    django-crispy-forms==1.8.1
    mysqlclient==1.4.6
    Pillow==7.0.0
    pytz==2019.3
    six==1.12.0
    sqlparse==0.3.0


Set up AWS S3 (System Storage Service) so that we can host our media files from that service instead of our local filesystem.
Created a new bucket that will hold the files. Name has to be universally unique in the world.
bucket name: blog-files-hammad
Allowed Corgs permission
IAM (Identity and Access Management) and create a user.
Give it AmazonS3fullAccess
Set up AWS access key id and secret access key as environment variables so that they are not shown in the code.
Also set up a environment variable for the bucket name just in case it changes
pip intall boto3 (sudo python3 -m pip install boto3)
pip intall django-storages(sudo python3 -m pip install django-storages)

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
