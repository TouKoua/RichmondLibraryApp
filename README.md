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

# Install Pillow
Pillow is used to save book images within the database.
Run this command to install Pillow.
pip install Pillow

# Install ElasticSearch
The next thing we need to do is install Elasticsearch. 
Download ElasticSearch here:
https://www.elastic.co/downloads/elasticsearch
There are two installers, one for Windows and one for Mac. Take the one that fits your system.
I, TouKoua, was working with Windows, so this section will follow that installation.
1. Download elasticsearch for your own operating system.
2. After downloading the file, extract the files to where you can find them/want them. (Preferrably, near the root folder of your project).
3. Access that folder and navigate to the bin folder and locate elasticsearch.bat. This is the file we will run to setup the Elasticsearch
server.
4. After launching the file, the server should run and setup everything you need to run Elasticsearch locally. At the end, you can ignore
the things for Kibana and Docker as they are not necessary for this project. Instead, above the prompt for Kibana and Docker there should be
a generated password to connect to Elasticsearch server via this project application which you will use later. Save it within a text file,
as it will not generate again after the startup.
5. Find the file http_ca.crt in the confic/certs folder within the ElasticSearch folder, and save the path to find it via the file explorer
tab. Again, you may save this information for later occurances.
6. Launch the project if it is not already open and navigate to the settings.py file. You are looking for the ElasticSearch_DSL section where
you will replace the existing password in the http_auth field, shown by the randomized characters, and provide the path to the file http_ca.crt.
for ca_certs.

REMINDER: You will need to launch elasticsearch.bat everytime you wish to use the application correctly as the database queryset or the process
of retrieving data from the database requires elasticsearch to be running in our implementation locally. A cloud service will differ as it will
almost constantly, hardware depending, be running.

# ElasticSearch DSL
This project also uses Elasticsearcg DSL
1. Run this command to install the required files: pip install django-elasticsearch-dsl
2. Add 'django_elasticsearch_dsl' to the INSTALLED_APPS in settings.py
3. define ELASTICSEARCH_DSL in settings.py with the password given from ElasticSearch and
4. run this command to setup the index (collection of defined models):
python manage.py search_index --rebuild

the absolute OR relative path to http_ca.crt file with in elasticsearch directory.

# Social Account Authentication
This project also has the option to authenticate using Google accounts.
We need to install the package that has this functionality.
Do this by running the following command
pip install django-allauth

Everything should be setup correctly, so you just need to run the project.