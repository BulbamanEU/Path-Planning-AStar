import bpy
import heapq
import numpy as np
from scipy.optimize import linear_sum_assignment

# get coordinates
start_locations = []
end_locations = []

green_color_name = "start"
red_color_name = "end"

def has_material(obj, material_name):
    for mat in obj.data.materials:
        if mat.name == material_name:
            return True
    return False

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        if has_material(obj, green_color_name):
            start_locations.append(tuple(round(coord, 0) for coord in obj.location))
        elif has_material(obj, red_color_name):
            end_locations.append(tuple(round(coord, 0) for coord in obj.location))

# Print results
print("Start Locations (Green Spheres):")
print(start_locations)
print("End Locations (Red Spheres):")
print(end_locations)


# AStar3D

class Node:
    def __init__(self, position=None, parent=None, cost=0, heuristic_cost=0, total_cost=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic_cost = heuristic_cost
        self.total_cost = total_cost

    def __lt__(self, other):
        # return self.cost < other.cost
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

            for new_position in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)  # ]:
                , (-1, -1, 0), (-1, 1, 0), (1, -1, 0), (1, 1, 0),
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
        # euclidian heuristics
        # return ((position[0] - goal[0]) ** 2 + (position[1] - goal[1]) ** 2 + (position[2] - goal[2]) ** 2) ** 0.5
        return abs(position[0] - goal[0]) + abs(position[1] - goal[1]) + abs(position[2] - goal[2])

    def step_length(self, last_pos, new_pos):
        # return ((new_pos[0] - last_pos[0]) ** 2 + (new_pos[1] - last_pos[1]) ** 2 + (new_pos[2] - last_pos[2]) ** 2) ** 0.5
        return abs(new_pos[0] - last_pos[0]) + abs(new_pos[1] - last_pos[1]) + abs(new_pos[2] - last_pos[2])

    # path cutting
    def is_line_of_sight_clear(self, start, end):
        # Placeholder for line-of-sight check
        # In a real scenario, this would check if a direct line between start and end is clear of obstacles.
        return True

    # path smoothing
    def smooth_path(self, path):
        return

collision_cords = []
obstacles = []

start = start_locations
goal = end_locations

start_np = np.array(start)
goal_np = np.array(goal)

cost_matrix = np.linalg.norm(start_np[:, np.newaxis] - goal_np, axis=2)
row_ind, col_ind = linear_sum_assignment(cost_matrix)

start = [start[i] for i in row_ind]
goal = [goal[j] for j in col_ind]

AStar = AStar3D()
paths = []

for i in range(len(start)):
    path = AStar.plan(start[i], goal[i], obstacles)
    paths.append(path)


def draw_path(path):
    scale = 1
    curve_data = bpy.data.curves.new(name="PathCurve", type='CURVE')
    curve_data.dimensions = '3D'
    polyline = curve_data.splines.new('POLY')
    polyline.points.add(len(path) - 1)

    for i, point in enumerate(path):
        polyline.points[i].co = (point[0] / scale, point[1] / scale, point[2] / scale, 1)

    curve_object = bpy.data.objects.new("Path", curve_data)
    bpy.context.collection.objects.link(curve_object)

for path in paths:
    draw_path(path)