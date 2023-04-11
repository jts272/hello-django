# hello-django

A repository to learn the Full Stack Framework Django in a local development
environment.

This repository was created with GitHub's Python `.gitignore` template.

## Environment settings

1. VS Code Running in Ubuntu 20.04 (WSL2)
2. Python `.venv` environment
3. `pip3 install 'django<4'`
4. `django-admin startproject django_todo .`
5. `python3 manage.py runserver`

Your app should now be running at `localhost:8000`

## URLs

Django projects are organized into apps. These are self-contained collections of
code that can be re-used. For example, instead of coding an authentication
system, install a Django app with this functionality already designed.

1. `python3 manage.py startapp todo` - creates 'todo' app folder
2. Define a function in `views.py` of the new app folder
3. In `urls.py` in the project root, import the function and add the `path` to
   the `urlpatterns` list.
4. With the Django server running, navigate to `localhost:8000/<your_url>` to
   view the page.
