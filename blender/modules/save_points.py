import os
import numpy as np
from scipy.optimize import linear_sum_assignment
import json
from get_coordinates import get_coords



def write_to_file(data, file_name="values.json"):
    current_script_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_script_dir, '..', 'examples', file_name))
    print(file_path)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        for key, value in data.items():
            json.dump(key, f)
            f.write(": ")
            json.dump(value, f)
            f.write("\n")

def read_from_file(file_name="values.json"):
    current_script_dir = os.path.dirname(__file__)
    file_path = os.path.abspath(os.path.join(current_script_dir, '..', 'examples', file_name))

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'r') as f:
        data = json.load(f)
    start = data.get("start")
    goal = data.get("goal")
    num_agents = len(start)

    return start, goal, num_agents




if __name__ == "__main__":
    start, goal = get_coords()

    start_np = np.array(start)
    goal_np = np.array(goal)

    cost_matrix = np.linalg.norm(start_np[:, np.newaxis] - goal_np, axis=2)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    start = [start[i] for i in row_ind]
    goal = [goal[j] for j in col_ind]

    data_to_save = {"start": start,
                    "goal": goal}

    write_to_file(data_to_save)
