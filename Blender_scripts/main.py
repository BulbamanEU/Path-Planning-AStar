import bpy
from remove_collection import delete_collection
from planAStar3D import AStar3D
from get_coordinates import get_coords
from draw_path import draw_path
from clear_action import reset_animations_and_constraints
from animation import no_rotation
import numpy as np
from scipy.optimize import linear_sum_assignment

def main():

    collision_cords = []
    obstacles = []

    delete_collection("Paths")

    start, goal = get_coords()

    print(f"end: {goal}")

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
        # print(f"length: {len(path)}, path: {path}")
        draw_path(path, i+1)

        reset_animations_and_constraints(f"Agent{i+1}")
        no_rotation(i+1)


        paths.append(path)


main()