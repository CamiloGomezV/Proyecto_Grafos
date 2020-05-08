from igraph import *
import unicodedata #Eliminar tildes

g = Graph()
g.add_vertex("prueba") #vertex set initializer

n_classes = 9

bins = [[] for x in range(n_classes)]


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
            vertex_id = data11
            bin_id  = strings[2]

            if bin_id == "Escuela de Administración":
                new_bin_id = 0
            elif bin_id == "Facultad de Jurisprudencia":
                new_bin_id = 1
            elif bin_id == "Facultad de Ciencias Naturales":
                new_bin_id = 2
            elif bin_id == "Escuela de Ciencias Humanas":
                new_bin_id = 3
            elif bin_id == "Escuela de Medicina y Ciencias de la Salud":
                new_bin_id = 4
            elif bin_id == "Facultad de Economía":
                new_bin_id = 5
            elif bin_id == "Facultad de Estudios Internacionales, Políticos y Urbanos":
                new_bin_id = 6
            elif bin_id == "Facultad de Creación":
                new_bin_id = 7
            elif bin_id == "Escuela de Ingeniería, Ciencia y Tecnología":
                new_bin_id = 8

            bins[new_bin_id].append(vertex_id)

        if data22 not in g.vs["name"]:

            g.add_vertex(data22)
            vertex_id = data22
            bin_id  = strings[4]
            if bin_id == "Escuela de Administración":
                new_bin_id = 0
            elif bin_id == "Facultad de Jurisprudencia":
                new_bin_id = 1
            elif bin_id == "Facultad de Ciencias Naturales":
                new_bin_id = 2
            elif bin_id == "Escuela de Ciencias Humanas":
                new_bin_id = 3
            elif bin_id == "Escuela de Medicina y Ciencias de la Salud":
                new_bin_id = 4
            elif bin_id == "Facultad de Economía":
                new_bin_id = 5
            elif bin_id == "Facultad de Estudios Internacionales, Políticos y Urbanos":
                new_bin_id = 6
            elif bin_id == "Facultad de Creación":
                new_bin_id = 7
            elif bin_id == "Escuela de Ingeniería, Ciencia y Tecnología":
                new_bin_id = 8

            bins[new_bin_id].append(vertex_id)

        #Añadir Aristas
        g.add_edge(data11,data22)

        line = file.readline()


g.delete_vertices("prueba")

g.simplify() #Making simple g

node_colours = []

for i in g.vs["name"]:
    if i in bins[0]:
        node_colours.append("green")
    elif i in bins[1]:
        node_colours.append("yellow")
    elif i in bins[2]:
        node_colours.append("red")
    elif i in bins[3]:
        node_colours.append("blue")
    elif i in bins[4]:
        node_colours.append("orange")
    elif i in bins[5]:
        node_colours.append("pink")
    elif i in bins[6]:
        node_colours.append("purple")
    elif i in bins[7]:
        node_colours.append("brown")
    elif i in bins[8]:
        node_colours.append("white")
    else:
        node_colours.append("grey")

out_fig_name = "labelled_graph.eps"

g.vs["color"] = node_colours

visual_style = {}

# Define colors used for outdegree visualization
colours = ['#fecc5c', '#a31a1c']

# Set bbox and margin
visual_style["bbox"] = (3000,3000)
visual_style["margin"] = 20

# Set vertex size
visual_style["vertex_size"] = 40

# Set vertex lable size
visual_style["vertex_label_size"] = 8

# Don't curve the edges
visual_style["edge_curved"] = False

# Set the layout
my_layout = g.layout_davidson_harel()
visual_style["layout"] = my_layout

# Plot the graph
plot(g, out_fig_name, **visual_style)
