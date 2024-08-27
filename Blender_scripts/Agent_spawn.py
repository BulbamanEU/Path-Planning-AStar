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

def save_agent_to_json(agent, filename):
    agent_data = agent.to_dict()
    try:
        with open(filename, 'a') as file:
            json.dump(agent_data, file)
            file.write('\n')
    except IOError as e:
        print(f"An error occurred: {e}")

def load_agents_from_json(filename):
    agents = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    agent_data = json.loads(line.strip())
                    agents.append(Agent.from_dict(agent_data))
    except IOError as e:
        print(f"An error occurred: {e}")
    return agents
