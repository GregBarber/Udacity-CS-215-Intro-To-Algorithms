#            animal       speed   weight lifespan brain
#                          (mph)   (kg)  (years) mass (g)
animals = [("dog",          46,   35,     13,  280    ),
           ("elephant",     30, 3500,     50, 6250    ),
           ("frog",          5,    0.5,    8,    3    ),
           ("hippopotamus", 45, 1600,     45,  573    ),
           ("horse",        40,  385,     30, 642     ),
           ("human",        27,   80,     78, 2000    ),
           ("lion",         50,  250,     30,  454    ),
           ("mouse",         8,    0.025,  2,    0.625),
           ("rabbit",       25,    4,     12,   40    ), 
           ("shark",        26,  230,     20,   92    ),
           ("sparrow",      16,    0.024,  7,    2    )]

def importance_rank(items, weights):
    names = []
    for item in items:
        names.append(item[0])
    # get the list of animal names
    scores = [sum([a*b for (a,b) in zip(item[1:], weights)]) for item in items]  # get the list of overall scores for each animal
    results = zip(scores,names) # make a list of tuple
    res2 = sorted(results) # sort the tuple based on the score
    return res2

def animal():
    answer = importance_rank(animals, (1,.01,10,300))

    for i in range(len(answer)):
        print(i, answer[i][1], "(", answer[i][0], ")")



#
# Write `max`
# 

def max(L):
    # return the maximum value in L
    m=L[0]
    for i in range(1,len(L)):
        if L[i] > m: m=L[i]
    return m

def test_max():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)


def names():
    file = open('yob1995.txt')
    data = []
    highest = ['', 0]
    second = ['', 0]

    for line in file:
        [name, sex, count] = line.split(',')
        if sex == 'F':
            count = int(count.rstrip('\n'))
            if count > highest[1]:
                second[0] = highest[0]
                second[1] = highest[1]
                highest[0] = name
                highest[1] = count
            elif count > second[1]:
                second[0] = name
                second[1] = count

    return second[0]



#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    P = []
    p = []
    # your code here
    for val in L:
        if val < v:
           p.append(val)
        elif val > v:
           P.append(val)
    p.append(v)
    return p.append(P)

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos


#####################################
#heap
#
# Implement remove_min
#

def remove_min(L):
    # your code here

    last_leaf = L[len(L)-1]
    L[0] = last_leaf
    L = L[0:len(L)-1]
    down_heapify(L, 0)
    return L

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children
def down_heapify(L, i):
    # If i is a leaf, heap property holds
    if is_leaf(L, i): 
        return
    # If i has one child...
    if one_child(L, i):
        # check heap property
        if L[i] > L[left_child(i)]:
            # If it fails, swap, fixing i and its child (a leaf)
            (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
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
        down_heapify(L, left_child(i))
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i))
        return

#########
# Testing Code
#

# build_heap
def build_heap(L):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L

def test_heap():
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9] #range(10)
    L = build_heap(L)
    L = remove_min(L)
    # now, the new minimum should be 1
    assert L[0] == 1
