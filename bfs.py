""" Simple bfs code
"""
import networkx as nx

def bfs(G,s):
    """
    Input:
    G: networkx graph
    s: source node

    Output:
    L2: Labels for all nodes in graph, 0=unreachable from source, 1=reachable
    L3: Shortest distance from source to nodes in graph
    """

    L1 = list(G.nodes) #Assumes nodes are numbered from 0 to N-1
    L2 = [0 for l in L1]
    L3 = [-1000 for l in L1]

    Q=[]
    Q.append(s)
    L2[s]=1
    L3[s]=0

    while len(Q)>0:
        x = Q.pop(0)
        for v in G.adj[x]:
            if L2[v]==0:
                Q.append(v)
                L2[v]=1
                L3[v]=1+L3[x]
            print("v=",v)
            print("Q=",Q)
    return L2,L3

if __name__=='__main__':
    #create a random graph and make it networkx graph
    e=[[1,2,1],[1,5,1],[2,3,1],[2,5,1],[5,4,1],[3,4,1],[4,6,1]]
    G = nx.Graph()
    G.add_weighted_edges_from(e)
    source = 1
    L2,L3 = bfs(G,source)
    print('reachable',L1, 'Not reachable',L2)
