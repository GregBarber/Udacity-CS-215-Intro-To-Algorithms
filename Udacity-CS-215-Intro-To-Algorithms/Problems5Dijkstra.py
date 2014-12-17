#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
# 

def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node

def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    index_node = {0:v}
    node_index = {v:0}
    heap = [0]
    final_dist = {}
    while len(dist_so_far)>0:
        #w = shortest_dist_node(dist_so_far)
        w = index_node[0] #dist_so_far[0]
        
        # lock it down!
       # final_dist[w] = dist_so_far[0]
        final_dist[w]=remove_min(heap, index_node, node_index)
        del dist_so_far[w]
        #del node_index[w]
        #del index_node[0]

        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    #add it to the heap
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    index = add_to_heap(heap, dist_so_far[x])
                    index_node[index] = x
                    node_index[x] = index
                    up_heapify(heap, len(heap)-1, index_node, node_index)
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    heap[node_index[x]] = dist_so_far[x]
                    up_heapify(heap, node_index[x], index_node, node_index)
    return final_dist

############
# 
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G

def test_Dijkstra():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

    #upheap
#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

def up_heapify(L, i, index_node, node_index):
    # your code here
    if i == 0: return

    if L[i] < L[parent(i)]: 
        #value needs to move up, swap L[i]into partent
        tmp = L[parent(i)]
        L[parent(i)] = L[i]
        L[i] = tmp
        swap_index(i, parent(i), index_node, node_index)
        up_heapify(L, parent(i), index_node, node_index)

    return

def down_heapify(L, i, index_node, node_index):
    # If i is a leaf, heap property holds
    if is_leaf(L, i): 
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
            swap_index(i, left_child(i), index_node, node_index)
        return
    # If i has two children...
    # check heap property
    if min(L[left_child(i)], L[right_child(i)]) >= L[i]: 
        return
    # If it fails, see which child is the smaller
    # and swap i's value into that child
    # Afterwards, recurse into that child, which might violate
    if L[left_child(i)] < L[right_child(i)]:
        # Swap into left child
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        swap_index(i, left_child(i), index_node, node_index)
        down_heapify(L, left_child(i), index_node, node_index)
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        swap_index(i, right_child(i), index_node, node_index)
        down_heapify(L, right_child(i), index_node, node_index)
        return

def parent(i): 
    return int((i-1)/2)
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def remove_min(heap, index_node, node_index):
    val = heap[0]
    if len(heap) == 1:
        del heap[0]
        del node_index[index_node[0]]
        del index_node[0]
        return val

    last_leaf_index = len(heap)-1
    last_leaf = heap[last_leaf_index]
    heap[0] = last_leaf
    del heap[len(heap)-1]

    swap_index(0, last_leaf_index, index_node, node_index)
    del node_index[index_node[last_leaf_index]]

    #index_node[0] = index_node[last_leaf_index]
    del index_node[last_leaf_index]

    down_heapify(heap, 0, index_node, node_index)
    return val

def add_to_heap(heap, value):
    heap.append(value)
    return len(heap)-1
    
def swap_index(index1, index2, index_node, node_index):
    node1 = index_node[index1]
    node2 = index_node[index2]
    tmpI1 = node_index[node1]
    node_index[node1] = node_index[node2]
    node_index[node2] = tmpI1

    index_node[index1] = node2
    index_node[index2] = node1
