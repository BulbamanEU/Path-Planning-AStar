import bpy
import random

num_agents = 100


def create_material(material_name, color):
    if material_name in bpy.data.materials:
        material = bpy.data.materials[material_name]
    else:
        material = bpy.data.materials.new(name=material_name)

    material.use_nodes = False
    material.diffuse_color = color + (1.0,)


def random_points(n):
    rnge = 200

    location = (random.randint(0, rnge), random.randint(0, rnge), random.randint(0, rnge))
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)
    start = bpy.context.object
    start.name = f"start{n}"

    material = bpy.data.materials.get("start")
    if material:
        start.data.materials.append(material)

    location = (random.randint(0, rnge), random.randint(0, rnge), random.randint(0, rnge))
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)
    end = bpy.context.object
    end.name = f"end{n}"

    material = bpy.data.materials.get("end")
    if material:
        end.data.materials.append(material)


for material_name, color in [("start", (0, 1, 0)), ("end", (1, 0, 0))]:
    if material_name not in bpy.data.materials:
        create_material(material_name, color)

for i in range(num_agents):
    random_points(i + 1)
