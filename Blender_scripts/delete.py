import bpy

def delete_object(object_name):
    # Check if the object exists in the current scene
    obj = bpy.data.objects.get(object_name)
    if obj:
        # Select the object
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        # Delete the object
        bpy.ops.object.delete()
        print(f"Deleted object: {object_name}")
    else:
        print(f"Object '{object_name}' not found!")