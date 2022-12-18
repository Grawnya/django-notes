# Django Notes

#### Frameworks
* A framework is a reusable "semi-complete" application that can be specialised to produce custom apps - don't need to worry about the plumbing at the lower level.

#### Model View Controller (MVC)
* A common programming paradigm or pattern.
* A way of working with data in its 3 different manifestations: 
    - at rest (model)
    - in motion (controller)
    - as presented (view)

#### Django
* Django is a full framework i.e. It comes with many preinstalled components and lots of low level automation, but it can be less flexible than a micro framework.
* A project within Django is a container for your site. Its a collection of apps which are self-contained pieces of functionality.
* Django's use of MVC architecture is slightly different as views can also act as controllers.
* Model View Template (MVT) is used, where the view is the controller in the MVC and the template is the user interface.
* It takes Python classes known as models and automatically creates db tables and their relationships.
* Templates are the presentation layer which define how info is displayed to the end user.
* Jinja can also be used as a template language.

#### Getting Set Up
* Download the stable Django 3.2 version, use `pip3 install 'django<4'`.
* The change to the suitable directory based on the Python you are using: `$ cd /workspace/.pip-modules/lib/python3.8/site-packages/`
* To check if successfully downloaded, `ls -la` should provide a list of downloaded libraries, including Django, but go back to the original directory using `cd -`, as changing anything in the site packages could corrupt them or the Python download.
* To start the project, type into the terminal `django-admin startproject project_name .` wher the full stop signifies that the project should be created in the current directory.
* This creates `manage.py`, which is management utility required throughout the project and a project directory of the name provided is created.
* 4 files are created within the project directory:
    - `__init__.py` - to tell our project that this is a directory we can import from.
    - `settings.py` - contains the global settings for our entire Django project.
    - `urls.py` - contains routing info.
    - `wsgi.py` - allows our web server to communicate with our Python application.
* Make sure secret key in `settings.py` is saved in `env.py` file in the form:
\
&nbsp;
`os.environ[SECRET_KEY] = insert secret key`
\
&nbsp;
and in the setting file:
\
&nbsp;
`SECRET_KEY = os.getenv("SECRET_KEY")`

* To run the project: `python3 manage.py runserver`

#### Creating an App:
* Type `python3 manage.py startapp app_name` in the terminal to create an app.
* Note the `urls.py` website can be used to activate functions in `views.py` within the project folder and requires the built-in `path` function, which takes 3 arguments:
    - the url that the user is going to type in (make sure to add this to end of the default url when running the project to see the app)
    - the view function that it's going to return
    - a name parameter

#### Templating:
* When creating a templates folder within the app folder, create another folder within it with the same name as the app. The reason that we're creating this secondary folder inside the templates directory is because when Django looks for templates inside of these apps it will always return the first one that it finds. So by separating it into a folder that matches its app name. We can ensure that we're getting the right template even if there's another template of the same name in a different app.
* After updating the `views.py`and `urls.py` files with suitable templates, add the app name to the `INSTALLED_APPS` list within `settings.py` to make sure it can run.

#### Migrations and Admins:
* Migrations are Django's way of converting Python code into database operations.
* `python3 manage.py makemigrations --dry-run` - Note: the dry run flag is used to run a command to see how the programme would run. You can run the command without the `--dry-run` command. It tells Django to convert our Python code into SQL code.
* `python3 manage.py showmigrations` - This shows migrartions done.
* `python3 manage.py migrate --plan` - Note: the plan flag shows what the command would do. **Run this at the after the initial setup to conduct the required migrations!**
* `python3 manage.py createsuperuser` - used to create a way to log in and look at the tables. Put in a username, email and password.
* To login to view the tables go to the url ending with `/admin` and put in your username and password.

#### Models:
* A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table.
* Models are created in the `models.py` file within the specific apps folder.
* Create a class, which will be the name of the table within the database and inherit `models.Model` to ensure that your class can do everything the built-in Django `model` class can do.
* You can define all fields within the class, but note that Django automatically creates an `id` field.
* `Charfield()` refers to a field consisting of characters or a string.
* `Booleanfield()` refers to a field consisting of a boolean value.
* After the class is created, make the migrations and a folder is created called `migrations`, which creates a file called `0001_initial.py` containing code creating the db table by converting code into SQL.
* Don't forget to the final migrate using only `migrate`as mentioned above. This is the step that converts the Python insto SQL.
* At this stage we can programmatically update the table, but we won't see it on the admin page, until you register it in the `admin.py`file. This can be done by importing the class within the models file and registering it with `admin.site.register(class_name)`.
* Note: By default all models that inherit the base model class in the `models.py` file will use its built-in string method to display their class name followed by the word "object" e.g. Item object(2). You can change this by overriding the `__str__` method and returning a suitable name.