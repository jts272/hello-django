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

### Using conditionals

The templating syntax is like Jinja2, in that `{{}}` represents data and `{%%}`
represents logic.

The general flow is to start a loop, then use conditionals to display data from
the db. For example, if an item has an `is_done` property, display the item name
within a `<strike>` tag.

Furthermore, the self-closing `{% empty %}` block can be used to render HTML in
the instance that the model has no entries.

## CRUD - C

1. Create new HTML page - copy and rename the single page from the templates dir
2. Add a link in the homepage with an href of `/add/`
3. Create the view in `views.py`
4. Include a path for `'add/'`, supplying the function and name properties
   - Remember to import the function
5. In our new page to add items, we create a form. Be deliberate in naming the
   `name` and `id` attributes. Apply labels
6. Set form `method="POST"` and `action="/add/"`
7. Apply Django `{% csrf_token %}` (cross site request forgery)
8. In `views.py` we create an `if` block on `POST`
   - Get the form values and create a class instance with them
9. Import `redirect` and apply to the return of the `POST` block
   - We redirect to the function, which renders the appropriate HTML page. The
     path in `urls.py` determines the actual browser url we go to

Of special note is the syntax used for url paths. For example, in the form
action, we want to submit the form to the current page. We need to use a
preceding `/` to identify that we want to use the current page and not create a
new one.

## Django forms

Allow Django to handle and validate the form directly.

1. Create `forms.py` in app root dir
2. Imports:

   ```py
     from django import forms
     from .models import Item
   ```

3. Setup the form class with inheritance
4. Nest the `Meta` class and provide `model` and `fields`
5. Import the `ItemForm` class into `views.py`
6. Create an instance of the form and create `context` var. Pass this into the
   return render
7. Now we can display this form with a simple `{{ form }}` block
   - We can alter the rendering method by appending `as_p`
8. In the `POST` block, we need to now let Django validate the form:

   ```py
   # DJANGO POST HANDLER
           form = ItemForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('get_todo_list')
   ```
