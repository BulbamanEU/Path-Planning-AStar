import bpy
import mathutils


def get_bounding_box_corners(obj):
    bbox_corners = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
    return bbox_corners


def is_aabb_collision(corners1, corners2):
    min1 = mathutils.Vector((min(corner[0] for corner in corners1),
                             min(corner[1] for corner in corners1),
                             min(corner[2] for corner in corners1)))

    max1 = mathutils.Vector((max(corner[0] for corner in corners1),
                             max(corner[1] for corner in corners1),
                             max(corner[2] for corner in corners1)))

    min2 = mathutils.Vector((min(corner[0] for corner in corners2),
                             min(corner[1] for corner in corners2),
                             min(corner[2] for corner in corners2)))

    max2 = mathutils.Vector((max(corner[0] for corner in corners2),
                             max(corner[1] for corner in corners2),
                             max(corner[2] for corner in corners2)))

    overlap_x = max1.x >= min2.x and max2.x >= min1.x
    overlap_y = max1.y >= min2.y and max2.y >= min1.y
    overlap_z = max1.z >= min2.z and max2.z >= min1.z

    return overlap_x and overlap_y and overlap_z


def check_objects_collision(obj1, obj2):
    corners1 = get_bounding_box_corners(obj1)
    corners2 = get_bounding_box_corners(obj2)
    return is_aabb_collision(corners1, corners2)

object1 = bpy.data.objects.get("Object1")
object2 = bpy.data.objects.get("Object2")

if object1 and object2:
    collision_detected = check_objects_collision(object1, object2)
    print(f"Collision Detected: {collision_detected}")
else:
    print("One or both objects not found.")
