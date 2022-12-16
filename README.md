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
<br/>

`os.environ[SECRET_KEY] = insert secret key`
<br/>
and in the setting file:
<br/>

`SECRET_KEY = os.getenv("SECRET_KEY")`

* To run the project: `python3 manage.py runserver`

#### Creating an App:
* Type `python3 manage.py startapp app_name` in the terminal to create an app.
* Note the `urls.py` website can be used to activate functions in `views.py` within the project folder and requires the built-in `path` function, which takes 3 arguments:
    - the url that the user is going to type in
    - the view function that it's going to return
    - a name parameter
