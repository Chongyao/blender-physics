import bpy
from bpy.props import(
    StringProperty,
    CollectionProperty
)
class physika_state_properties(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.physika_state = StringProperty(defalut = "None")

    @classmethod 
    def unregister(cls):
        del bpy.types.Scene.physika_state


class physika_base_state_properties(bpy.types.PropertyGroup):
    curr = StringProperty(defalut = "None")
    next = StringProperty(default = "None")
    prev = StringProperty(default = "None")

class physika_state_graph(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.physika_state_graph = CollectionProperty(type=physika_base_state_properties)

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.physika_state_graph

def register():
    bpy.utils.register_class(physika_base_state_properties)
    bpy.utils.register_class(physika_state_graph)
    bpy.utils.register_class(physika_state_properties)

def unregister():
    bpy.utils.unregister_class(physika_base_state_properties)
    bpy.utils.unregister_class(physika_state_graph)
    bpy.utils.unregister_class(physika_state_properties)
