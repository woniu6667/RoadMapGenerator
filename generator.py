import networkx as nx
import  matplotlib.pyplot as plt
import sys, random, string

if(len(sys.argv) != 3):
    print("Usage: python generator.py <Node Size> <Cluster Size>")
    sys.exit(1)

def randhex():
    hex_c = ""
    for i in range(7):
        hex_c += random.choice("ABCDEF0123456789")
    return hex_c

def RoadName():
    rn = ""
    for i in range(2):
        rn += random.choice(string.ascii_uppercase)
    return rn

def RoadExit(name, length):
    name += "-"
    name += str(i+1)
    return name

def clusterGen(groad):
    splitnum = []
    split = []
    if(int(sys.argv[2]) >= len(groad)):
        print("Cluster Size cannot be greater or equal to the Node Size")
        sys.exit(1)
    else:
        splitnum = random.sample(range(1, len(groad)), int(sys.argv[2]) )
        splitnum.sort()
    
    split.append(groad[0:splitnum[0]])
    for i in range(1,len(splitnum)):
        split.append( groad[ splitnum[ i - 1 ] : splitnum[ i ] ] )
    return split

G = nx.Graph()
road = []
edges = []
clusteredNode = []
for i in range(1,int(sys.argv[1])):
     road.append(i)
     G.add_node(i)
clusteredNode = clusterGen(road)



for i in range(1, len(road)): 
         randy = random.randint(1, len(road)+1)
         if(road[i] != randy):
             G.add_edge(road[i], randy)

print(randhex())
 #plt.subplot(121)
 #options = { 'width':.09, 'node_shape':'.', 'node_color':"red", 'node_size':.1, 'with_labels':False} 
 #nx.draw_networkx(G, **options)
 #plt.show()
 #plt.savefig("roadyRoadMcRoad.png", dpi=1250, bbox_inches='tight', format="PNG")