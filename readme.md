# Writing Django!

- it is a convention to call the project "mysite"

- next step, you create an app (python3 manage.py startapp appname) with the name of the main app your project will be about

- you can change the timezone of your server in the main settings.py module

- the whole project is a package, thanks to the __init__.py file, which means all sub documents or objects can be imported.

- you can customize and import configurations, different dbs and even web servers gateways! for your project, this framework is really flexible! 

- nor python or django can serve as web servers, so they need a middleware. It used to be a group of APIs in the past, nowadays, WSGI and ASGI web servers providers do the thing. 

- sqlite comes by default with django, however, the most suitable db for the typical django projects may be a postgresql rdb

- migrations only runs for installed_apps

- each installed app in your django project contains models. Those models are classes which represents tables in our database schema. As soon as you start a brand new django project, it's cool to run migrations for the default apps which of course have models, and you shall run 

python3 manage.py makemigrations 

for each brand new app you add to your
installed_apps

- migrations are changes to your model