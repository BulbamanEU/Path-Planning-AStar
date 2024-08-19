import heapq

class Node:
    def __init__(self, position=None, parent=None, cost=0, heuristic_cost=0, total_cost=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic_cost = heuristic_cost
        self.total_cost = total_cost

    def __lt__(self, other):
        #return self.cost < other.cost
        return self.total_cost < other.total_cost

    def __eq__(self, other):
        return self.position == other.position

class AStar3D:
    def plan(self, start, end, obstacles):
        start_node = Node(position=start)
        end_node = Node(position=end)

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


            for new_position in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1) #]:
            ,(-1, -1, 0), (-1, 1, 0), (1, -1, 0), (1, 1, 0),
             (-1, 0, -1), (1, 0, -1), (-1, 0, 1), (1, 0, 1),
             (0, -1, -1), (0, 1, -1), (0, -1, 1), (0, 1, 1),
             (-1, -1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1),
             (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)]:

                node_position = (current_node.position[0] + new_position[0],
                                 current_node.position[1] + new_position[1],
                                 current_node.position[2] + new_position[2])

                if node_position in closed_list:
                    continue

                if node_position in obstacles:
                    continue

                # check if node is inside the grid

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

    #path cutting
    def is_line_of_sight_clear(self, start, end):
        # Placeholder for line-of-sight check
        # In a real scenario, this would check if a direct line between start and end is clear of obstacles.
        return True

    #path smoothing
    def smooth_path(self, path):
        return


# create grid or just search around?

# path cutting
# check the path if it is possible to shorten it by skipping some points and going straight to the end or closer to the end

# need a way for multi agent path planning
# CBS with A* maybe
# find every agent path with A* then check for collisions and re-plan paths if needed
# ILP or MILP but idk ar jie computationaly viable butu
