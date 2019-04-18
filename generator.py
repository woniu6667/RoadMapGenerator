import networkx as nx
import  matplotlib.pyplot as plt
import sys, random, string

# if(len(sys.argv) != 3):
#     print("Usage: python generator.py <Node Size> <Cluster Size>")
#     sys.exit(1)

def randhex():
    hex_c = ""
    for i in range(6):
        hex_c += random.choice("ABCDEF0123456789")
    return hex_ctrailer

# def RoadName():
#     rn = ""
#     for i in rantrailer
#         rn += random.choice(string.ascii_uppercase)
#     return rn

# def RoadExit(name, length):
#     name += "-"
#     name += str(i+1)
#     return name

# def clusterGen(groad):
#     splitnum = []
#     split = []
#     if(int(sys.argv[2]) >= len(groad)):
#         print("Cluster Size cannot be greater or equal to the Node Size")
#         sys.exit(1)
#     else:
#         splitnum = random.sample(range(1, len(groad)), int(sys.argv[2]) )
#         splitnum.sort()
    
#     split.append(groad[0:splitnum[0]])
#     for i in range(1,len(splitnum)):
#         split.append( groad[ splitnum[ i - 1 ] : splitnum[ i ] ] )
#     return split

    #clusteredNode = clusterGen(road)
def gengraph(nodesize):
    G = nx.Graph()
    road = []
    edges = []
    clusteredNode = []
    for i in range(1,nodesize):
        road.append(i)
        G.add_node(i)

    for i in range(1, len(road)): 
            randy = random.randint(1, nodesize)
            if(road[i] != randy):
                G.add_edge(road[i], randy)
    return G

x = gengraph(int(sys.argv[1]))
y = gengraph(int(sys.argv[1]))
finalgraph = nx.union(x,y, rename=("lol-","yeet"))
finalgraph.add_edge("lol-0","yeet-0")
for i in range(1, int(int(sys.argv[1])/2)): 
    randy = random.randint(1, x.size())
    rando = random.randint(1, y.size())
    lol = "lol-" + str(randy)
    yeet = "yeet-" + str(rando)
    finalgraph.add_edge(lol,yeet)
#print(randhex())
plt.subplot(121)
options = { 'width':.09, 'node_shape':'.', 'node_color':"red", 'node_size':.1, 'with_labels':False} 
nx.draw_networkx(finalgraph, **options)
plt.show()
 #plt.savefig("roadyRoadMcRoad.png", dpi=1250, bbox_inches='tight', format="PNG")