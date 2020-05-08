from igraph import *
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


g.delete_vertices("prueba")

g.simplify() #Making simple g

out_fig_name = "graph.eps"

visual_style = {}

# Define colors used for outdegree visualization
colours = ['#fecc5c', '#a31a1c']

# Set bbox and margin
visual_style["bbox"] = (4000,4000)
visual_style["margin"] = 40

# Set vertex colours
visual_style["vertex_color"] = 'grey'

# Set vertex size
visual_style["vertex_size"] = 40

# Set vertex lable size
visual_style["vertex_label_size"] = 8

# Don't curve the edges
visual_style["edge_curved"] = False

# Set the layout
my_layout = g.layout_davidson_harel()
visual_style["layout"] = my_layout

#Plot the graph
plot(g, out_fig_name, **visual_style)
