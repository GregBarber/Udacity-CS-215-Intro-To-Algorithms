def find_eulerian_tour(graph):
    # your code here
    tour =[]
    
    for points in list(graph):
        if points[0] not in tour:
            tour.append(points[0])
        if points[1] not in tour:
            tour.append(points[1])
    return tour