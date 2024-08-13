import numpy as np


def interpolate_position(path, velocity, t):
    """
    Interpolate the position of the agent at time t.

    :param path: List of waypoints [(x1, y1, z1), (x2, y2, z2), ...]
    :param velocity: Speed at which the agent moves
    :param t: Time to interpolate the position for
    :return: Interpolated position at time t
    """
    total_length = 0
    segments = []

    for i in range(1, len(path)):
        segment = np.linalg.norm(np.array(path[i]) - np.array(path[i - 1]))
        segments.append(segment)
        total_length += segment

    distance_covered = t * velocity

    for i in range(1, len(path)):
        if distance_covered <= segments[i - 1]:
            ratio = distance_covered / segments[i - 1]
            return np.array(path[i - 1]) + ratio * (np.array(path[i]) - np.array(path[i - 1]))
        distance_covered -= segments[i - 1]

    return np.array(path[-1])


def detect_path_collision(path1, velocity1, radius1, path2, velocity2, radius2, time_interval, max_time):
    """
    Detect if two agents collide at any point along their paths and return the collision coordinates.

    :param path1: Waypoints of the first agent [(x1, y1, z1), (x2, y2, z2), ...]
    :param velocity1: Velocity of the first agent
    :param radius1: Radius of the first agent
    :param path2: Waypoints of the second agent [(x1, y1, z1), (x2, y2, z2), ...]
    :param velocity2: Velocity of the second agent
    :param radius2: Radius of the second agent
    :param time_interval: Time interval for checking collisions
    :param max_time: Maximum time to check for collisions
    :return: Tuple (collision_detected, collision_coordinates, time_of_collision)
             where collision_detected is a boolean, collision_coordinates is a tuple (x, y, z), and time_of_collision is the time step at which collision occurs.
    """
    t = 0
    while path1 and path2:
        pos1 = interpolate_position(path1, velocity1, t)
        pos2 = interpolate_position(path2, velocity2, t)

        distance = np.linalg.norm(pos1 - pos2)

        if distance <= radius1 + radius2:
            # Calculate the average position as the collision point (simplified assumption)
            collision_coordinates = (pos1 + pos2) / 2.0
            return True, tuple(collision_coordinates), t

        t += time_interval

    return False, None, None


# Example usage:

