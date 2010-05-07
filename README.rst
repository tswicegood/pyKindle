PyKindle
========
Python library for parsing Kindle clippings

Usage
-----
Pretty straight forward::

    >>> from kindle.parser import parse
    >>> path_to_clippings = "/Volumes/Kindle/documents/My Clippings.txt"
    >>> clippings = parse(path_to_clippings)

Now you have a list of dictionaries containing all of the data that Kindle
tracks inside its ``My Clippings.txt`` file.

For example, here's the structure of the last clipping out of my Kindle::

    >>> clippings[-1]
    {'author': 'Bryan Lawson',
     'date': datetime.datetime(2010, 5, 6, 21, 26, 0, 3),
     'location': '624-25',
     'notes': 'Clients often seem to find it easier to  communicate their wishes by reacting to and criticising a proposed  design, than by trying to draw up an abstract comprehensive performance   specification.',
     'title': 'How Designers Think, Fourth Edition: The Design Process Demystified',
     'type': 'Highlight'}


Handling Pragmatic Bookshelf books
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There is one oddity here that I feel obliged to mention (seeing as how I write
for them and you've all bought `<my book>http://pragprog.com/titles/tsgit`_ and
want to use pyKindle to parse your notes from it, right?): Pragmatic Bookshelf.

Each of the digital version that Pragmatic Bookshelf creates is watermarked
with the name of the original purchaser.  This is generally a good thing, but
if you're syncing to a site such as `<Readernaut>http://readernaut.com`_, you
need to be able to search the original book name.

You can provide filters (see the source code for examples) for all of the
fields as they come out of the Kindle.  Here's an example one-liner for
adjusting the title field to account for the Pragmatic Bookshelf issue::

    >>> from kindle.parser import filter_title
    >>> title_filter = lambda x: filter_title(x).replace(" (Travis Swicegood)", '')
    >>> clippings = kindle.parser.parse(path_to_clippings, title_filter=title_filter)

Dig into the code.  It's not complicated.  You'll be able to see what all the filters
are doing and how to make awesome filters for yourself. :-)
