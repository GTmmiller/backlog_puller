backloggery-puller
==================

`backloggery-puller` is a simple python modlue that can pull a user's complete video game backlog from [The Backloggery](http://www.backloggery.com) given a username. The results can be returned in XML and JSON format as well as a regular ole' python object.

Setup
=====

Make sure you have python 2.8.x installed.

That's it! `backloggery-puller` only relys on The Python Standard Library to work properly.

Usage
=====

`backloggery-puller` consists of two major components: A GamesRequest that pulls the raw HTML from The Backloggery, and the BacklogHTMLParser that converts the raw html into more useful forms.

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
