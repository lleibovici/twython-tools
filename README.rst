Twython Tools
=============

Command line scripts and tools for implementing Twython functions.

Incorporates functions from other Python libraries and modules,
including twython, requests, PyCrypto, simplecrypt (included), and
foad.py (optional).

Use of Tor is optional.

GPG is no longer used for encrypting the OAuth data. There is, of
course, nothing wrong with GPG itself, but there is plenty of concern
with the impending conflict between the python-gnupg package and the
more recent fork.

The foad.py script is `here <https://github.com/adversary-org/foad>`__.

Python version specific information is in the Documentation/ directory.


REQUIREMENTS
------------

-  Python 3.3 or greater (3.4 or above recommended).
-  Current version of Twython.
-  Current version of Requests.
-  Current version of PyCrypto.

I recommend reinstalling Requests with the --upgrade flag after Twython
is installed as Twython tends to install an older version. As this code
depends on Twython you can skip Requests and rely on the version
installed by Twython by default.

To use the scripts which post images to Twitter requires additional
software not included in this project.  In particular, `wkhtmltopdf
<https://github.com/wkhtmltopdf/wkhtmltopdf>`__, which is a component
of wkhtmltopdf.  Some people might prefer to use ImageMagick or
something else instead.  To convert text to HTML or XHTML I use the
Haskell program, `Pandoc <http://pandoc.org>`__.

The main scripts affected by this are tweet-full.py and tweet-long.py.
The former uses whatever images are fed to it and the latter uses
specific programs (Pandoc and wkhtmltoimage) to generate an image of
text from a text file.  Most often the text file will be converted
from Markdown, reStructuredText or Emacs' Org-Mode.  The default or
fallback is to use Markdown, especially if the extension is .txt.


Recommendations
---------------

-  Python 3.4 or greater.
-  Current version of Twython.
-  Current version of Requests.
-  Current version of PyCrypto.
-  Current version of Pandoc.
-  Current version of wkhtmltopdf.
-  Current version of Tor or the Tor Browser.

Note that Tor only needs to be running to be used.  The code will
automatically test for the presence of a SOCKS or HTTP proxy on the
standard Tor ports (9050 and 9150) and the standard Privoxy
port (8118) to connect through.  If those ports are open, then it will
be used, otherwise it will connect directly.


Installation
~~~~~~~~~~~~

Note: it may be necessary to use sudo on POSIX systems (including OS X):

::

    pip3 install --upgrade twython
    pip3 install --upgrade requests
    pip3 install --upgrade pycrypto


Contacting me
-------------

My email address is in most of the scripts in this project as well as
included in my GPG key as the primary user ID.

A minimised copy of my GPG key is in the Documentation/ directory
(ben-key-min.asc), this version does not include all the current
signatures. Refreshing that key from the key servers will restore those
signatures.

To get my key directly from the servers run:

::

    gpg --recv-keys 0x321E4E2373590E5D

To refresh my key if it is already in your keyring run:

::

    gpg --refresh-keys 0x321E4E2373590E5D

You can also visit my `website <http://www.adversary.org/>`__ or `follow
me on Twitter <https://twitter.com/benmcginnes>`__.


Using the Scripts
-----------------

The scripts generally take their parameters on the command line, but are
also able to receive those parameters through interactive text prompts.
Generally I recommend the latter at least until you are familiar enough
with the order to run them without those prompts (or until I get around
to updating them to use argparse).
