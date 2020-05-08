from igraph import *
from random import *

def strong_version(n):
    h = Graph()

    g = h.Growing_Random(n,1,citation=True)

    g.simplify()

    seed(1)

    rang = g.vcount()-1

    while g.diameter() > 6:
        g.add_edge(randint(0,rang),randint(0,rang))

    g.simplify()

    print("Number of vertices:", g.vcount())
    print("Number of edges:", g.ecount())
    print("Density of the graph:", 2*g.ecount()/(g.vcount()*(g.vcount()-1)))

    degrees = []
    total = 0

    for n in range(g.vcount()):
        neighbours = g.neighbors(n, mode='ALL')
        total += len(neighbours)
        degrees.append(len(neighbours))

    print("Average degree:", total/g.vcount())
    print("Maximum degree:", max(degrees))

    separation = 0
    for i in g.vs():
        separation += g.eccentricity(i)

    separation /= g.vcount()

    print("Separation degree: ", separation)
    print("Radius: ",g.radius())
    print("Diameter: ",g.diameter())
