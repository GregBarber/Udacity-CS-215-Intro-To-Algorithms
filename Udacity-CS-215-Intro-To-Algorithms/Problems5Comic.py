
from Lesson5Comics import test_comic_me
from Problems5Dijkstra import dijkstra

def make_link_value(G, node1, node2, value):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = value
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = value
    return G

def test_comic_weighted():
    weighted_G = {}
    G = {}
    (books, characters) = test_comic_me()

    for primary in characters:
        for secondary in characters[primary]:
            make_link_value(weighted_G, primary, secondary, 1.0/characters[primary][secondary])
            make_link_value(G, primary, secondary, 1.0)
    asfd=9

    weighted_distance = []
    distance = []
    
    i=0
    count = 0
    total = 0
    for character in G:
        distance = dijkstra(G, character)
        weighted_distance = dijkstra(weighted_G, character)

        for link in distance.keys():
            weighted = weighted_distance[link]
            unweighted = distance[link]

            total += 1
            if unweighted != weighted: count += 1
        

    print('Total: ' + str(total) + ' and different: ' + str(count))
            
    '''
            i+=1

    i = 0
    for character in weighted_G:
        weighted_distance = dijkstra(weighted_G, character)
        i+=1
        
    
    for i in range(len(distance)-1):
        if distance[i] is not weighted_distance[i]:
            count += 1
           '''
