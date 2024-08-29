import sys
import numpy as np
from scipy.optimize import linear_sum_assignment
import json

sys.path.append(r'C:\Users\Gintas\Documents\MANO IT\pathFinding')
from Blender_scripts.get_coordinates import get_coords



def write_to_file(data, file_path=r"C:\Users\Gintas\Documents\MANO IT\pathFinding\Blender_scripts\examples\values.json"):
    with open(file_path, 'w') as f:
        for key, value in data.items():
            json.dump(key, f)
            f.write(": ")
            json.dump(value, f)
            f.write("\n")



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
