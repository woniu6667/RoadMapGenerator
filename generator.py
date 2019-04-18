import networkx as nx
import  matplotlib.pyplot as plt
import sys, random

G = nx.Graph()
road = []

for i in range(1,int(sys.argv[1])):
    road.append(i)
    G.add_node(i)
edges = []

for i in range(1, len(road)): 
        randy = random.randint(1, len(road)+1)
        if(road[i] != randy):
            G.add_edge(road[i], randy)

plt.subplot(121)
options = { 'width':.09, 'node_shape':'.', 'node_color':"red", 'node_size':.1, 'with_labels':False} 
nx.draw_networkx(G, **options)
#plt.show()
plt.savefig("roadyRoadMcRoad.png", dpi=1250, bbox_inches='tight', format="PNG")