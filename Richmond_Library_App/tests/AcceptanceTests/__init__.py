import sys
sys.path.append(r"C:\Users\Proje\Desktop\Projects\RichmondLibraryApp")
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Richmond_Library_App.settings")
django.setup()

from Richmond_Library_App.tests.AcceptanceTests.test_editUser import *