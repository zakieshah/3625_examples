from nodes import WikiPage
from queue import Queue


# see the bottom of nodes.py for example of how to use the WikiPage objects

# define start and end pages
start = WikiPage('https://en.wikipedia.org/wiki/Breadth-first_search')
goal = WikiPage('https://en.wikipedia.org/wiki/New_York_City')

# write a search algorithm to find a path from start to goal
frontier = Queue()
frontier.put(start)
reached = {start}

while not frontier.empty():
    state = frontier.get()
    for child in state.children:
        
        if child == goal:
            print(child.get_ancestors())
            exit()
        if child not in reached:
            reached.add(child)
            frontier.put(child)
