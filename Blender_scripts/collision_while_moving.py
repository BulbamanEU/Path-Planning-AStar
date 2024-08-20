import bpy
import mathutils


def ellipsoids_collide(obj1, obj2):
    # Ensure both objects are meshes
    if obj1.type == 'MESH' and obj2.type == 'MESH':
        # Get the locations (centers) of the ellipsoids
        center1 = obj1.location
        center2 = obj2.location

        # Get the radii along each axis (half of the dimensions)
        radii1 = obj1.dimensions / 2.0
        radii2 = obj2.dimensions / 2.0

        # Calculate the vector between the centers
        delta = center2 - center1

        # Normalize the delta by the radii of each ellipsoid
        normalized_delta = mathutils.Vector((delta.x / radii1.x, delta.y / radii1.y, delta.z / radii1.z))
        normalized_distance_squared = normalized_delta.length_squared

        # Calculate the maximum distance allowed for no collision
        max_distance_squared = (1.0 ** 2)  # Always 1.0 squared for unit sphere after normalization

        # Check collision based on normalized distance
        return normalized_distance_squared <= (1.0 + radii2.x / radii1.x) ** 2

    return False

def frame_change_handler(scene):
    """Check collisions at each frame."""
    object1 = bpy.data.objects.get("Sphere1")  # Replace with your object names
    object2 = bpy.data.objects.get("Sphere2")  # Replace with your object names

    if object1 and object2:
        collision = ellipsoids_collide(object1, object2)
        if collision:
            print(f"Collision detected between {object1.name} and {object2.name} at frame {scene.frame_current}")
            object1.data.materials.append(bpy.data.materials.get("collision"))
            object2.data.materials.append(bpy.data.materials.get("collision"))

        else:
            object1.data.materials.clear()
            object2.data.materials.clear()

bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(frame_change_handler)

# To remove the handler later, use
# bpy.app.handlers.frame_change_post.remove(frame_change_handler)
