# -*- coding: utf-8 -*-
"""BFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PkJlOmR9fxA3S7ym0-tOiRj5ZR87mjM9
"""

GRAPH = {
    'Delhi': {'Jaipur': 280, 'Agra': 210, 'Lucknow': 400},
    'Agra': {'Delhi': 210, 'Gwalior': 120},
    'Gwalior': {'Agra': 120, 'Bhopal': 400},
    'Jaipur': {'Delhi': 280, 'Jodhpur': 330, 'Udaipur': 410},
    'Lucknow': {'Delhi': 400, 'Kanpur': 80},
    'Kanpur': {'Lucknow': 80, 'Allahabad': 190},
    'Allahabad': {'Kanpur': 190, 'Varanasi': 120},
    'Varanasi': {'Allahabad': 120, 'Patna': 250},
    'Patna': {'Varanasi': 250, 'Ranchi': 300, 'Kolkata': 560},
    'Ranchi': {'Patna': 300, 'Jamshedpur': 130},
    'Jamshedpur': {'Ranchi': 130, 'Kolkata': 280},
    'Kolkata': {'Patna': 560, 'Jamshedpur': 280, 'Bhubaneswar': 440},
    'Bhubaneswar': {'Kolkata': 440, 'Cuttack': 30, 'Puri': 60},
    'Puri': {'Bhubaneswar': 60},
    'Cuttack': {'Bhubaneswar': 30},
    'Jodhpur': {'Jaipur': 330, 'Udaipur': 250},
    'Udaipur': {'Jaipur': 410, 'Jodhpur': 250, 'Ahmedabad': 260},
    'Ahmedabad': {'Udaipur': 260, 'Surat': 280},
    'Surat': {'Ahmedabad': 280, 'Mumbai': 280},
    'Mumbai': {'Surat': 280, 'Pune': 150},
    'Pune': {'Mumbai': 150}
}

def bestfirst(source, destination):
    """Optimal path from source to destination using straight line distance heuristic

    :param source: Source city name
    :param destination: Destination city name
    :returns: Heuristic value, cost and path for optimal traversal
    """
    # HERE THE STRAIGHT LINE DISTANCE VALUES ARE IN REFERENCE TO KOLKATA AS THE DESTINATION
    straight_line = {
        'Delhi': 1400, 'Jaipur': 1200, 'Agra': 1300, 'Lucknow': 1100, 'Kanpur': 1050,
        'Allahabad': 900, 'Varanasi': 850, 'Patna': 600, 'Gwalior': 1200, 'Bhopal': 1000,
        'Ranchi': 500, 'Jamshedpur': 300, 'Kolkata': 0, 'Bhubaneswar': 450, 'Puri': 510,
        'Cuttack': 440, 'Jodhpur': 1400, 'Udaipur': 1300, 'Ahmedabad': 1200, 'Surat': 1250,
        'Mumbai': 1600, 'Pune': 1550
    }

    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]

    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic = straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node]))

def main():
    """Main function"""
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    goal = input().strip()
    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nBest First Search PATH:')
        heuristic, cost, optimal_path = bestfirst(source, goal)
        print('PATH COST =', cost)
        print(' -> '.join(city for city in optimal_path))

if __name__ == '__main__':
    main()

