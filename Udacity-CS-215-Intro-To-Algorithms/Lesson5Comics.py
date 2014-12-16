import csv
import time

def make_link_count(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    if node2 not in (G[node1]):
        (G[node1])[node2] = 1
    else:
        (G[node1])[node2] += 1
    if node2 not in G:
        G[node2] = {}
    if node1 not in (G[node2]):
        (G[node2])[node1] = 1
    else:
        (G[node2])[node1] += 1
    return G

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test_comic_me():
    books = {} # dictionary with book titles as key and values are a list of characters in that book
    characters = {} # dictionary with key as the character and value is a dictionary with key as other characters and value is the count of the times they appear together
    strongest_link = [None, None, 0] # will maintain the two characters names and teh count of times they appear together

    # Read an undirected graph in CSV format. Each line is an edge
    time1 = time.time()
    data = csv.reader(open('fileComicLesson5'), delimiter='\t')
    
    for (name, book) in data: 
        if book not in books:
            books[book] = [name]
        else:
            books[book].append(name)

        if name not in characters:
            characters[name] = {}

        for coactor in books[book]:
            if coactor != name:
                if coactor not in characters[name]:
                    characters[name][coactor] = 1
                else:
                    characters[name][coactor] += 1

                    if characters[name][coactor] > strongest_link[2]:
                        strongest_link = [name, coactor, characters[name][coactor]]

    time2 = time.time()
    print('Strongest link : ' + strongest_link[0] + ' ' + strongest_link[1] + ' ' + str(strongest_link[2]))
    print("total time =  " + str(time2-time1))

    return books, characters

def test_comic():
    time1 = time.time()
    data = csv.reader(open('fileComicLesson5'), delimiter='\t')
    Graph = {}
    G2={}
    books = {}
    characters = []
    strongest_link = [None, None, 0]
    for (name, book) in data:
        make_link(Graph, name, book.rstrip('\n'))
            
            
        if name not in characters:
            characters.append(name)
            '''
        if book not in books:
            books[book] = [name]
        else:
            books[book].append(name)
            '''
    time2 = time.time()
    print("read time = " + str(time2-time1))


    time1 = time.time()
    for char1 in characters:
        for book in Graph[char1]:
            for char2 in Graph[book]:
                #if char1 > char2:
                    make_link_count(G2, char1, char2)

    time2 = time.time()
    print("strength time = " + str(time2-time1))




import time
import csv
from collections import defaultdict

def highest_strength(graph):
    return max((s, x, y) 
               for x, links in graph.items() 
               for y, s in links.items())

def make_link(G, node1, node2):
    if node1 not in G: G[node1] = defaultdict(int)
    G[node1][node2] += 1     
    if node2 not in G: G[node2] = defaultdict(int)
    G[node2][node1] += 1

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    comics = {}
    for (character, comic_book) in tsv:
        if comic_book not in comics:
            comics[comic_book] = []
        comics[comic_book].append(character)
    G = {}
    for comic_book in comics:
        i = 1
        for character in comics[comic_book]:
            for current in comics[comic_book][i:]:
                make_link(G, character, current)
            i += 1        
    return G

def test_comic3():
    start_time = time.time()
    G = read_graph('fileComicLesson5')
    print("read time:", time.time() - start_time)
    start_time = time.time()
    print(highest_strength(G))
    print("strength time:", time.time() - start_time)
            