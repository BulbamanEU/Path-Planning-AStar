import bpy

def create_ellipsoid(location, scale, n):
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)

    obj = bpy.context.object

    obj.scale = scale
    obj.name = f"Agent{n}"