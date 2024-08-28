import bpy
import json


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


def save_agents(agents, file_path):

    with open(file_path, 'w') as f:
        for agent in agents:
            agent_data = agent.to_dict()
            json.dump(agent_data, f)
            f.write('\n')


def get_agents(file_path):
    agents = []

    with open(file_path, 'r') as file:
        for line in file:
            agent = json.loads(line.strip())
            agents.append(Agent.from_dict(agent))

    return agents

