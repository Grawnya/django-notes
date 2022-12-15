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