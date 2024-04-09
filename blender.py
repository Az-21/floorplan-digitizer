# NOTE::This script is not meant to be run using normal python interpreter.
# It is meant to be run using Blender 3.6 LTS's python interpreter.

import bpy  # type: ignore


# Delete all default objects
bpy.ops.object.select_all(action="DESELECT")
bpy.ops.object.select_by_type(type="MESH")
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type="CURVE")
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type="LIGHT")
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type="CAMERA")
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type="CURVES")
bpy.ops.object.delete()


# Path floorplan SVG
svg_path = "path/to/floorplan.svg"

# Import SVG file
bpy.ops.import_curve.svg(filepath=svg_path)
bpy.ops.object.select_all(action="SELECT")