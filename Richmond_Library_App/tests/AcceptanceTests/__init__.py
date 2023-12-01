import sys
sys.path.append(r"C:\Users\Proje\Desktop\Projects\RichmondLibraryApp")
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Richmond_Library_App.settings")
django.setup()

from Richmond_Library_App.tests.AcceptanceTests.test_addBook import *
from Richmond_Library_App.tests.AcceptanceTests.test_editUser import *
from Richmond_Library_App.tests.AcceptanceTests.test_login import *
from Richmond_Library_App.tests.AcceptanceTests.test_logout import *
from Richmond_Library_App.tests.AcceptanceTests.test_removeBook import *

# To run all tests within the direct use the command below:
# python manage.py test Richmond_Library_App.tests.AcceptanceTests
# To run a specific test file within the direct use the command:
# python manage.py test Richmond_Library_App.tests.AcceptanceTests.(test file name)