"""Basic Dijkstra algorithm implemented using dictionaries. Generates dictionary of shortest distances to all other nodes 
given list of nodes and weights in the following format [[node1,node2,weight],[node3,node5,weight]..... ]
"""
import networkx as nx

def dijkstra(G,s):
    """Find shortest distances to s in weighted graph, G"""

    #Initialize dictionaries
    dinit = 10**6
    Edict = {} #Explored nodes
    Udict = {} #Unexplored nodes

    for n in G.nodes():
        Udict[n] = dinit
    Udict[s]=0

    #Main search
    while len(Udict)>0:
        #Find node with min d in Udict and move to Edict
        dmin = dinit
        for n,w in Udict.items():
            if w<dmin:
                dmin=w
                nmin=n
        Edict[nmin] = Udict.pop(nmin)
        print("moved node", nmin)

        #Update provisional distances for unexplored neighbors of nmin
        for n,w in G.adj[nmin].items():

            if n in Edict:
                pass
            elif n in Udict:
                dcomp = dmin + w['weight']
                if dcomp<Udict[n]:
                    Udict[n]=dcomp
            else:
                dcomp = dmin + w['weight']
                Udict[n] = dcomp

    return Edict


if __name__=='__main__':
    #create a random graph and make it networkx graph, generates dictionary of shortest distances to all other nodes
    e=[[1,2,3],[1,5,2],[2,3,1],[2,5,1],[5,4,5],[3,4,2],[4,6,1]]
    G = nx.Graph()
    G.add_weighted_edges_from(e)
    source = 1
    Edict = dijkstra(G,source)
    print("source=%d" %(source))
