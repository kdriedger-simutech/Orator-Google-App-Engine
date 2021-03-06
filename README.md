# Orator port for Google App Engine with Bottle Framework or webapp2 and File Helper

You can use this project for your App Engine application. 

Orator is a Eloquent (Laravel) port to Python, a very useful ORM library.

## HowTo Configure your project
app.yaml:
- set "application" field as your application ID
- set "version" field as your application version
- set "api_version" field as your API version

Config/config.py:
- modify config variable with your online/local application (user, password, unix_socket in the first "config"; user, password in the second "config")

FileHelper/file_helper.py (if you need File Helper, or simply delete FileHelper directory):
- modify "your GS dir/" with your Google Storage Directory 

## HowTo Configure this project in localhost
Windows:
- install Python 2.7 (note: check if HKEY_CURRENT_USER/Software/Python/PythonCore/2.7 variable in regedit is setted)
- install C++ compiler library for Python
- install MySql Python connector (MySQLdb)
- install MySql Python client connector (_mysqli)
- install Google App Engine SDK for Python
optionally:
- install PyCharm or Visual Studio 2015 + PTVS (Python Tools for Visual Studio)

## Simple example

With this library, you can use it as a demo and modify for your own purposes.

The file main.py contains the main program, that simply imports a Controller (UserController) that contains a simple method (get user data from database). You can test via REST API GET http calls. In this example, "/user_controller/get_profile/{ID}" return all data for user that have id "ID" formatted in JSON. All controllers is located in "Controllers" directory.

The "Models" directory contains Entity definition according to ORM Eloquent standard (table, hidden, fillable, relations etc...).

## Credits

The orator project belongs to MakarenaLabs and source code was written by Enrico Giordano. 

See Original Orator library: https://github.com/sdispater/orator

Modified to run on webapp2 by Kevin Driedger

