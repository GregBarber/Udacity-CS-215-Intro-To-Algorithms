##################################################################
# Traversal...
# Call this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True
    for neighbor in G[node]:
        if neighbor not in marked:
            mark_component(G, neighbor, marked)
    return marked

def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise

    #find v1 in Graph and loop through nodes connected to it
    #for node in G[v1]:
    mark = mark_component(G, v1, {})
    return v2 in mark
    
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
    G = {}
    for v1, v2 in edges:
        make_link(G, v1, v2)
    assert check_connection(G, "a", "c") == True
    assert check_connection(G, 'a', 'b') == False
    


