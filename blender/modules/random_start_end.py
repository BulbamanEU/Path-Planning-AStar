import bpy
import random
import numpy as np
import math


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

def saved_points(n, s_loc, g_loc):
    bpy.ops.mesh.primitive_uv_sphere_add(location=s_loc)
    start = bpy.context.object
    start.name = f"start{n}"
    material = bpy.data.materials.get("start")
    if material:
        start.data.materials.append(material)

    bpy.ops.mesh.primitive_uv_sphere_add(location=g_loc)
    goal = bpy.context.object
    goal.name = f"end{n}"
    material = bpy.data.materials.get("end")
    if material:
        goal.data.materials.append(material)

def hor_grid_formation(num_agents, spacing, height):
    locations = []
    size = int(num_agents**0.5) + 1
    for i in range(size):
        for j in range(size):
            if len(locations) < num_agents:
                locations.append((i * spacing, j * spacing, height))
    return locations

def ver_grid_formation(num_agents, spacing):
    locations = []
    size = int(num_agents**0.5) + 1
    for i in range(size):
        for j in range(size):
            if len(locations) < num_agents:
                locations.append((5, i * spacing, j * spacing))
    return locations

def draw_points(num_agents, radius):
    height = 5
    loc = generate_spiral_formation(num_agents, radius, height)
    print(loc)
    n=1

    for location in loc:
        bpy.ops.mesh.primitive_uv_sphere_add(location=location)
        start = bpy.context.object
        start.name = f"start{n}"
        material = bpy.data.materials.get("start")
        if material:
            start.data.materials.append(material)
        n += 1


def generate_spiral_formation(num_agents, initial_radius, growth_rate):
    locations = []
    for i in range(num_agents):
        angle = i * 0.1  # Adjust the step to control the tightness of the spiral
        radius = initial_radius + i * growth_rate
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z =
        locations.append((x, y, 0))
    return locations

def generate_diamond_formation(num_agents, spacing, height):
    locations = []
    layer = 0

    while len(locations) < num_agents:
        layer += 1
        # Top and bottom layers of the diamond
        for i in range(-layer, layer + 1):
            for j in range(-layer, layer + 1):
                if abs(i) + abs(j) == layer and len(locations) < num_agents:
                    locations.append((i * spacing, j * spacing, height))

    return locations


def generate_circle_formation(num_agents, radius):
    locations = []
    angle_step = 2 * math.pi / num_agents
    for i in range(num_agents):
        angle = i * angle_step
        y = radius * math.cos(angle)
        z = radius * math.sin(angle) + radius + 10
        locations.append((radius+10, y, z))
    return locations