# RichmondLibraryApp
This is a Capstone Project being done for UWM CS595. We were tasked with creating a Library Application for the Richmond School District.

# To get started:

Make sure you have Python install on your machine. This project was created using Python 3.11
Run this command to check your Python version:
python --version

If you need to install Python, do so with the following link:
https://www.python.org/downloads/

# Using VSCode
If you're using VSCode, make sure you setup your virtual enviroment before moving on. Otherwise the following python commands will not work.
Head to the command palette and search for Python: Create Environment and then click on Venv.
From there, choose your python version and VSCode should begin the process to create a new virtual environment.

# Install Django
After installing Python, make sure you have Django installed. This project is using Django 4.2.5
Run this command to install Django:
pip install Django==4.2.5

Run this command to check your Django version:
python -m django --version

# Install Bootstrap
The next thing we need to do is install bootstrap. This project uses Bootstrap 5
Run this command to install Bootstrap:
pip install django-bootstrap-v5

# Install ElasticSearch
The next thing we need to do is install Elasticsearch. 
Download ElasticSearch here:
https://www.elastic.co/downloads/elasticsearch
There are two installers, one for Windows and one for Mac. Take the one that fits your system.
I was working with Windows, so this section will follow that installation.
After downloading the file, extract the files to where you can find them/want them. (Preferrably, near the root folder of your project).
Now go into the folder, go into the bin folder, and find elasticsearch.bat. This is the file we will run
Starting that file will run the server and setup everything you need to run elasticsearch locally.
At the end, you should see things for Kibana and Docker. Ignore those and look for where the password
for the elastic user is. Copy that and save it somewhere, you will need this later.
Now go back to the project and open the settings file and find the ElasticSearch_DSL section.
Place the password you got in the http_auth section.
You will also need to provide the path to the elasticsearch certificate from the project root folder.
In the elasticsearch folder, the certificate is located at config/certs/http_ca.ct

# ElasticSearch DSL
This project also uses Elasticsearcg DSL
First, Run this command to install the required files:
pip install django-elasticsearch-dsl
Second, add 'django_elasticsearch_dsl' to the INSTALLED_APPS in settings.py
Third, define ELASTICSEARCH_DSL in settings.py.

# Social Account Authentication
This project also has the option to authenticate using Google accounts.
We need to install the package that has this functionality.
Do this by running the following command
pip install django-allauth

Everything should be setup correctly, so you just need to run the project.