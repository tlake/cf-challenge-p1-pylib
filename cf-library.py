'''
Use object-oriented Python to model a public library (w/ three classes: Library,
Shelf, & Book). 

The library should be aware of a number of shelves. Each shelf should know what
books it contains. Make the book object have "enshelf" and "unshelf" methods that 
control what shelf the book is sitting on. The library should have a method to
report all books it contains. Note: this should *not* be a Django (or any other) 
app - just a single file with three classes (plus commands at the bottom showing
it works) is all that is needed. 
'''


# The library needs to know how many shelves it has
# It needs to have a method to report all the books it contains
# (that should include both shelved and unshelved books)
class Library(object):

    def __init__(self):
        self.shelves = []
        self.unshelved_books = []

    def report(self):
        for shelf in self.shelves:
            print "\nShelf " + shelf.title + ":"
            shelf.report()
        print "\nUnshelved Books:"
        for book in self.unshelved_books:
            print book.author + ": " + book.title


# The Shelf needs to know which books it contains
class Shelf(object):

    def __init__(self, library, title):
        self.books = []
        self.library = library
        self.library.shelves.append(self)
        self.title = title

    def report(self):
        for book in self.books:
            print book.author + ": " + book.title

# A Book needs 'enshelf' and 'unshelf' methods
class Book(object):

    def __init__(self, title, author, library):
        self.title = title
        self.author = author
        self.shelf = "unshelved"
        self.library = library
        library.unshelved_books.append(self)

    def enshelf(self, shelf):
        if self in self.library.unshelved_books:
            self.library.unshelved_books.remove(self)
        else:
            self.shelf.books.remove(self)
        self.shelf = shelf
        shelf.books.append(self)

    def unshelf(self):
        if self in self.shelf.books:
            self.shelf.books.remove(self)
        self.library.unshelved_books.append(self)
        self.shelf = "unshelved"

    def report(self):
        if self.shelf == "unshelved":
            print self.shelf
        else:
            print self.shelf.title


'''
COMMANDS
'''
# initial instantiation
print "INITIAL SETUP"

libfellows = Library()

a_m = Shelf(libfellows, "A-M")
n_z = Shelf(libfellows, "N-Z")

cold_days = Book("Cold Days", "Butcher, Jim", libfellows)
hurin = Book("The Children of Hurin", "Tolkien, J. R. R.", libfellows)
name_wind = Book("The Name of the Wind", "Rothfuss, Patrick", libfellows)


# report
print "CALLING THE LIBRARY'S REPORT METHOD:"

libfellows.report()


# shelve two of the books
print "\nSHELVING TWO BOOKS"

cold_days.enshelf(a_m)
name_wind.enshelf(n_z)

# call each of the books' report method to learn where they are
print "\nBOOK REPORTS"

cold_days.report()
hurin.report()
name_wind.report()

# alternatively, let's call the library's report method
print "\nLIBRARY REPORT"

libfellows.report()

# and because why not, let's also call the report methods of the shelves
print "\nSHELF REPORTS"

a_m.report()
n_z.report()

# let's also make sure that the unshelf method works
print "\nUNSHELF, BOOK REPORT, LIBRARY REPORT"

cold_days.unshelf()
cold_days.report()
libfellows.report()

# proving that enshelf works from shelf to shelf, too
print "\nMOVING FROM ONE SHELF TO ANOTHER"

name_wind.enshelf(a_m)
libfellows.report()
