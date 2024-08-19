import bpy

def reset_animations_and_constraints(agent_name):
    agent_obj = bpy.data.objects.get(agent_name)

    if agent_obj:
        agent_obj.animation_data_clear()
        agent_obj.constraints.clear()