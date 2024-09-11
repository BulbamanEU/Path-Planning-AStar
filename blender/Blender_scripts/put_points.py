import bpy
import random
import math

SPACING = 1
HEIGHT = 1
RADIUS = 1


def calculate_start():
    calculating = True
    num = 0

    while calculating:
        if bpy.data.objects.get(f"start{num+1}"):
            num += 1
        else:
            calculating = False

    for n in range(num):
        start = bpy.data.objects.get(f"start{n+1}")
        # 0 - x, 1 - y, 2 - z
        start.location[0] = 50

    return num


def grid_formation(num_agents, spacing, height, orientation="horizontal"):
    locations = []
    size = int(num_agents**0.5) # + 1
    for i in range(size):
        for j in range(size):
            if len(locations) < num_agents:
                if orientation == "horizontal":
                    locations.append((i * spacing, j * spacing, height))
                else:
                    locations.append((height, i * spacing, j * spacing))
    return locations

def generate_line_formation(num_agents, spacing, height, orientation="horizontal"):
    locations = []
    for i in range(num_agents):
        if orientation == 'horizontal':
            locations.append((i * spacing, 0, height))
        else:
            locations.append((height, 0, i * spacing))
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

def generate_random_scatter(num_agents, range_x, range_y, range_z):
    locations = []
    for _ in range(num_agents):
        x = random.uniform(0, range_x)
        y = random.uniform(0, range_y)
        z = random.uniform(0, range_z)
        locations.append((x, y, z))
    return locations

def generate_diamond_formation(num_agents, spacing, height):
    locations = []
    n = int((num_agents + 1) / 2)
    for i in range(n):
        for j in range(n - i):
            if len(locations) < num_agents:
                locations.append((i * spacing, j * spacing, height))
                if len(locations) < num_agents:
                    locations.append((-i * spacing, j * spacing, height))
                    if len(locations) < num_agents:
                        locations.append((i * spacing, -j * spacing, height))
                        if len(locations) < num_agents:
                            locations.append((-i * spacing, -j * spacing, height))
    return locations

def generate_spiral_formation(num_agents, initial_radius, growth_rate):
    locations = []
    for i in range(num_agents):
        angle = i * 0.1  # Adjust the step to control the tightness of the spiral
        radius = initial_radius + i * growth_rate
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        locations.append((x, y, 0))
    return locations


def generate_cluster_formation(num_agents, cluster_centers, radius):
    locations = []
    for i in range(num_agents):
        center = random.choice(cluster_centers)
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, radius)
        x = center[0] + r * math.cos(angle)
        y = center[1] + r * math.sin(angle)
        locations.append((x, y, 0))
    return locations


def generate_rectangle_formation(num_agents, rows, cols, spacing):
    locations = []
    for i in range(rows):
        for j in range(cols):
            if len(locations) < num_agents:
                locations.append((i * spacing, j * spacing, 0))
    return locations


def create_cube_formation(cube_size=2, spacing=2):
    bpy.ops.object.select_all(action='DESELECT')

    # Coordinates for the vertices of a cube
    positions = [
        (-cube_size, -cube_size, -cube_size),
        (-cube_size, -cube_size, cube_size),
        (-cube_size, cube_size, -cube_size),
        (-cube_size, cube_size, cube_size),
        (cube_size, -cube_size, -cube_size),
        (cube_size, -cube_size, cube_size),
        (cube_size, cube_size, -cube_size),
        (cube_size, cube_size, cube_size)
    ]

    for idx, pos in enumerate(positions):
        # Create a sphere at each vertex of the cube
        bpy.ops.mesh.primitive_uv_sphere_add(location=[p * spacing for p in pos])
        obj = bpy.context.object
        obj.name = f"Cube_Vertex_{idx + 1}"
        # Optionally, you can scale the spheres to make them smaller
        obj.scale = (0.5, 0.5, 0.5)


# Delete any existing objects in the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create the cube formation
create_cube_formation()



