import networkx as nx
import  matplotlib.pyplot as plt
import sys, random, string


def randhex():
    hex_c = "#"
    for i in range(6):
        hex_c += random.choice("ABCDEF0123456789")
        print(hex_c)
    return hex_c

G = nx.Graph()
road = []
edges = []
clusteredNode = []
for i in range(1,int(sys.argv[1])):
     road.append(i)
     G.add_node(i)
for i in range(1, len(road)): 
         randy = random.randint(1, len(road)+1)
         if(road[i] != randy):
             G.add_edge(road[i], randy)

#pos = nx.complete_graph(G)
#plt.subplot(121)
nx.draw_networkx(G, width=.09, node_shape = ".", node_color= randhex(), node_size=10, with_labels=False)
#plt.show()
plt.savefig("roadyroadroad.png", dpi=700, bbox_inches='tight', format="PNG")