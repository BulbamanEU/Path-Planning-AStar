import bpy
from random_start_end import random_points, create_material, saved_points, draw_points, select_formation
from Agent_spawn import create_ellipsoid
from save_points import read_from_file
from log_info import write_log

num_agents = 50
FORMATIONS = ["random_points", "hor_grid_formation", "ver_grid_formation",
              "spiral_formation", "diamond_formation", "circle_formation"]
s_formation = FORMATIONS[1]
g_formation = FORMATIONS[3]
rnge = 50

# read_from_example = "example_test_2.json"
read_from_example = False # change to comment to visualize from file

def delete_environment():
    bpy.ops.object.select_all(action='DESELECT')

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.delete()


def new_environment():
    for material_name, color in [("start", (0, 1, 0)), ("end", (1, 0, 0)), ("collision", (0.246, 0.069, 0.802))]:
        if material_name not in bpy.data.materials:
            create_material(material_name, color)

def generate(read_from_example):

    start, goal, num_agents_f = read_from_file(read_from_example)
    write_log(f"start locs: {start}")
    write_log(f"goal locs: {goal}")
    for n in range(1, num_agents_f + 1):
        saved_points(n, start[n - 1], goal[n - 1])
        create_ellipsoid((0, 0, 0), (x_scale, y_scale, z_scale), n)

def spawning():
    start_points = []
    goal_points = []

    start_points = select_formation(s_formation)
    draw_points(start_points, "start")

    goal_points = select_formation(g_formation)
    draw_points(goal_points, "end")

    for n in range(len(start_points)):
        create_ellipsoid((0, 0, 0), (x_scale, y_scale, z_scale), n+1)






x_scale = 1
y_scale = 1
z_scale = 2

delete_environment()
new_environment()

if read_from_example:
    generate(read_from_example)
else:
    spawning()

