
from Lesson5Comics import test_comic_me

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
    (books, characters) = test_comic_me()

    for primary in characters:
        for secondary in characters[primary]:
            make_link_value(weighted_G, primary, secondary, 1.0/characters[primary][secondary])
            make_link_value(G, primary, secondary, 1.0)
    asfd=9
