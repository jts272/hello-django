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

## Templates

1. Create `templates` dir
2. Create dir of the same name as the app we are working in e.g. `todo/`
3. Create your template HTML files in here
   - With the VS Code Django extension installed, filetype `Django HTML` should
     be recognized. Add an emmet mapping in settings if required.
4. Update render function in `views.py`
5. Update paths in `urls.py`.
   - Remember to import the corresponding function from `<app>.views`
6. Add our app dir to the list of `INSTALLED_APPS` in `settings.py`

## Migrations

Migrations = Django's way of converting Python code into database operations.
Instead of raw SQL commands for example, Django will do it for you, as long as
you provide the Python code.

When starting the Django development server, there will appear warnings of
unapplied migrations, owing to the `db.sqlite3` file created with
`startproject`, which has not been used.

### Commands to know

1. `python3 manage.py makemigrations` + `--dry-run` flag
2. `python3 manage.py showmigrations`
3. `python3 manage.py migrate` + `--plan` flag

### Logging into the database

1. `python3 manage.py create superuser`
2. Fill in appropriate credentials to create superuser
3. Quit and restart the server to see that the warning messages are gone
4. Navigate to `localhost:8000/admin` to login to Django administration
   - This admin path is provided by default in `urls.py`

## Models

Consider a model as the top row of a spreadsheet.

Use _class inheritance_ from Django's own Models class. The `models.py` of our
app created by Django imports this. We must simply supply it to the classes we
create.

In short, if functionality from one class is needed in another, inherit the
required class.

With the Item class defined, we need to actually create the table in the
database. We do this with the migration commands outlined above.

We still need to expose our model to be viewable in the admin panel. From the
app's `admin.py`, we import the class and use `admin.site.register(<Class>)`

By default, GitHub's Python .gitignore template will ensure that the resulting
`db.sqlite3` file is not tracked. This is important as the database could
contain sensitive information.

The class is now available in the admin panel. The GUI can be used to perform
CRUD functions on items in the table.

To override Django's default generic table object naming convention, we add the
following to the app's `models.py`:

```py
def __str__(self):
        str(return self.name)
```

We will now see the name we have provided instead of the generic one assigned
by Django's base Model.

## CRUD - R

1. Give access to the Item model in `views.py`
   - import, queryset var, context dict
2. Supply context dict to the render() args
3. Access the vars in the HTML file with templating syntax
