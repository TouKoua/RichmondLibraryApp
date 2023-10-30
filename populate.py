import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Richmond_Library_App.settings")
django.setup()
from Richmond_Library_App.models import Book


# Run the populate.py to fill out book database with given information
def populate():
    booklist = [("The Way of Kings", "Sanderson, Brandon", 9780765365279, 2011, "Tor Fantasy", 1, 1, 'static\images\TheWayOfKings.png'),
            ("Word of Radiance", "Sanderson, Brandon", 9780765365286, 2015, "Tor Fantasy", 1, 1, 'static\images\WordsOfRadiance.jpg'),
            ("Oathbringer", "Sanderson, Brandon", 9783453270381, 2017, "Tor Fantasy", 1, 1, 'static\images\Oathbringer.jpg'),
            ("Rhythm of War", "Sanderson, Brandon", 9780765326386, 2020, "Tor Books", 1, 1, 'static\images\RhythmofWar.jpg'),
            ("Harry Potter and the Sorcercer's Stone", "J.K. Rowling", 9780590353427, 1997, "Scholastic", 1, 1, 'static\images\harrypotterandthesorcererstonecoverart.jpg'),
            ("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 9780439064866, 1998, "Scholastic", 1, 1, 'static\images\harrypotterandthechamberofsecrets.jpg'),
            ("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 9780439655484, 1999, "Scholastic", 1, 1, 'static\images\harrypotterandtheprisonerofazkaban.jpg'),
            ("Harry Potter and the Goblet of Fire", "J.K. Rowling", 9780439139601, 2000, "Scholastic", 1, 1, 'static\images\harrypotterandthegobletoffire.jpg'),
            ("Harry Potter and the Order of the Phoenix", "J.K. Rowling", 9780439358071, 2003, "Scholastic", 1, 1, 'static\images\harrypotterandtheorderofthephoenix.jpg'),
            ("Harry Potter and the Half-Blood Prince", "J.K. Rowling", 9780439785969, 2005, "Scholastic", 1, 1, 'static\images\harrypotterandthehalfbloodprince.jpg'),
            ("Harry Potter and the Deathly Hallows", "J.K. Rowling", 9780545010221, 2007, "Scholastic", 1, 1, 'static\images\harrypotterandthedeathlyhallows.jpg'),
            ("Crazy Rich Asians", "Kevin Kwan", 9780345803788, 2014, "Anchor", 1, 1, 'static\images\crazyrichasianscoverart.jpg'),]
    
    for i in booklist:
        if Book.objects.filter(title=i[0]).exists() == False:
            newbook = Book.objects.create(title=i[0], author=i[1], isbn=i[2], year=i[3], publisher=i[4], copies=i[5], available=i[6], image=i[7])
            newbook.save()


if __name__ == "__main__":
    populate()