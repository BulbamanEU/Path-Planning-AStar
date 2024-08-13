import bpy

start_locations = []
end_locations = []

green_color_name = "start"
red_color_name = "end"

def has_material(obj, material_name):
    for mat in obj.data.materials:
        if mat.name == material_name:
            return True
    return False

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        if has_material(obj, green_color_name):
            start_locations.append(tuple(round(coord, 0) for coord in obj.location))
        elif has_material(obj, red_color_name):
            end_locations.append(tuple(round(coord, 0) for coord in obj.location))

# Print results
print("Start Locations (Green Spheres):")
print(start_locations)
print("End Locations (Red Spheres):")
print(end_locations)
