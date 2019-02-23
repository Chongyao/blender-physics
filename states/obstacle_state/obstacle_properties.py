import bpy
from bpy.props import (
    PointerProperty,
    CollectionProperty
)


class physika_obj_ptr(bpy.types.PropertyGroup):
    obj_ptr = PointerProperty(
        name = "Obj_Pointer",
        type = bpy.types.Object
    )

class physika_obstacles(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.physika_obstacles = PointerProperty(
            name="PhysiKa Obstacles",
            type= cls
        )

        cls.objs = CollectionProperty(
            type = physika_obj_ptr
        )

def register():
    bpy.utils.register_class(physika_obj_ptr)
    bpy.utils.register_class(physika_obstacles)

def unregister():
    bpy.utils.unregister_class(physika_obj_ptr)
    bpy.utils.unregister_class(physika_obstacles)
