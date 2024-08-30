import bpy

def draw_path(path, n):
    scale = 1
    curve_data = bpy.data.curves.new(name="PathCurve", type='CURVE')
    curve_data.dimensions = '3D'
    polyline = curve_data.splines.new('POLY')
    polyline.points.add(len(path) - 1)

    for i, point in enumerate(path):
        polyline.points[i].co = (point[0] / scale, point[1] / scale, point[2] / scale, 1)

    curve_object = bpy.data.objects.new(f"Path{n}", curve_data)
    bpy.context.collection.objects.link(curve_object)
