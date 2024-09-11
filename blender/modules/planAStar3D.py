import heapq

class Node:
    def __init__(self, position=None, parent=None, cost=0, heuristic_cost=0, total_cost=0):
        self.position = tuple(position)  # Ensure position is stored as a tuple
        self.parent = parent
        self.cost = cost
        self.heuristic_cost = heuristic_cost
        self.total_cost = total_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __eq__(self, other):
        return self.position == other.position

class AStar3D:
    def plan(self, start, end, obstacles, step_size):
        start_node = Node(position=tuple(start))  # Convert start position to a tuple
        end_node = Node(position=tuple(end))  # Convert end position to a tuple

        open_list = []
        closed_list = set()
        open_dict = {}

        heapq.heappush(open_list, start_node)
        open_dict[start_node.position] = start_node

        while open_list:
            current_node = heapq.heappop(open_list)
            closed_list.add(current_node.position)
            open_dict.pop(current_node.position, None)

            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                return path[::-1]

            for new_position in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1),
                                 (-1, -1, 0), (-1, 1, 0), (1, -1, 0), (1, 1, 0),
                                 (-1, 0, -1), (1, 0, -1), (-1, 0, 1), (1, 0, 1),
                                 (0, -1, -1), (0, 1, -1), (0, -1, 1), (0, 1, 1),
                                 (-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1),
                                 (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)]:

                node_position = (current_node.position[0] + new_position[0]*step_size,
                                 current_node.position[1] + new_position[1]*step_size,
                                 current_node.position[2] + new_position[2]*step_size)

                if node_position in closed_list:
                    continue

                if node_position in obstacles:
                    continue

                d = self.step_length(current_node.position, node_position)
                g_new = current_node.cost + d
                h_new = self.heuristics(node_position, end_node.position)
                f_new = g_new + h_new

                new_node = Node(node_position, current_node, g_new, h_new, f_new)

                if node_position in open_dict and open_dict[node_position].total_cost <= new_node.total_cost:
                    continue

                heapq.heappush(open_list, new_node)
                open_dict[node_position] = new_node

        return None

    def heuristics(self, position, goal):
        return abs(position[0] - goal[0]) + abs(position[1] - goal[1]) + abs(position[2] - goal[2])

    def step_length(self, last_pos, new_pos):
        return abs(new_pos[0] - last_pos[0]) + abs(new_pos[1] - last_pos[1]) + abs(new_pos[2] - last_pos[2])
