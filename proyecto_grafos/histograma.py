from igraph import *
from random import *
import matplotlib.pyplot as plt
import numpy as np
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
xmin = g.ecount()

x = []
y = []

def mydegree():
    separation = 0
    for i in g.vs():
        separation += g.eccentricity(i)

    separation /= g.vcount()

    return separation

for i in range(2000):
    if i%10==0:
        x.append(int(g.ecount()))
        y.append(mydegree())
    g.add_edge(randint(0,rang),randint(0,rang))


plt.rcParams.update({'font.size': 17})


plt.figure(figsize=(40,10))
plt.plot(x, y, linewidth=3.0)
plt.ylabel('Separation degree')
plt.xlabel('number of edges')
plt.title('variation of separation degree')
plt.xlim(xmin,g.ecount())
plt.yticks(np.arange(int(min(y))+2, int(max(y))+1, 2.0))
plt.xticks(np.arange(min(x), max(x)+1, 50.0))
plt.grid(True)
plt.savefig('separation_degree.png', bbox_inches='tight')
plt.show()
plt.draw()
