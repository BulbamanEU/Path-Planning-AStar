from remove_collection import delete_collection
from planAStar3D import AStar3D
from get_coordinates import get_coords
from draw_path import draw_path
from clear_action import reset_animations_and_constraints
from animation import no_rotation, adjust_path_after_collision
from Agent_spawn import Agent, save_agents
from delete import delete_object
from log_info import write_log
import numpy as np
from scipy.optimize import linear_sum_assignment
from save_points import write_to_file

step_length = 1
speed = 10

# TODO: better new path calculation
def new_path(agent, n):
    start = agent.path[0]
    goal = agent.path[-1]

    write_log(f"Planning A* algorithm for {agent.name}")
    write_log(f"Starting: {start} \nGoal: {goal}")

    obstacles = agent.obstacles
    write_log(f"Agent obstacles: {obstacles}")
    AStar = AStar3D()

    path = AStar.plan(start, goal, obstacles, step_length)
    delete_object(f"Path{n}")
    write_log(f"length: {len(path)}, path: {path}")
    draw_path(path, n)

    reset_animations_and_constraints(f"Agent{n}")
    no_rotation(n, speed)
    agent.path = path

    write_log(f"Replanned A* path for {agent.name}")
    return path


def main():
    obstacles = []

    delete_collection("Paths")

    start, goal = get_coords()

    # TODO: group start/goal locations differently?

    start_np = np.array(start)
    goal_np = np.array(goal)

    cost_matrix = np.linalg.norm(start_np[:, np.newaxis] - goal_np, axis=2)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    start = [start[i] for i in row_ind]
    goal = [goal[j] for j in col_ind]

    data_to_save = {"start": start,
                    "goal": goal}

    # write_to_file(data_to_save, loc_file)

    AStar = AStar3D()
    paths = []

    for i in range(len(start)):
        path = AStar.plan(start[i], goal[i], obstacles, step_length)
        agent = Agent(f"Agent{i+1}", path)

        agents.append(agent)

        draw_path(path, i+1)

        reset_animations_and_constraints(f"Agent{i+1}")
        no_rotation(i+1, speed)

        paths.append(path)


if __name__ == "__main__":
    agent_file = "test.json"
    # loc_file = "example.json"
    agents = []
    main()
    save_agents(agents, agent_file)