path1 = [(1, 2, 3), (1, 3, 3), (1, 4, 3), (1, 5, 3), (1, 6, 3), (1, 6, 4), (1, 6, 5), (2, 6, 5), (2, 6, 6), (2, 6, 7), (3, 6, 7), (4, 6, 7), (4, 6, 8), (4, 6, 9), (5, 6, 9), (5, 6, 10), (5, 6, 11), (5, 7, 11), (5, 7, 12), (6, 7, 12), (6, 7, 13), (6, 7, 14), (7, 7, 14), (7, 7, 15), (7, 7, 16), (8, 7, 16), (9, 7, 16), (9, 8, 16), (9, 8, 17), (9, 8, 18), (9, 8, 19), (9, 9, 19), (9, 10, 19), (9, 10, 20), (10, 10, 20), (11, 10, 20), (11, 11, 20), (11, 12, 20), (11, 12, 21), (11, 12, 22), (12, 12, 22), (12, 12, 23), (13, 12, 23), (14, 12, 23), (15, 12, 23), (15, 13, 23), (15, 13, 24), (15, 13, 25), (15, 13, 26), (16, 13, 26), (16, 13, 27), (16, 13, 28), (16, 14, 28), (16, 15, 28), (16, 15, 29), (17, 15, 29), (17, 16, 29), (17, 16, 30), (17, 16, 31), (18, 16, 31), (19, 16, 31), (20, 16, 31), (21, 16, 31), (22, 16, 31), (23, 16, 31), (23, 17, 31), (23, 18, 31), (24, 18, 31), (25, 18, 31), (26, 18, 31), (27, 18, 31), (28, 18, 31), (29, 18, 31), (30, 18, 31), (30, 19, 31), (30, 19, 32), (30, 19, 33), (30, 19, 34), (31, 19, 34), (31, 20, 34), (31, 21, 34), (32, 21, 34), (32, 22, 34), (33, 22, 34), (33, 22, 35), (33, 22, 36), (34, 22, 36), (34, 22, 37), (34, 22, 38), (35, 22, 38), (36, 22, 38), (36, 22, 39), (37, 22, 39), (38, 22, 39), (39, 22, 39), (40, 22, 39), (40, 23, 39), (41, 23, 39), (42, 23, 39), (42, 23, 40), (43, 23, 40), (43, 24, 40), (43, 24, 41), (43, 24, 42), (43, 24, 43), (43, 24, 44), (44, 24, 44), (44, 25, 44), (44, 25, 45), (45, 25, 45), (45, 26, 45), (45, 26, 46), (46, 26, 46), (46, 27, 46), (46, 27, 47), (47, 27, 47), (47, 27, 48), (47, 27, 49), (47, 28, 49), (47, 28, 50), (47, 29, 50), (47, 30, 50), (47, 30, 51), (47, 30, 52), (47, 31, 52), (47, 32, 52), (47, 33, 52), (47, 33, 53), (47, 33, 54), (47, 33, 55), (47, 33, 56), (47, 33, 57), (47, 34, 57), (47, 35, 57), (47, 35, 58), (48, 35, 58), (48, 36, 58), (48, 37, 58), (48, 38, 58), (48, 39, 58), (48, 39, 59), (49, 39, 59), (50, 39, 59), (50, 40, 59), (50, 41, 59), (50, 41, 60), (50, 41, 61), (51, 41, 61), (52, 41, 61), (53, 41, 61), (53, 42, 61), (53, 43, 61), (54, 43, 61), (55, 43, 61), (55, 44, 61), (55, 45, 61), (55, 45, 62), (56, 45, 62), (56, 45, 63), (56, 46, 63), (56, 47, 63), (56, 48, 63), (57, 48, 63), (57, 49, 63), (57, 50, 63), (58, 50, 63), (58, 51, 63), (58, 51, 64), (59, 51, 64), (60, 51, 64), (61, 51, 64), (62, 51, 64), (63, 51, 64), (63, 51, 65), (63, 52, 65), (63, 53, 65), (63, 53, 66), (63, 53, 67), (63, 54, 67), (63, 54, 68), (64, 54, 68), (64, 54, 69), (64, 54, 70), (64, 55, 70), (64, 56, 70), (64, 57, 70), (64, 57, 71), (64, 57, 72), (65, 57, 72), (65, 58, 72), (65, 59, 72), (65, 60, 72), (65, 61, 72), (65, 62, 72), (66, 62, 72), (66, 62, 73), (67, 62, 73), (68, 62, 73), (69, 62, 73), (69, 63, 73), (69, 63, 74), (69, 63, 75), (69, 63, 76), (70, 63, 76), (71, 63, 76), (71, 63, 77), (71, 63, 78), (71, 64, 78), (71, 65, 78), (71, 66, 78), (71, 67, 78), (71, 68, 78), (71, 69, 78), (71, 69, 79), (71, 69, 80), (71, 69, 81), (71, 69, 82), (72, 69, 82), (72, 70, 82), (72, 71, 82), (72, 71, 83), (72, 72, 83), (72, 72, 84), (72, 73, 84), (72, 74, 84), (72, 75, 84), (72, 76, 84), (73, 76, 84), (73, 77, 84), (73, 77, 85), (73, 77, 86), (73, 77, 87), (74, 77, 87), (74, 78, 87), (74, 79, 87), (74, 80, 87), (74, 81, 87), (74, 81, 88), (74, 82, 88), (74, 82, 89), (75, 82, 89), (76, 82, 89), (77, 82, 89), (78, 82, 89), (79, 82, 89), (79, 83, 89), (79, 84, 89), (80, 84, 89), (80, 85, 89), (80, 85, 90), (80, 85, 91), (81, 85, 91), (82, 85, 91), (83, 85, 91), (83, 85, 92), (83, 85, 93), (83, 85, 94), (83, 86, 94), (83, 86, 95), (84, 86, 95), (85, 86, 95), (86, 86, 95), (87, 86, 95), (87, 87, 95), (87, 88, 95), (87, 89, 95), (87, 90, 95), (87, 90, 96), (87, 90, 97), (87, 91, 97), (87, 91, 98), (88, 91, 98), (89, 91, 98), (89, 92, 98), (89, 93, 98), (89, 94, 98), (89, 95, 98), (89, 96, 98), (89, 97, 98), (89, 97, 99), (90, 97, 99), (91, 97, 99), (92, 97, 99), (93, 97, 99), (93, 98, 99), (93, 99, 99), (94, 99, 99), (95, 99, 99), (96, 99, 99), (96, 100, 99), (96, 100, 100), (97, 100, 100), (98, 100, 100), (99, 100, 100), (100, 100, 100)]

path2 = [(2, 2, 3), (3, 2, 3), (4, 2, 3), (4, 3, 3), (4, 4, 3), (4, 5, 3), (5, 5, 3), (5, 5, 4), (5, 5, 5)]

velocity1 = 1.0  # units per second
velocity2 = 1.0  # units per second
radius1 = 0.5  # units
radius2 = 0.5  # units

time_interval = 0.1  # seconds
max_time = 5.0  # seconds

collision, collision_coords, collision_time = detect_path_collision(path1, velocity1, radius1, path2, velocity2,
                                                                    radius2, time_interval, max_time)

if collision:
    print(f"Collision detected at coordinates {collision_coords} at time {collision_time} seconds.")
else:
    print("No collision detected.")
