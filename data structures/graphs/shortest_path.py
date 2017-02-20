# -*- coding: utf-8 -*-
# !/usr/bin/env python


import queue

## Shortest paths
# Floyd Warshall: distances to self is wrong (2 or 4?)
# Add comments

## Unweighted graphs
def distancesFrom(g, s):
    """ 
        Returns the list of distances using a bfs.
    
        Input:
            Graph as an adjacency list
    """
    
    V = []                                                                      # List of visited vertices
    D = [0 for k in range(len(g))]                                              # Distances
    Q = queue.Queue()
    Q.put((s,0))
    
    while not Q.empty():
        u, d = Q.get()
        
        if u not in V:
            V += [u]
            for v in g[u]:
                Q.put( (v,d+1) )
            D[u] = d
    return D

def pathFrom(g, s):
    """
        Returns the path to go to a vertex using a bfs
        
        Input:
            Graph as an adjacency list
        
        Returns:
            List l such as l[i] is the list of vertices to use to go to i from s
    """
    
    V = []                                                                      # List of visited vertices
    P = [None for k in range(len(g))]                                           # List of paths
    Q = queue.Queue()
    Q.put((s,[]))
    
    while not Q.empty():
        u, p = Q.get()
        
        if u not in V:
            V += [u]
            for v in g[u]:
                Q.put( (v,p+[u]) )
            P[u] = p+[u]
    return P

## Weighted graphs: dijkstra
## Weighted graphs: Floyd Warshall
## Waighted graphs: A star
def listPaths_uul(g, sourceNode):
    """ 
    Returns the list of the shortest path from sourceNode to all ather accessible nodes in g.
    Breadth First Search used.
    
    Arguments: 
        arg1: an unweighted graph implemented by adjacency list. 
        arg2: sourceNode. 
    
    Returns:
        List
    
    Todo:
        Comment variable use
        Comment
    """
    
    q = Queue()
    paths = [[] for k in range(g.getOrder())]
    
    q.put((sourceNode,[]))

    while not q.empty():
        (current_vertice, path) = q.get()

        if paths[current_vertice] == []:
            path = path + [current_vertice]
            paths[current_vertice] = path
            for neighbor in g.getNeighbors(current_vertice):
                q.put((neighbor, path))
    return paths



def dijkstra(g, source):
    """
    Returns the list of distances and the list of paths
    
    Todo:
        Add the paths
    """
    
    global infinity
    order = g.getOrder()
    
    distances = [ infinity for k in range(order) ]
    predecessors = [None for k in range(order) ]
    
    visited = []
    q = priorityQueue()
    
    # To get the same result as FW 
    # for neighbor in g.getNeighbors(source):
    #     if g.getWeight(source, neighbor) < distances[source]:
    #         distances[source] = 2* g.getWeight(source, neighbor)
    #         predecessors[source] = neighbor
    
    q.put((0,source))
    
    while not q.empty():
        cur_distance, cur_vertex = q.get()
        visited.append(cur_vertex)
        
        for neighbor in g.getNeighbors(cur_vertex):
            if neighbor not in visited:
                new_distance = cur_distance + g.getWeight(cur_vertex,neighbor)
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = cur_vertex
                    q.put((new_distance, neighbor))
    
    return distances, predecessors



def floydWarshall(g):
    """ Floyd Warshall's algorithm. """
    global infinity
    order = g.getOrder()

    # Create the adjacency matrix of the graph
    distances = [ [infinity for j in range(order)] for i in range(order) ]
    nextVertex = [[None for j in range(order)] for i in range(order) ]
    

    # Initialise adjacency matrix and the nextVertex matrix
    for i in range(order):
        for j in range(order):
            if j in g.getNeighbors(i):
                distances[i][j] = g.getWeight(i,j)
                nextVertex[i][j] = j

    # Floyd-Warshall
    for k in range(order):
        for i in range(order):
            for j in range(order):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    nextVertex[i][j] = nextVertex[i][k]
    
    return distances, nextVertex


## Tests
