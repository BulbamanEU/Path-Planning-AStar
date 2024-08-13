import heapq
import math
import bpy
from AStar3D import paths


def draw_path(path):
    scale = 1
    curve_data = bpy.data.curves.new(name="PathCurve", type='CURVE')
    curve_data.dimensions = '3D'
    polyline = curve_data.splines.new('POLY')
    polyline.points.add(len(path) - 1)

    for i, point in enumerate(path):
        polyline.points[i].co = (point[0] / scale, point[1] / scale, point[2] / scale, 1)

    curve_object = bpy.data.objects.new("Path", curve_data)
    bpy.context.collection.objects.link(curve_object)

for path in paths:
    draw_path(path)
