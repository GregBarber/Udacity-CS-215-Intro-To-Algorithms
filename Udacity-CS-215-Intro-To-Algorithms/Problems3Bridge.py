# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

# So far, we've represented graphs 
# as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
# 
# In order to represent a spanning tree
# we need to create two classes of edges
# we'll refer to them as "green" and "red"
# for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1}, 
#      'b': {'a': 1, 'd': 1}, 
#      'c': {'a': 1, 'd': 1}, 
#      'd': {'c': 1, 'b': 1, 'e': 1}, 
#      'e': {'d': 1, 'g': 1, 'f': 1}, 
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1} 
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'}, 
#      'b': {'a': 'green', 'd': 'red'}, 
#      'c': {'a': 'green', 'd': 'green'}, 
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'} 
#      }
#       

def create_rooted_spanning_tree(G, root):
    # use DFS from the root to add edges and nodes
    # to the tree.  The first time we see a node
    # the edge is green, but after that its red
    open_list = [root]
    S = {root:{}}
    while len(open_list) > 0:
        node = open_list.pop()
        neighbors = G[node]
        for n in neighbors:
            if n not in S:
                # we haven't seen this node, so
                # need to use a green edge to connect
                # it
                make_color_link(S, node, n, 'green')
                open_list.append(n)
            else:
                # we have seen this node,
                # but, first make sure that 
                # don't already have the edge
                # in S
                if node not in S[n]:
                    make_color_link(S, node, n, 'red')
    return S

def create_rooted_spanning_tree2(G, root):
    S = {}
    # your code here
    visited = {}
    open_list = [root]
    #go through the nodes in G
    while len(open_list)>0:

        node = open_list[0]
        edges = G[node]
        for neighbor in edges:
            if neighbor not in visited:
                #if a connection exists at all between nodes in S the new connection is red
                if path_exists(S, node, neighbor):
                    make_color_link(S, node, neighbor, 'Red')
                else:
                    make_color_link(S, node, neighbor, 'Green')
                
                open_list.append(neighbor)

        del open_list[0]
        visited[node] = True
    return S

def path_exists(S, node1, node2):
    if len(S.keys()) < 1: return False

    open_list = [node1]
    visited = {}
    while len(open_list)>0:
        for neighbor in S[open_list[0]]:
            if neighbor not in visited:
                if neighbor == node2: return True
                else: open_list.append(neighbor)

        visited[open_list[0]] = True
        del open_list[0]
    return False

def make_color_link(G, node1, node2, color):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = color
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = color
    return G

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    po = {}

    depth = calc_depth(S, root)
    check_node(S, root, depth, po)
    
    return po

def check_node(S, node, depth, po):

    for nodes in get_children(S, depth, node):
        if nodes not in po:
            check_node(S, nodes, depth, po)
        
    if len(po) == 0: 
        po[node] = 1
    else:
        po[node] = max(po.values()) + 1

def get_children(S, depth, node):
    children = []
    linked_nodes = S[node]
    linked_nodes = {key: value for key, value in linked_nodes.items() if value != 'red'}
    for l in linked_nodes:
        if depth[l] > depth[node]: 
            children.append(l)

    children.sort()
    return children

def get_children_all(S, depth, node):
    children = []
    linked_nodes = S[node]
    #linked_nodes = {key: value for key, value in linked_nodes.items() if value != 'red'}
    for l in linked_nodes:
        if depth[l] > depth[node]: 
            children.append(l)

    children.sort()
    return children

def calc_depth(S, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while  len(open_list) > 0:
        current = open_list.pop()

        for neighbor in S[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return distance_from_start

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    #green edges only

    # num of descendents = sum of the number of descendents of children
    descendents = {}
    depth = calc_depth(S, root)
    descendents = _descendents(S, root, descendents, depth)


    return descendents

def _descendents(S, root, descendents, depth):
    children = get_children(S, depth, root)

    d = 1
    for child in children:
        if child not in descendents:
            _descendents(S, child, descendents, depth)
            d += descendents[child]

    descendents[root] = d

    return descendents

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    lpo = {}
    depth = calc_depth(S, root)
    lpo = _lpo(S, root, po, depth)


    return lpo

def _lpo(S, root, po, depth):
    children = get_children_all(S, depth, root)

    for child in children:
        _lpo(S, child, po, depth)


def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    pass

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
#################

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    pass

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]


def test_bridge():
#    test_create_rooted_spanning_tree()
    test_post_order()
    test_number_of_descendants()
    test_lowest_post_order()
    test_highest_post_order()
    test_bridge_edges()
