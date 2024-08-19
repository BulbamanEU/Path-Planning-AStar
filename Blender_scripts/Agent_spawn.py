import bpy

x_scale = 1
y_scale = 1
z_scale = 2

num_agents = 100

def create_ellipsoid(location, scale, n):
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)

    obj = bpy.context.object

    obj.scale = scale
    obj.name = f"Agent{n}"

for n in range(1, num_agents+1):
    create_ellipsoid((0, 0, 0), (x_scale, y_scale, z_scale), n)