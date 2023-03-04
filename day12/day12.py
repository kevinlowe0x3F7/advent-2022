import heapq

def day12():
    nodes = dict()
    distances = dict()
    i = 1
    starting_locations = []
    with (open('./day12.txt')) as f:
        for line in f.readlines():
            j = 0
            for char in line.rstrip():
                if char == "S":
                    print("found start: {}", (i, j))
                    nodes[(i, j)] = 1
                    distances[(i, j)] = float('inf')
                elif char == "E":
                    print("found end: {}", (i, j))
                    nodes[(i, j)] = 26
                    distances[(i, j)] = 0
                else:
                    nodes[(i, j)] = ord(char) - 96
                    distances[(i, j)] = float('inf')
                    if char == "a":
                        starting_locations.append((i, j))
                j += 1
            i += 1

    start = (21, 0)
    end = (21, 72)
    pq = [(0, end)]
    visited = set()
    while pq:
        (dist, node) = heapq.heappop(pq)
        if node in visited:
            continue

        visited.add(node)

        for neighbor in get_neighbors(nodes, node):
            if neighbor not in visited:
                new_distance = dist + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

    print(distances)
    print(distances[start])
    print(min([distances[location] for location in starting_locations]))


def get_neighbors(nodes, pos):
    possible_neighbors = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
    neighbors = []
    for neighbor in possible_neighbors:
        if is_valid_neighbor(nodes, pos, neighbor):
            neighbors.append(neighbor)
    return neighbors


def is_valid_neighbor(nodes, pos, potential_neighbor):
    neighbor = nodes.get(potential_neighbor)
    return neighbor is not None and nodes[pos] - neighbor <= 1


if __name__ == '__main__':
    day12()
