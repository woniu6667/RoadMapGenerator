
import networkx as nx
import  matplotlib.pyplot as plt
f = open("road-usroads.mtx","r")
x = f.read()
y = x.split()
G = nx.Graph()

i = 0
print("graph size = " + str(len(y)))
while(i != 5000 ):# len(y)):
    if( i % 2 == 0):
        G.add_node(y[i])
    else:
        G.add_edge(y[i-1], y[i])
    i+=1
plt.subplot(121)
nx.draw_networkx(G, width=.09, node_color="red", node_size=.01, with_labels=False)
plt.savefig("roadyroadroad.png", dpi=2000, bbox_inches='tight', format="PNG")