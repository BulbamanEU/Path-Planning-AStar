import bpy
from random_start_end import random_points, create_material
from Agent_spawn import create_ellipsoid
from save_points import read_from_file

num_agents = 20
rnge = 20

read_from_example = False # change to .txt file to visualize
# read_from_example = r".txt"

def delete_environment():
    bpy.ops.object.select_all(action='DESELECT')

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.delete()


def new_environment(read_from_example):
    for material_name, color in [("start", (0, 1, 0)), ("end", (1, 0, 0)), ("collision", (0.246, 0.069, 0.802))]:
        if material_name not in bpy.data.materials:
            create_material(material_name, color)

    min_distance = max(x_scale, y_scale, z_scale) * 2

    start_points = []
    goal_points = []

    if read_from_example:
        start, goal, num_agents_f = read_from_file(read_from_example)
        for n in range(1, num_agents_f + 1):
            loc = random_points(n, rnge, start_points, goal_points, min_distance)
            create_ellipsoid((0, 0, 0), (x_scale, y_scale, z_scale), n)
    else:
        for n in range(1, num_agents + 1):
            start_loc, goal_loc = random_points(n, rnge, start_points, goal_points, min_distance)
            create_ellipsoid((0,0,0), (x_scale, y_scale, z_scale), n)


x_scale = 1
y_scale = 1
z_scale = 2

delete_environment()
new_environment(read_from_example)


