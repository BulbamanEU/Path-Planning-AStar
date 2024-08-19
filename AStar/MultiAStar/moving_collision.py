import numpy as np
from fcl import *

# Define two spheres with their respective transforms and radii
sphere1 = Sphere(radius=1.0)
sphere2 = Sphere(radius=0.5)

# Define initial and final transforms for each sphere
tf1_start = Transform(np.array([0.0, 0.0, 0.0]))  # Initial transform for sphere 1
tf1_end = Transform(np.array([2.0, 0.0, 0.0]))  # Final transform for sphere 1
tf2_start = Transform(np.array([3.0, 0.0, 0.0]))  # Initial transform for sphere 2
tf2_end = Transform(np.array([1.0, 0.0, 0.0]))  # Final transform for sphere 2

# Define number of steps for interpolation
num_steps = 999

# Perform swept collision detection
collision_detected = False
for i in range(num_steps + 1):
    t = i / num_steps

    # Interpolate transforms manually
    tf1_interpolated = Transform(np.array([0.0, 0.0, 0.0]))  # Initialize interpolated transform for sphere 1
    tf2_interpolated = Transform(np.array([0.0, 0.0, 0.0]))  # Initialize interpolated transform for sphere 2

    # Perform linear interpolation for translation
    translation1 = (1 - t) * tf1_start.getTranslation() + t * tf1_end.getTranslation()
    translation2 = (1 - t) * tf2_start.getTranslation() + t * tf2_end.getTranslation()

    tf1_interpolated.setTranslation(translation1)
    tf2_interpolated.setTranslation(translation2)

    # Create collision objects with interpolated transforms
    o1 = CollisionObject(sphere1, tf1_interpolated)
    o2 = CollisionObject(sphere2, tf2_interpolated)

    # Create collision request and result
    request = CollisionRequest()
    result = CollisionResult()

    # Perform collision check
    collide(o1, o2, request, result)

    # Check collision result
    if result.is_collision:
        collision_detected = True
        print(f"Collision detected at time step {i}/{num_steps}")
        for contact in result.contacts:
            print(f"Contact between {contact.o1} and {contact.o2}")
        break

if not collision_detected:
    print("No collision detected during the motion.")
