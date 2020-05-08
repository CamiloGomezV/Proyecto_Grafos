from igraph import *
from random import *
import unicodedata #Eliminar tildes

g = Graph()
g.add_vertex("prueba") #vertex set initializer

with open("Grafos 3.csv", 'r') as file:
    line = file.readline()

    while line != "":
        strings = line.rstrip().split("\",\"")

        #Eliminar Tildes, Mayusculas y espacios en blanco
        data1 = strings[1]
        data2 = strings[3]

        a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
        trans = str.maketrans(a,b)

        data11 = data1.translate(trans).lower().replace(" ","").replace(".","")
        data22 = data2.translate(trans).lower().replace(" ","").replace(".","")

        #Añadir Vértices
        if data11 not in g.vs["name"]:
            g.add_vertex(data11)
        if data22 not in g.vs["name"]:
            g.add_vertex(data22)

        #Añadir Aristas
        g.add_edge(data11,data22)

        line = file.readline()

seed(1)
g.delete_vertices("prueba")

rang = g.vcount()-1

print("Edges before: ", g.ecount())
print("Density of the graph:", 2*g.ecount()/(g.vcount()*(g.vcount()-1)))

while g.diameter() > 6:
    g.add_edge(randint(0,rang),randint(0,rang))

g.simplify()

print("Edges After: ", g.ecount())

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
#print("Vertex ID with the maximum degree:", degrees.index(max(degrees)))

separation = 0
for i in g.vs():
    separation += g.eccentricity(i)

separation /= g.vcount()

print("Separation degree: ", separation)

print("Radius: ",g.radius())
print("Diameter: ",g.diameter())
