import bpy

start_frame = 1
end_frame = 200

def no_rotation(n):
    agent_name = f'Agent{n}'
    path_name = f'Path{n}'

    agent_obj = bpy.data.objects.get(agent_name)
    path_obj = bpy.data.objects.get(path_name)

    if agent_obj and path_obj and path_obj.type == 'CURVE':

        follow_path_constraint = agent_obj.constraints.new(type='FOLLOW_PATH')
        follow_path_constraint.target = path_obj

        follow_path_constraint.use_curve_follow = False
        follow_path_constraint.use_fixed_location = True
        follow_path_constraint.offset_factor = 0.0

        agent_obj.rotation_mode = 'XYZ'

        path_obj.data.use_path = True
        path_obj.data.path_duration = end_frame - start_frame

        follow_path_constraint.offset_factor = 0.0
        agent_obj.keyframe_insert(data_path="constraints[\"Follow Path\"].offset_factor", frame=start_frame)

        follow_path_constraint.offset_factor = 1.0
        agent_obj.keyframe_insert(data_path="constraints[\"Follow Path\"].offset_factor", frame=end_frame)
    else:
        print(f"Agent or Path not found for index {n}: {agent_name}, {path_name}")
