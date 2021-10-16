# django-notebook
This is a simple API using Django REST Framework to create, view, update and delete text snippets.

Steps to set up the project locally:

1. Clone the Repository `https://github.com/GodsonJohn01/django-notebook.git`.
   Now, get into the repository `cd django-notebook`

2. Install and activate virtualenv: 
    `pip install virtualenv` (ignore if already installed)
    `virtualenv venv`
    `source venv/bin/activate`

3. Install the requirements using `pip install -r requirements.txt`


4. Migrate the tables to database: `python manage.py migrate`

5. Create Superuser: `python manage.py createsuperuser`

6. Now run the server `python manage.py runserver`. Congrats! API is ready by now if everything is right.

7. Install and open Postman. We will be using Postman for creating API requests.
   Postman is an API platform for building and using APIs. Go to https://www.postman.com/ to download Postman or to know more about Postman.


8. To signup, Open `Postman` and go to: http://127.0.0.1:8000/api/signup/
   Goto `Body -> row -> select type as json`
   Give the `username` and `password` in json fromat (eg: {"username": "user-new", "password": "pass@123"}) and send the `POST` request.

9. Go to: http://127.0.0.1:8000/api/login/ with the same credentials and method to login.

10. Now, Go to http://127.0.0.1:8000/api/token/ to get your access and refresh token. Resend the request to get new tokens. Note down the `tokens`.

11. Go to `Authorization -> Bearer Token` and give the `access token`.

12. Go to: http://127.0.0.1:8000/api/token/refresh/.
    Go to Body and provide key as `refresh` and value as the `refresh token` you got now.
    You can send the new request to get your new `access token` once the existing access token got expired.

13. Go to http://127.0.0.1:8000/api/snippets/create/ to create a new snippet.
    Goto `Body -> row -> select type as json`
    Give the title and content in json fromat (eg: {"title": "new-title", "content": "This is the new content!"}) and send the request.

14. Go to http://127.0.0.1:8000/api/snippets/ and choose method as `GET` to see the snippets you've created.

15. Note any id of the listed snippets (eg: 1) and go to http://127.0.0.1:8000/api/snippets/1/ (give noted id instead of 1) to view it's detail.

    Now, use the same API and change json data and the method to `PATCH` to update the content of the snippet.

    Change the method to `DELETE` and send the request to delete the Snippet.

16. Hurray! By now, you've worked with the API for a simple notebook using `Django REST Framework.`

<hr>

### Notes
Issue in running the project?

Install all the specified requirements.<br>
Please make sure you've used correct method to send the request(eg: `GET/POST/PATCH/DELETE`).<br>
Kindly follow all the instructions properly and try again. Thanks!<br>
