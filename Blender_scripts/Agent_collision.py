import bpy
import mathutils

num_agents = 20


def get_evaluated_position(obj):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval = obj.evaluated_get(depsgraph)
    return obj_eval.matrix_world.translation

def ellipsoids_collide(obj1, obj2):
    if obj1.type == 'MESH' and obj2.type == 'MESH':
        center1 = get_evaluated_position(obj1)
        center2 = get_evaluated_position(obj2)

        radii1 = obj1.dimensions / 2.0
        radii2 = obj2.dimensions / 2.0

        delta = center2 - center1

        # Normalize the delta by the radii of each ellipsoid
        normalized_delta = mathutils.Vector((delta.x / radii1.x, delta.y / radii1.y, delta.z / radii1.z))
        normalized_distance_squared = normalized_delta.length_squared

        # Check collision based on normalized distance
        return normalized_distance_squared <= (1.0 + radii2.x / radii1.x) ** 2

    return False

def frame_change_handler(scene):
    colliding_agents = set()

    for i in range(1, num_agents + 1):
        for j in range(i + 1, num_agents + 1):
            agent1 = bpy.data.objects.get(f"Agent{i}")
            agent2 = bpy.data.objects.get(f"Agent{j}")

            if agent1 and agent2:
                collision = ellipsoids_collide(agent1, agent2)
                if collision:
                    print(f"Collision detected between {agent1.name} and {agent2.name} at frame {scene.frame_current}")
                    colliding_agents.add(agent1)
                    colliding_agents.add(agent2)
            else:
                print(f"Agent not found: Agent{i} or Agent{j}")

    for i in range(1, num_agents + 1):
        agent = bpy.data.objects.get(f"Agent{i}")
        if agent:
            if agent in colliding_agents:
                #bpy.data.materials.get("collision") not in agent.data.materials: 
                agent.data.materials.clear()
                agent.data.materials.append(bpy.data.materials.get("collision"))
            else:
                agent.data.materials.clear()

bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(frame_change_handler)

# To remove the handler later, use
# bpy.app.handlers.frame_change_post.remove(frame_change_handler)
