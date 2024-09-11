import bpy
import random
import numpy as np
import math

SPACING = 3
OFFSET = 10

RADIUS = 40

INITIAL_RADIUS = 15
GROWTH_RATE = 3
H_GROWTH_RATE = 0.6


def select_formation(formation, NUM_AGENTS):

    locations = []

    if formation == "random_points":
        locations = random_points(NUM_AGENTS, rnge=50, min_distance=5)

    if formation == "hor_grid_formation":
        locations = hor_grid_formation(NUM_AGENTS, SPACING, OFFSET + random.randint(-10, 10))

    if formation == "ver_grid_formation":
        locations = ver_grid_formation(NUM_AGENTS, SPACING+2, OFFSET + random.randint(-10, 10))

    if formation == "spiral_formation":
        locations = spiral_formation(NUM_AGENTS, INITIAL_RADIUS, GROWTH_RATE, H_GROWTH_RATE)

    if formation == "diamond_formation":
        locations = diamond_formation(NUM_AGENTS, SPACING, OFFSET)

    if formation == "circle_formation":
        locations = circle_formation(NUM_AGENTS, RADIUS)

    return locations


def draw_points(locations, type):
    n = 1

    for loc in locations:
        bpy.ops.mesh.primitive_uv_sphere_add(location=loc)
        point = bpy.context.object
        point.name = type + str(n)
        material = bpy.data.materials.get(type)
        if material:
            point.data.materials.append(material)
        n += 1


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


def random_points(num_agents, rnge=30, min_distance=3):
    locations = []

    for n in range(num_agents):
        point = generate_non_colliding_point(locations, rnge, min_distance)
        locations.append(point)

    return locations


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


def hor_grid_formation(num_agents, spacing, offset):
    locations = []
    size = int(num_agents**0.5) + 1
    for i in range(size):
        for j in range(size):
            if len(locations) < num_agents:
                locations.append((i * spacing, j * spacing, offset))
    return locations


def ver_grid_formation(num_agents, spacing, offset):
    locations = []
    size = int(num_agents**0.5) + 1
    for i in range(size):
        for j in range(size):
            if len(locations) < num_agents:
                locations.append((offset, i * spacing, j * spacing))
    return locations


#def spiral_formation(num_agents, initial_radius, growth_rate):
#    locations = []
#    for i in range(num_agents):
#        angle = i * 0.1  # Adjust the step to control the tightness of the spiral
#        radius = initial_radius + i * growth_rate
#        x = radius * math.cos(angle)
#        y = radius * math.sin(angle)
#        # z =
#        locations.append((x, y, 0))
#    return locations

def spiral_formation(num_agents, initial_radius, growth_rate, height_growth_rate):
    locations = []
    for i in range(num_agents):
        angle = i * 0.3  # Controls the tightness of the spiral
        # radius = initial_radius + i * growth_rate
        x = initial_radius * math.cos(angle)
        y = initial_radius * math.sin(angle)
        z = i * height_growth_rate  # Increasing the Z-axis value gradually to create the spiral's height
        locations.append((x, y, z))
    return locations


def diamond_formation(num_agents, spacing, offset):
    locations = []
    layer = 0

    while len(locations) < num_agents:
        layer += 1
        # Top and bottom layers of the diamond
        for i in range(-layer, layer + 1):
            for j in range(-layer, layer + 1):
                if abs(i) + abs(j) == layer and len(locations) < num_agents:
                    locations.append((i * spacing, j * spacing, offset))

    return locations


def circle_formation(num_agents, radius):
    locations = []
    angle_step = 2 * math.pi / num_agents
    for i in range(num_agents):
        angle = i * angle_step
        y = radius * math.cos(angle)
        z = radius * math.sin(angle) + radius + 10
        locations.append((radius + 10, y, z))
    return locations