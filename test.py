import networkx as nx
import  matplotlib.pyplot as plt
import sys, random, string

color_map =[]
name = []
colorlist = []

def randhex():
    hex_c = "#"
    for i in range(6):
        hex_c += random.choice("ABCDEF0123456789")
    return hex_c

def NetworkName():
    rn = ""
    for i in range(2):
        rn += random.choice(string.ascii_uppercase)
    rn + "-"
    return rn

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

def clusters(num):
    x = []
    nodesize = int(sys.argv[2])
    for i in range(num):
        generateGraph = gengraph(nodesize)
        x.append(generateGraph)
        color_map.append(randhex())
    return x

def setEdges(graph, name, finalgraph):
    for j in range(int(sys.argv[3])):
        for i in range(1,len(graph)):
            randoTheRock = random.randint(1, len(graph[i]))
            randyJohnson = random.randint(1, len(graph[i-1]))
            randoName = name[i] + str(randoTheRock)
            randyName = name[i-1] + str(randyJohnson)
            finalgraph.add_edge(randoName,randyName)

def finalConnection(graph):
    finalgraph = nx.Graph()
    for i in range(len(graph)):
        name.append(NetworkName())
    finalgraph = nx.union_all(graph, rename=(name))
    setEdges(graph, name, finalgraph)
    return finalgraph

if(len(sys.argv) != 4):
    print("Usage: python test.py <Number of Clusters> <Number of Nodes> <Number of Cluster Edges>")
    sys.exit(1)


clustersize = int(sys.argv[1])
Graphy = clusters(clustersize)
finalgraph = finalConnection(Graphy)

for node in finalgraph:
    for i in range(len(name)):
        if(name[i] in node):
            colorlist.append(color_map[i])


plt.subplot(121)
options = { 'width':.09,'font_size':2,'node_size':2, 'with_labels':True} 
nx.draw_networkx(finalgraph, node_color=colorlist, **options)
#plt.show()
plt.savefig("roadyRoadMcRoad.png", dpi=1250, bbox_inches='tight', format="PNG")
