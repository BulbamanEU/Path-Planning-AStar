import bpy
from remove_collection import delete_collection
from planAStar3D import AStar3D
from get_coordinates import get_coords
from draw_path import draw_path
from clear_action import reset_animations_and_constraints
from animation import no_rotation
from Agent_spawn import Agent, save_agent_to_json
from delete import delete_object
import numpy as np
from scipy.optimize import linear_sum_assignment


def new_path(agent, n):
    start = agent.path[0]
    print(start)
    goal = agent.path[-1]
    print(goal)
    obstacles = agent.obstacles
    AStar = AStar3D()

    path = AStar.plan(start, goal, obstacles)
    delete_object(f"Path{n}")
    print(f"length: {len(path)}, path: {path}")
    draw_path(path, n)

    reset_animations_and_constraints(f"Agent{n}")
    no_rotation(n)
    agent.path = path
    return path

def main():

    collision_cords = []
    obstacles = []

    delete_collection("Paths")

    start, goal = get_coords()

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
        agent = Agent(f"Agent{i+1}", path)
        file_path = r"C:\Users\Gintas\Documents\MANO IT\pathFinding\Blender_scripts\test.json"
        save_agent_to_json(agent, file_path)
        # print(f"length: {len(path)}, path: {path}")

        draw_path(path, i+1)

        reset_animations_and_constraints(f"Agent{i+1}")
        no_rotation(i+1)


        paths.append(path)


main()