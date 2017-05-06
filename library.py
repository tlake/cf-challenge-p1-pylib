"""
Python Example: A Simple Library

This is just a sample three-class system to emulate a simple approximation of
a library. The goal is to tightly encapsulate functionality into classes.

Further good features to implement later include:
    - allow unshelved Books in a Library
    - Book method to add/remove itself to/from a Shelf
    - Book method to add/remove itself to/from a Library
    - Shelf method to add/remove itself to/from a Library
    - Shelf method to add/remove Books to/from itself
    - Library method to add/remove Books to/from one of its Shelves
    - (all of the above methods should make sure everything is updated)
"""

class Library(object):
    """The Library object.

    Has a collection of Shelves, which can contain Books. Can report every
    Book within itself. Also has methods to update the associated Shelf for
    all Books it contains, and to update the associated Library for all
    Books and Shelves it contains.
    """

    def __init__(self, name, shelves=[]):
        """Configures a Library object."""

        self.name = name
        self.shelves = []
        for shelf in shelves:
            self.shelves.append(shelf)
        self._sync_shelves()
        self._sync_books()
    
    def __repr__(self):
        """Customizes the internal representation of a Library instance."""

        return "<Library: {}>".format(self.name)

    def __str__(self):
        """Customizes the human-readable representation of a Library instance."""

        return self.name

    def _sync_shelves(self):
        """Updates all Shelf objects in the Library with their current Library."""

        for shelf in self.shelves:
            shelf.library = self
    
    def _sync_books(self):
        """Updates all Book objects in the Library with their current Library and Shelf."""

        for shelf in self.shelves:
            shelf._sync_books()

    def get_shelves(self):
        """Returns a list of the Shelf objects that the Library contains."""

        return self.shelves

    def list_shelves(self):
        """Prints a list of the Shelf objects that the Library contains."""

        for shelf in self.shelves:
            print(shelf)

    def get_books(self):
        """Returns a list of the Book objects that the Library's Shelves contain."""

        books = []
        for shelf in self.shelves:
            books += shelf.get_books()
        return books

    def list_books(self):
        """Prints a list of the Book objects that the Library's Shelves contain."""

        for shelf in self.shelves:
            shelf.list_books()


class Shelf(object):
    """The Shelf object.
    
    Has a list of Book objects. Can report every Book it contains. Also contains
    a method to update the associated Shelf for all Books it contains."""

    def __init__(self, name, books=[]):
        """Configures a Shelf object."""

        self.name = name
        self.books = []
        self.library = None
        for book in books:
            self.books.append(book)
        self._sync_books()

    def __repr__(self):
        """Customizes the internal representation of the Shelf object."""

        return "<Shelf: {} (library: {})>".format(
            self.name,
            self.library
        )

    def __str__(self):
        """Customizes the human-readable representaion of the Shelf object."""

        return self.name

    def _sync_books(self):
        """Updates all Book objects within the Shelf with their current Library and Shelf."""

        for book in self.books:
            book.library = self.library
            book.shelf = self

    def get_books(self):
        """Returns a list of the Book objects that the Shelf contains."""

        return self.books

    def list_books(self):
        """Prints a list of the Book objects that the Shelf contains."""

        for book in self.books:
            print(book)


class Book(object):
    """The Book object.

    Books have a title and an author, a notion of the Shelf on which it resides, and
    the Library in which it resides."""

    def __init__(self, title, author):
        """Configures a Book object."""

        self.title = title
        self.author = author
        self.library = None
        self.shelf = None

    def __repr__(self):
        """Customizes the internal representation of the Book object."""

        return "<Book: {} by {} (library: {}, shelf: {})>".format(
            self.title,
            self.author,
            self.library,
            self.shelf
        )

    def __str__(self):
        """Customizes the human-readable representation of the Book object."""

        return "'{}'".format(self.title)


