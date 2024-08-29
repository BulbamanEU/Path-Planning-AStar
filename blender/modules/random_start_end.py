import bpy
import random
import numpy as np


def create_material(material_name, color):
    if material_name in bpy.data.materials:
        material = bpy.data.materials[material_name]
    else:
        material = bpy.data.materials.new(name=material_name)

    material.use_nodes = False
    material.diffuse_color = color + (1.0,)


def is_valid_distance(new_point, existing_points, min_dist_xy=1, min_dist_z=2):
    for point in existing_points:
        dx = abs(new_point[0] - point[0])
        dy = abs(new_point[1] - point[1])
        dz = abs(new_point[2] - point[2])

        if dx < min_dist_xy or dy < min_dist_xy or dz < min_dist_z:
            return False
    return True


def generate_random_point(rnge):
    return (random.randint(0, rnge), random.randint(0, rnge), random.randint(0, rnge))



def is_far_enough(new_point, points, min_distance):
    for point in points:
        distance = np.linalg.norm(np.array(new_point) - np.array(point))
        if distance < min_distance:
            return False
    return True

def generate_non_colliding_point(existing_points, rnge, min_distance):
    while True:
        new_point = (random.randint(0, rnge), random.randint(0, rnge), random.randint(0, rnge))
        if is_far_enough(new_point, existing_points, min_distance):
            return new_point


def random_points(n, rnge, start_points, goal_points, min_distance):
    start_location = generate_non_colliding_point(start_points, rnge, min_distance)
    bpy.ops.mesh.primitive_uv_sphere_add(location=start_location)
    start = bpy.context.object
    start.name = f"start{n}"
    material = bpy.data.materials.get("start")
    if material:
        start.data.materials.append(material)
    start_points.append(start_location)

    # Generate non-colliding goal point
    goal_location = generate_non_colliding_point(goal_points, rnge, min_distance)
    bpy.ops.mesh.primitive_uv_sphere_add(location=goal_location)
    goal = bpy.context.object
    goal.name = f"end{n}"
    material = bpy.data.materials.get("end")
    if material:
        goal.data.materials.append(material)
    goal_points.append(goal_location)

    return start_location, goal_location