**Archive Notice**: As of May 22nd 2024, [The Backloggery has had a total UI redesign](https://www.patreon.com/posts/remake-launch-104736678) rendering this package unusable. If you want similar functionality, [The Backloggery now has a CSV export function](https://www.patreon.com/posts/site-update-v1-1-108426624).

Thank you so much to everyone who used this project, asked for new features, and made contributions!

backlog_puller
==============

*Formerly `backloggery-puller`*

`backlog_puller` is a simple python module that can pull a user's complete video game backlog from [The Backloggery](http://www.backloggery.com) given a username. The results can be returned in XML and JSON format as well as a regular ole' python object.

Setup
=====

Make sure you have python 2.7.x installed.

That's it! The `backloggery-puller` module only relies on The Python Standard Library to work properly. Other versions of Python 2 might work, but they haven't been tested.

Installation
============

You can install `backlog_puller` from PyPi with the following command:

`pip install backlog_puller`

When `backlog_puller` is installed the `backlog_pull` command is also installed. Simply enter:

`backlog_pull {username}` 

on your terminal of choice and you will get a JSON representation of that user's backlog.

Usage
=====

`backloggery-puller` consists of two major components: A GamesRequest that pulls the raw HTML from The Backloggery, and the BacklogHTMLParser that converts the raw html into more useful output.

**For example:**
```python
import backloggery_puller

request = GamesRequest("username")
parser = BacklogHTMLParser()
parser.feed(request.get_raw_page())
print parser.backlog
```

Will create a `GamesRequest` for the user `"username"` and feed it into a `BacklogHTMLParser` where it will be stored as a python dictionary. The `BacklogHTMLParser` can then output the parsed data as XML, JSON, or a serialized Python object.

Feature List/Todos
==================

- [X] Retrieve HTML containing entire backlog  
    - [X] Retrieve one page of HTML  
    - [X] Retrieve subsequent page with no overlap  
    - [X] Retrieve pages until the end is reached  
- [ ] Parse HTML to more useful formats  
    - [X] Pull basic data from raw HTML  
        - [X] Pull game name  
        - [X] Pull completion status  
        - [X] Pull game console name
    - [ ] Pull advanced data from raw HTML
    - [X] Format basic data into XML  
    - [X] Format basic data into JSON  
    - [ ] Format basic data into CSV  