if __name__ == "__main__":
    """In this block, I run a sequence of commands to demonstrate the functionality
    and features of the module. This chunk of code executes when this file is run
    with Python from the command line:
        
    $: python library.py
    """

    print("""First, let's start by creating a couple of books, a shelf, and a library:

    ```
    book1 = Book(
        title="The Name of the Wind",
        author="Patrick Rothfuss",
    )

    book2 = Book(
        title="The Wise Man's Fear",
        author="Patrick Rothfuss",
    )

    shelf1 = Shelf(
        name="rothfuss",
        books=[book1, book2],
    )

    library1 = Library(
        name="The Rothfuss National Library",
        shelves=[shelf1],
    )
    ```
""")

    
    book1 = Book(
        title="The Name of the Wind",
        author="Patrick Rothfuss",
    )

    book2 = Book(
        title="The Wise Man's Fear",
        author="Patrick Rothfuss",
    )

    shelf1 = Shelf(
        name="rothfuss",
        books=[book1, book2],
    )

    library1 = Library(
        name="The Rothfuss National Library",
        shelves=[shelf1],
    )

    print("Let's inspect our world:")

    print("\n>>> print(library1)")
    print(library1)

    print("\n>>> library1.list_shelves()")
    library1.list_shelves()

    print("\n>>> library1.list_books()")
    library1.list_books()

    print("\n>>> print(library1.get_shelves()")
    print(library1.get_shelves())

    print("\n>>> library1.get_books()")
    print(library1.get_books())

    print("""

Now let's add another shelf and some more books:

    ```
    book3 = Book(
        title="The Doors of Stone",
        author="Patrick Rothfuss",
    )

    shelf1.books.append(book3)

    book4 = Book(
        title="The Sparrow",
        author="Maria Doria Russell",
    )

    book5 = Book(
        title="The Lies of Locke Lamora",
        author="Scott Lynch",
    )

    shelf2 = Shelf(
        name="NOT-fuss",
    )
    ```
""")

    book3 = Book(
        title="The Doors of Stone",
        author="Patrick Rothfuss",
    )

    shelf1.books.append(book3)

    book4 = Book(
        title="The Sparrow",
        author="Maria Doria Russell",
    )

    book5 = Book(
        title="The Lies of Locke Lamora",
        author="Scott Lynch",
    )

    shelf2 = Shelf(
        name="NOT-fuss",
    )

    print("Let's inspect the world again:")

    print("\n>>> library1.list_shelves()")
    library1.list_shelves()

    print("\n>>> library1.list_books()")
    library1.list_books()

    print("\n>>> print(shelf2)")
    print(shelf2)

    print("\n>>> print([shelf2])")
    print([shelf2])

    print("\n`shelf2` should be empty of books:")
    print(">>> print(shelf2.get_books()")
    print(shelf2.get_books())

    print("\n>>> print([book3])")
    print([book3])

    print("\n>>> print([book4])")
    print([book4])
    
    print("\n>>> print([book5])")
    print([book5])

    print("""

Finally, let's add those homeless books and shelves to the library:

    ```
    library.shelves.append(shelf2)
    shelf2.books.extend([book4, book5])
    ```
""")

    library1.shelves.append(shelf2)
    shelf2.books.extend([book4, book5])

    print("But oh no! Those things don't know that they've been added!")

    print("\n>>> print(book3.shelf)")
    print(book3.shelf)

    print("\n>>> print(book3.library)")
    print(book3.library)

    print("\n>>> print(shelf2.library)")
    print(shelf2.library)

    print("\n>>> print(book4.shelf)")
    print(book4.shelf)
    
    print("\n>>> print(book4.library)")
    print(book4.library)

    print("""

Let's make the library update everything:

    ```
    library1._sync_shelves()
    library2._sync_books()
    ```
""")

    library1._sync_shelves()
    library1._sync_books()

    print("\n>>> print(book4.shelf)")
    print(book4.shelf)
    
    print("\n>>> print(book4.library)")
    print(book4.library)

    print("\n>>> print(shelf2.library)")
    print(shelf2.library)

    print("\n>>> library1.list_shelves()")
    library1.list_shelves()

    print("\n>>> shelf1.list_books()")
    shelf1.list_books()

    print("\n>>> shelf2.list_books()")
    shelf2.list_books()

    print("\n>>> library1.list_books()")
    library1.list_books()

