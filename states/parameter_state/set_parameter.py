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
        cls.frames = IntProperty(
            name = "num of frames",
            subtype = 'UNSIGNED',
            default = 50,
            step = 10
        )
        cls.delt_t = FloatProperty(
            name = "delt_t",
            description = 'delt time between each iteraton step instead of delt time between each frame',
            min = 0.01,
            max = 0.1,
            step = 1
        )
        
        cls.frame_rate = IntProperty(
            name = 'frame rate',
            description = 'num of frames per second',
            default = 10,
            subtype = "UNSIGNED",
            max = 100,
            update = lambda self, context: self._update_frame_rate(context)
        )

        def _update_frame_rate(self, context):
            if self.frame_rate >  1/self.delt_t:
                self.frame_rate = int(1/self.delt_t)
        
            
        
    @classmethod
    def unregister(cls):
        del bpy.types.Scene.physika_discrete
        

# class union_prameter():
#     class
def add_specific_discrete_properties():
    for enum in discrete_types.discrete_method:
        exec('class physika_para_' + enum[1] + '(bpy.types.PropertyGroup):pass')
        for paras in eval('discrete_type.' + enum[1] + '_parameter'):
            
            pass   
        setattr(physika_para, enum[1], PointerProperty(type=eval('physika_para_' + enum[1])))

def register():
    bpy.utils.register_class(physika_para)
    bpy.types.Scene.physika_para = PointerProperty(type=physika_para)


def unregister():
    bpy.utils.unregister_class(physika_para)
    del bpy.types.Scene.physika_para

