from nodes import WikiPage
from queue import Queue

start = WikiPage('https://en.wikipedia.org/wiki/Breadth-first_search')
goal = WikiPage('https://en.wikipedia.org/wiki/New_York_City')

frontier = Queue()
frontier.put(start)

reached = set()

while frontier.qsize() > 0:
    node: WikiPage = frontier.get()
    for child in node.children:
        if child == goal:
            print('found path: ', child.get_ancestors())
            print(frontier.qsize(), len(reached))
            exit()

        if child not in reached:
            reached.add(child)
            frontier.put(child)

print('failed')


