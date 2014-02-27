backloggery-puller
==================

A simple python modue that can pull down all the games and metadata from a backloggery account in a variety of different formats.

Feature List
------------

[X] Retrieve HTML containing entire backlog
	[X] Retrieve one page of HTML
	[X] Retrieve subsequent page with no overlap
	[X] Retrieve pages until the end is reached

[] Parse HTML to more useful formats
	[] Pull basic data from raw HTML
		[] Pull game name
		[] Pull completion status
		[] Pull game console name
		[] Pull game region
	[] Format basic data into XML
	[] Format basic data into JSON