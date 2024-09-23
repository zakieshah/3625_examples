from nodes import WikiPage
from queue import Queue


# see the bottom of nodes.py for example of how to use the WikiPage objects

# define start and end pages
start = WikiPage('https://en.wikipedia.org/wiki/Breadth-first_search')
goal = WikiPage('https://en.wikipedia.org/wiki/New_York_City')

# write a search algorithm to find a path from start to goal
