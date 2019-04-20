
import networkx as nx
import  matplotlib.pyplot as plt
import sys
f = open(sys.argv[1],"r")
x = f.read()
y = x.split()
# even numbers = node
# odd number = edge connections

G = nx.dodecahedral_graph()
i = 0
print("graph size = " + str(len(y)))
while(i != len(y)): #good luck
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
plt.savefig("roadyroadroad.png", dpi=700, bbox_inches='tight', format="PNG")
