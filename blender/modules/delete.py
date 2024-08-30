import bpy

def delete_object(object_name):
    obj = bpy.data.objects.get(object_name)
    if obj:
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        bpy.ops.object.delete()
        print(f"Deleted object: {object_name}")
    else:
        print(f"Object '{object_name}' not found!")