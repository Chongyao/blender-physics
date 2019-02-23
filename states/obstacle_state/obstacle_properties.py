import bpy
from bpy.props import (
    PointerProperty,
    CollectionProperty,
    IntProperty
)

def scene_chosenobject_poll(self, object):
    physika_obj_name = bpy.context.scene.physika.physika_object_name
    return object.type == 'MESH' and object.name != physika_obj_name

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

    objs = CollectionProperty(
            type = physika_obj_ptr
        )
    index = IntProperty(default = -1)

    chosen_obj = PointerProperty(
        name = "chosen obj",
        type = bpy.types.Object,
        poll = scene_chosenobject_poll
    )

def register():
    bpy.utils.register_class(physika_obj_ptr)
    bpy.utils.register_class(physika_obstacles)

def unregister():
    bpy.utils.unregister_class(physika_obj_ptr)
    bpy.utils.unregister_class(physika_obstacles)
