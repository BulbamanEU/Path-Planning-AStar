import bpy
from random_start_end import random_points, create_material
from Agent_spawn import create_ellipsoid

num_agents = 10
rnge = 15

def delete_environment():
    bpy.ops.object.select_all(action='DESELECT')

    bpy.ops.object.select_all(action='SELECT')

    bpy.ops.object.delete()


def new_environment():
    agents = []
    for material_name, color in [("start", (0, 1, 0)), ("end", (1, 0, 0))]:
        if material_name not in bpy.data.materials:
            create_material(material_name, color)

    for n in range(1, num_agents + 1):
        loc = random_points(n, rnge)
        create_ellipsoid((0, 0, 0), (x_scale, y_scale, z_scale), n)


x_scale = 1
y_scale = 1
z_scale = 2

delete_environment()
new_environment()


