# APP NAME
    Instagram clone
## AUTHOR
    Iyerikuzwe Regine

## DESCRIPTION
    This is an application more or less like the popular social media platform Instagram where users can sign up, post pictures view pictures posted by others comment on them as well as like or dislike the pictures

## User stories
    As a user can do the following:

    Sign in to the application to start using
    Upload pictures to the application.
    View their profiles containing all their pictures
    A user can Follow other users and see their the users timeline.
    Like a picture and leave a comment on it.
## Set Up and Installation
    Prerequisites
    Python 3.6.2
    Virtual environment
    Postgres Database
    Reliable Internet Connection
## Installation Process
    Copy repolink
    in your terminal run the following commands

    $ git clone REPO-URL in your terminal
    $ cd Ikuzweinsta1_clone
    $ python3.6 -m venv virtual
    $ touch .env ( to the file add : SECRET_KEY= DEBUG=True)
    $ source virtual/bin/activate
    $ python3.6 -m pip install -r requirements.txt
    $ psql ; CREATE DATABASE insta ;
    In the settings.py module of the project make the following changes

    DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'instagram', 'USER': POSTGRES_USERNAME, 'PASSWORD': POSTGRES_USERNAME, } }

    $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
## Known Bugs
    No known bugs
## CREDITS
    Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used
    This project uses major technologies which are :

    HTML5/CSS
    Bootstrap
    Python3.6
    Django FrameWork
    Postgress Database
## Support and Contacts
    In case You have any issues using this code please do no hesitate to get in touch with me through iyerikuzweregine19@gmail.com or leave a commit here on github.
    or 0789329012
 ## Contributing
    When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

    Please note we have a code of conduct, please follow it in all your interactions with the project.
## Link to github.
    https://github.com/iyerikuzwe/Ikuzweinsta1

## Deployment
    Before you can host a website externally you're first going to have to:
        1.Make a few changes to your project settings.
        2.Choose an environment for hosting the Django app.
        3.Choose an environment for hosting any static files.
        4.Set up a production-level infrastructure for serving your website. 
## License
    Copyright (c) 2019 Regine Iyerikuzwe

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
## Acknowledgement
    1. I would like to express my deepest appreciation to moringa school who provided me the possibility to complete this project.
    2.  A special gratitude I give to my mentors,  whose contribution in stimulating suggestions and encouragement,  helped me to coordinate my project.

    3. Furthermore I would also like to acknowledge with much appreciation the crucial role of my classmates who  help me to assemble the codes and gave suggestion about the task.
    4.  Last but not least, many thanks go to the mentor of the project, [Mr Saphani,Mr Aristote] whose have invested his full effort in guiding our team in achieving the goal.
    5. I have to appreciate the guidance given by other facilitators that has improved our projects skills,thanks to their comments and advices.   