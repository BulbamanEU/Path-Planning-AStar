import bpy
from log_info import write_log

def delete_object(object_name):
    obj = bpy.data.objects.get(object_name)
    if obj:
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        bpy.ops.object.delete()
        write_log(f"Deleted object: {object_name}")
    else:
        write_log(f"Object '{object_name}' not found!")