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
