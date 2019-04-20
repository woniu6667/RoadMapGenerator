
import networkx as nx
import  matplotlib.pyplot as plt
import sys
f = open(sys.argv[1],"r")
x = f.read()
y = x.split()
# even numbers = node
# odd number = edge connections

if(len(sys.argv) != 2):
    print("Usage: python roadmap.py <road file>")
    sys.exit(1)

filename = sys.argv[1].split(".")[0]
filename += ".png"
G = nx.dodecahedral_graph()
i = 0
while(i != len(y)): #good luck
    if( i % 2 == 0):
        G.add_node(y[i])
    else:
        G.add_edge(y[i-1], y[i])
    i+=1

#pos = nx.complete_graph(G)
#plt.subplot(121)
nx.draw_networkx(G, alpha=.5, width=.09, node_shape = ".", node_color="red", node_size=.25, with_labels=False)
#plt.show()
plt.savefig(filename, dpi=1250, bbox_inches='tight', format="PNG")