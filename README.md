# twitterapi

Steps to run the app:
1.Pyhton3 and python3-venv should be installed

2.python3 -m venv virtualenvname

3.source virtualenvname/bin/activate

4.python3 -m pip install --upgrade pip

5.pip install -r requirements.txt

6.python3 manage.py makemigrations

7.python3 manage.py migrate

8.python3 manage.py runserver

The API is a browsable API implemented in DjangoRestFramework

# Endpoints

api/users/register/ : To register a user user

api/users/login/: To login the user

After this step login from the given username and password by clicking on the login button on the top right hand side of the screen 

api/users/list/: To list all the users

api/users/<pk>/: To retrieve details about a particular user
  
After creating multiple users we can follow other users

api/users/follow/<pk>/: To follow a user, After following the user its status posts will be visible to us



api/status/: Will list all of our status posts

api/status/create/: To post a status

api/status/<pk>/: To retrieve details about a particular status

api/status/<pk>/update/: To update details about a particular status

api/status/<pk>/destroy/: To delete a particular status
  
api/status/list_all/ : Will list all the status posts of the users whom we follow

api/status/share/<pk>/: To share a post

api/status/like/<pk>/: To like a post



api/comments/create/<pk>/: Will create a comment for the given status
