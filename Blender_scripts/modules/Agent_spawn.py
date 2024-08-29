import bpy
import json
import os


class Agent:
    def __init__(self, name, path=None, obstacles=None):
        self.name = name
        self.path = path if path is not None else []
        self.obstacles = obstacles if obstacles is not None else []

    def to_dict(self):
        return {
            'name': self.name,
            'path': self.path,
            'obstacles': self.obstacles
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name', ''),
            path=data.get('path', []),
            obstacles=data.get('obstacles', [])
        )


def create_ellipsoid(location, scale, n):
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)

    obj = bpy.context.object

    obj.scale = scale
    obj.name = f"Agent{n}"


def save_agents(agents, file_name):
    current_script_dir = os.path.dirname(__file__)
    script_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
    file_path = os.path.join(script_dir, 'data', file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        for agent in agents:
            agent_data = agent.to_dict()
            json.dump(agent_data, f)
            f.write('\n')


def get_agents(file_name="test.json"):
    current_script_dir = os.path.dirname(__file__)
    script_dir = os.path.abspath(os.path.join(current_script_dir, '..'))
    file_path = os.path.join(script_dir, 'data', file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    agents = []

    with open(file_path, 'r') as file:
        for line in file:
            agent = json.loads(line.strip())
            agents.append(Agent.from_dict(agent))

    return agents

