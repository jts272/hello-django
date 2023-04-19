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

## CRUD - U

1. Create an Edit button that points to the url we will create,
   `/edit/{{ item.id }}`. Django creates the appended `id`
2. Create the new view `edit_item()`, providing `request` and `item_id`
3. Render return the `todo/edit_item.html` we will create
4. The edit page is based of the add page, which incorporates the `{{ form }}`.
   By removing the form action, it POSTs to the current page
5. Add the path as `edit/<item_id>/`, calling the `edit_item` view. Add `name`
6. Create the form in the view with the Django shortcut `get_object_or_404`
7. Add the post handler to update the db

## CRUD - D

1. Get the var with the `get_object_or_404`, supplying the class and id
2. Call `delete()` on this var
3. Return redirect

For further specifics on Updating and Deleting in this application, see:
<https://docs.google.com/document/d/1RNDHMuQEBJ8if9XYR1WLjNJx_Z4Nad-NarjRVFrC0gQ/edit>

## Django testing

Django apps create a `tests.py` file, which can be duplicated and appended with
an appropriate name for the group of things being tested, e.g. `test_views.py`

We create a test class, which inherits `TestCase` from the default import. From
here, we define functions with the standard `self.assert<Whatever>()` syntax.

Classes that are being tested must also be imported, as shown in `test_forms.py`

Run a specific test file with `python3 manage.py test <app>.tests_<module>`

This can be further appended with the test class, then even further with the
test function. This is done simply with dot notation.

When testing for url paths, do not forget to include the trailing '`/`'

## Coverage

Coverage is used to show _how much_ of our code has been tested - not how much
is passing.

1. `pip3 install coverage`
2. Run with `coverage run --source=todo manage.py test`
3. View the report with `coverage report`
4. Create an interactive HTML report with `coverage html`
   - This creates the `htmlcov` dir
5. View the HTML with `python3 -m http.server`
   - This will not work whilst the Django server is running - use one or the
     other
6. Create tests for the missing items highlighted in red
7. Re-run coverage and the HTML report command

## Deployment

### Heroku CLI install

For WSL2:

```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Logging in

The following command assumes MFA is enabled on the account. This login method
is required for API calls.

1. `heroku login -i`
2. Enter email address
3. Enter the password - this is the API key found in 'Account settings' on the
   web

### Installing project requirements

Heroku uses an ephemeral file system. It is wiped clean every time Heroku
updates, or we redeploy our app. The SQLite db we have been using in development
is file-based, which makes it unsuitable for production deployment.

We will use a Heroku addon, which allows us to use Postgres that will be
separate from our application. It will survive even if the app server is
destroyed.

Here are the following steps to use Postgres in our app:

1. `pip3 install psycopg2-binary`
   - We will install the Heroku addon later. This takes care of the Django side
2. `pip3 install gunicorn`
   - This replaces our development server once the app is deployed to Heroku
3. `pip3 freeze --local > requirements.txt`
   - This tells Heroku the packages to install for our app

### Creating a Heroku app

1. `heroku apps:create jts272-hello-django`
   - App will default to US region. Optionally append `--region eu`
2. `heroku apps`
   - Display our created apps in Heroku
3. If a git repo has not been setup, Heroku automatically sets one up for us. By
   entering `git remote -v` we should see:

   ```bash
   heroku  https://git.heroku.com/jts272-hello-django.git (fetch)
   heroku  https://git.heroku.com/jts272-hello-django.git (push)
   origin  https://github.com/jts272/hello-django.git (fetch)
   origin  https://github.com/jts272/hello-django.git (push)
   ```

- `git push heroku main` would push the main branch to the heroku remote
- `git push origin main` would push the main branch to the git remote

### Creating a database

1. Login to ElephantSQL
2. Create new instance, providing an app name, e.g. `jts272-hello-django`
3. Select region and data center
4. Review and create instance
5. Select the app's database URL from the dashboard and copy

### Connecting the external database to our app

1. In the Heroku app dashboard, go to settings and reveal config vars. Add the
   following:

   ```bash
   "DATABASE_URL": "postgres://<YOUR_DB_URL_PASSWORD_FROM_ELEPHANTSQL>"
   ```

### Connecting the external database to our IDE

1. Create an `env.py` file in the root of the project if it does not exist.
   _Immediately_ add this to `.gitignore`
2. Add the following code:

   ```py
   os.environ.setdefault("DATABASE_URL", "my_copied_database_url")
   ```

3. `pip3 install dj_database_url==0.5.0`
4. Update your `requirements.txt`
   - Just run the `freeze` command again, as before
5. In the root Django dir, add the following imports to `settings.py`:

   - The first line should already be generated by Django

   ```py
   from pathlib import Path
   import os
   import dj_database_url
   import env
   ```

6. Further down in the file, we can replace the default `DATABASES` var with the
   following:

```py
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

7. Run the `python3 manage.py migrate` command
   - This transfers the database _structure_ but not the data content
8. Run the Django server to conclude the database setup!

   - In instances where ports are already running, execute this command, found
     [here:](https://stackoverflow.com/questions/20239232/django-server-error-port-is-already-in-use)

   ```bash
   sudo fuser -k 8000/tcp
   ```

### Attempting first deployment

1. Commit and push all code to GitHub/origin. Ensure your `env.py` file and
   imports are in order before pushing
2. `git push heroku main`
   - If your `requirements.txt` contains `pkg_resources==0.0.0`, remove it. See
     https://stackoverflow.com/questions/39577984/what-is-pkg-resources-0-0-0-in-output-of-pip-freeze-command
3. We will see the push command fail. Heroku is looking for static files, but we
   have not used any in this application. The error messages provide us with the
   following code to input:

   ```bash
   heroku config:set DISABLE_COLLECTSTATIC=1
   ```

4. Run the above code snippet and push again
5. A URL should be provided once the application builds. However, it will
   exhibit an application error. Check the logs with `heroku logs --tail`
   - We will find error `code=H14 desc="No web processes running"`. In other
     words, we haven't told Heroku that this is a web application that needs a web server running - this is why we installed `gunicorn`
   - These Heroku error codes are useful in diagnosing deployment problems
6. Create the `Procfile` in the root dir
7. Push to git and Heroku. Now when we view the application at the deployed
   url, we will see a Django error regarding `ALLOWED_HOSTS`

### Fixing allowed hosts

Django needs a list of allowed hosts to ensure the security of HTTP requests.
Any requests from a host not in the `ALLOWED_HOSTS` lists will be blocked by
default.

1. In `settings.py`, add the deployed URL as a string to the `ALLOWED_HOSTS` var
   - By default, this should be an empty list.
   - Remove the preceding `https://` from the URL
