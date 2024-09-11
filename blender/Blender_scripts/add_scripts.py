import os
import sys
import bpy

def create_material(material_name, color):
    if material_name in bpy.data.materials:
        material = bpy.data.materials[material_name]
    else:
        material = bpy.data.materials.new(name=material_name)

    material.use_nodes = False
    material.diffuse_color = color + (1.0,)

current_script_dir = os.path.dirname(__file__)

script_dir = os.path.abspath(os.path.join(current_script_dir, '..', 'Blender_scripts'))
modules_dir = os.path.abspath(os.path.join(current_script_dir, '..', 'modules'))

sys.path.append(script_dir)
sys.path.append(modules_dir)

for material_name, color in [("start", (0, 1, 0)), ("end", (1, 0, 0)), ("collision", (0.246, 0.069, 0.802))]:
    if material_name not in bpy.data.materials:
        create_material(material_name, color)