import bpy
from .para_temp import Property_add_subproperty
from . import discrete_types
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty
        )

class physika_para(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        cls.physika_discrete = EnumProperty(
            name = "Setting physika discreting method",
            items = discrete_types.discrete_method,
            # default = 'mass_spring'
        )
    @classmethod
    def unregister(cls):
        del bpy.types.Scene.physika_discrete
        

# class union_prameter():
#     class
    

def register():
    bpy.utils.register_class(physika_para)
    bpy.types.Scene.physika_para = PointerProperty(type=physika_para)


def unregister():
    bpy.utils.unregister_class(physika_para)
    del bpy.types.Scene.physika_para

