#    Addon info
bl_info = {
    "name": "Sprytile Painter",
    "author": "Jeiel Aranal",
    "location": "View3D > UI panel > Add meshes",
    "category": "Paint"
    }

if "bpy" in locals():
    import imp
    imp.reload(sprytile_modal)
    imp.reload(sprytile_panel)
else:
    from . import sprytile_modal, sprytile_panel

import bpy
from bpy.props import EnumProperty, IntProperty

def setup_props():
    # Scene properties
    bpy.types.Scene.sprytile_normalmode = EnumProperty(
        items = [
            ("X",           "X",    "World X-Axis",     1),
            ("Y",           "Y",    "World Y-Axis",     2),
            ("Z",           "Z",    "World X-Axis",     3),
            ("LAST_NORMAL", "Last", "Last Used Normal", 4)
        ],
        name = "Normal Mode",
        description = "Normal to create in mesh in"
    )

    bpy.types.Scene.sprytile_paintmode = EnumProperty(
        items = [
            ("PAINT",       "Paint",        "", 1),
            ("SET_NORMAL",  "Set Normal",   "", 2)
        ],
        name = "Sprytile Paint Mode",
        description = "Sprytile Paint tool mode"
    )

    # Object properties
    bpy.types.Object.sprytile_matid = IntProperty(
        name = "Material ID",
        description = "Material index used for object"
    )

def teardown_props():
    del bpy.types.Scene.sprytile_normalmode
    del bpy.types.Scene.sprytile_paintmode
    del bpy.types.Object.sprytile_matid

def register():
    bpy.utils.register_module(__name__)
    setup_props()

def unregister():
    bpy.utils.unregister_module(__name__)
    teardown_props()

if __name__ == "__main__":
    register()