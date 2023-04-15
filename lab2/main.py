#from graph_draw import *
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def is_degree_sequence(sequence):
    while len(sequence) > 0:
        if(all(v == 0 for v in sequence)):
            return True
        
        sequence = sorted(sequence, reverse=True)

        if len(sequence) <= sequence[0] or sequence[0] < 0:
            return False

        for i in range(1, sequence[0] + 1):
            sequence[i] -= 1

        sequence = sequence[1:]
    return True

def create_graph(sequence):
    n = len(sequence)
    edges = []
    
    # Sort the degree sequence in descending order
    degrees_sorted = sorted(sequence, reverse=True)
    
    # Construct the graph
    for i in range(n):
        for j in range(i+1, n):
            # Check if the current vertex can still be connected to the remaining vertices
            if degrees_sorted[i] > 0 and degrees_sorted[j] > 0:
                edges.append((i+1, j+1))
                degrees_sorted[i] -= 1
                degrees_sorted[j] -= 1
    
    # Check if the degree sequence is valid
    if sum(degrees_sorted) > 0:
        return None
    print(edges)
    return edges

def draw_visible_circle_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    
    # Draw the graph on a visible circle
    pos = nx.circular_layout(G, scale=2)
    nx.draw(G, pos, with_labels=True)
    
    # Set the axis limits to make the circle visible
    ax = plt.gca()
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    
    # Show the graph
    plt.show()


def swap_edges(G):
    # Select two random edges to swap
    edge1 = random.choice(list(G.edges()))
    edge2 = random.choice(list(G.edges()))
    
    # Check if the selected edges are not the same or parallel
    while edge1 == edge2 or edge1[0] == edge2[0] or edge1[1] == edge2[1]:
        edge2 = random.choice(list(G.edges()))
    
    # Check if swapping the edges would change the degrees of vertices
    if len(set([edge1[0], edge1[1], edge2[0], edge2[1]])) != 4:
        return G
    
    # Swap the edges
    G.remove_edges_from([edge1, edge2])
    G.add_edges_from([(edge1[0], edge2[1]), (edge2[0], edge1[1])])
    
    return G

def find_degree_sequence(vertices, edges):
    degree_sequence = []
    for v in vertices:
        degree = sum(1 for e in edges if v in e)
        degree_sequence.append(degree)
    return degree_sequence

def degree_sequence(G):
    degree_sequence = []
    for v in G:
        degree_sequence.append(len(G[v]))
    return degree_sequence


def draw_randomized_circle_graph(edges, num_swaps_):
    G = nx.Graph()
    G.add_edges_from(edges)
    
    # Draw the original graph on a visible circle
    pos = nx.circular_layout(G, scale=2)
    
    # Set the axis limits to make the circle visible
    ax = plt.gca()
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    
    # Randomize the graph while keeping the degrees of vertices fixed
    num_swaps = num_swaps_  # set the number of swaps to perform
    for i in range(num_swaps):
        G_new = swap_edges(G.copy())
        if(np.array_equal(degree_sequence(G), degree_sequence(G_new))):
            G = G_new
    
    # Draw the randomized graph on the same circle
    nx.draw(G, pos, with_labels=True, edge_color='r')
    
    # Show the graph
    plt.show()



def zadanie1():
    print('\nZadanie 1')
    print('ok' if not is_degree_sequence([1, 2, 3, 4, 4]) else 'not ok')
    print('ok' if is_degree_sequence([1, 2, 2, 3, 4, 4]) else 'not ok')
    print('ok' if not is_degree_sequence([1, 2, 2, 3, 3, 4]) else 'not ok')
    print('ok' if is_degree_sequence(
        [1, 2, 2, 3, 4, 4, 2, 2, 2, 3, 1, 5, 7, 4]) else 'not ok')
    print('ok' if not is_degree_sequence(
        [1, 2, 2, 3, 4, 4, 2, 2, 2, 3, 1, 5, 7, 5]) else 'not ok')
    print('ok' if not is_degree_sequence(
        [1, 2, 2, 3, 4, 4, 2, 2, 2, 3, 1, 5, 7, 14]) else 'not ok')

    print('ok' if is_degree_sequence([2,2,4,4,4,4,4]) else 'not ok')
    
    print('ok' if is_degree_sequence([2,3,4,4,4,4,4]) else 'not ok')
    g = create_graph([1,3,2,3,2,4,1])
    draw_visible_circle_graph(g)

def zadanie2():
    print('\nZadanie 2')
    edges = create_graph([1,3,2,3,2,4,1])
    draw_visible_circle_graph(edges)
    draw_randomized_circle_graph(edges, 5)

def find_connected_components(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    nr = 0  # Number of connected components
    comp = {}  # Dictionary to store the component number for each vertex
    visited = set()  # Set to keep track of visited vertices
    largest_comp_size = 0  # Size of the largest connected component
    largest_comp_nr = -1  # Component number of the largest connected component

    def dfs(vertex):
        nonlocal nr, largest_comp_size, largest_comp_nr
        visited.add(vertex)
        comp[vertex] = nr
        comp_size = 1
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                comp_size += dfs(neighbor)
        if comp_size > largest_comp_size:
            largest_comp_size = comp_size
            largest_comp_nr = nr
        return comp_size

    # Initialize comp dictionary with -1 for all vertices
    for vertex in graph:
        comp[vertex] = -1

    # Perform DFS on unvisited vertices
    for vertex in graph:
        if vertex not in visited:
            nr += 1
            dfs(vertex)

    print("Connected components: ", comp)
    print("Largest connected component: Component Number = {}, Size = {}".format(largest_comp_nr, largest_comp_size))

def zadanie3():
    print('\nZadanie 2')
    edges1 = create_graph([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2])
    edges2 = create_graph([1,3,2,3,2,4,1])
    find_connected_components(edges1)
    find_connected_components(edges2)

def zadanie4():
    print('\nZadanie 2')
    edges1 = create_graph([4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2])
    edges2 = create_graph([1,3,2,3,2,4,1])

def main():
    #zadanie1()
    #zadanie2()
    #zadanie3()
    zadanie4()


if __name__ == '__main__':
    main()
