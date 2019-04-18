# Directed graph (each unordered pair of nodes is saved once): roadNet-CA.txt 
# California road network
# Nodes: 1965206 Edges: 5533214
# FromNodeId	ToNodeId

# Directed graph (each unordered pair of nodes is saved once): roadNet-PA.txt 
# Pennsylvania road network
# Nodes: 1088092 Edges: 3083796
# FromNodeId	ToNodeId

# Directed graph (each unordered pair of nodes is saved once): roadNet-TX.txt 
# Texas road network
# Nodes: 1379917 Edges: 3843320
# FromNodeId	ToNodeId

import networkx as nx
import  matplotlib.pyplot as plt

f = open("road-usroads.mtx","r")
x = f.read()
y = x.split()
# even numbers = node
# odd number = edge connections

G = nx.dodecahedral_graph()
i = 0
print("graph size = " + str(len(y)))
while(i != 10000 ):# len(y)):
    if( i % 2 == 0):
        G.add_node(y[i])
    else:
        G.add_edge(y[i-1], y[i])
    i+=1
    print(i)

#pos = nx.complete_graph(G)
#plt.subplot(121)
nx.draw_networkx(G, width=.09, node_shape = ".", node_color="red", node_size=10, with_labels=False)
#plt.show()
plt.savefig("roadyroadroad.png", dpi=1000, bbox_inches='tight', format="PNG")