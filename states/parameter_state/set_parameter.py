import os
import bpy
from .para_temp import Property_add_subproperty
# from . import discrete_types
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty
        )
property_adder = Property_add_subproperty()

# add parameters in specific method
# for enum in discrete_types.discrete_method:
#     class_name = 'physika_para_' + enum[1]
#     exec('class ' + class_name + '(bpy.types.PropertyGroup):pass')
#     for para in eval('discrete_types.' + enum[1] + '_parameter'):
#         exec('property_adder.add_' + para[1] + '_parameter(' + class_name + ', para[0], para[3])')
import json
discrete_methods = []
json_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "para_temp.json")
with open(json_file, "r") as para_temp:
    methods = json.load(para_temp)
for method, cates in methods.items():
    discrete_methods.append(method)
    exec('class physika_' + method + '(bpy.types.PropertyGroup):pass')
    for cate, paras in cates.items():
        if cate == "blender":
            continue
        exec('class ' + method + "_" + cate + '(bpy.types.PropertyGroup):pass')
        for para, value in paras.items():
            if type(value) == float:
                exec('property_adder.add_float_parameter(' + method + '_' + cate + ', para, attr_default = value)')
            elif type(value) == int:
                exec('property_adder.add_int_parameter(' + method + '_' + cate + ', para, attr_default = value)')
            elif type(value) == str:
                #TODO: add enum
                pass
        exec('setattr(physika_' + method + ', "' + cate + '", PointerProperty(type = ' + method + '_' + cate +'))')
        
types = tuple(((method, method, method) for method in discrete_methods))

class physika_para(bpy.types.PropertyGroup):
    
    @classmethod
    def register(cls):
        print(types)
        cls.physika_discrete = EnumProperty(
            name = "Setting physika discreting method",
            items = types,
            default = 'meshless'
        )
        # cls.common_frames = IntProperty(
        #     name = "num of frames",
        #     subtype = 'UNSIGNED',
        #     default = 50,
        #     step = 10
        # )
        # cls.common_delt_t = FloatProperty(
        #     name = "delt_t",
        #     description = 'delt time between each iteraton step instead of delt time between each frame',
        #     min = 0.01,
        #     max = 0.1,
        #     step = 1,
        #     default = 0.01
        # )
        
        # cls.common_frame_rate = IntProperty(
        #     name = 'frame rate',
        #     description = 'num of frames per second',
        #     default = 10,
        #     subtype = "UNSIGNED",
        #     max = 100,
        #     update = lambda self, context: self._update_frame_rate(context)
        # )

        # cls.common_gravity = FloatProperty(
        #     name = "gravity",
        #     default = 9.81
        # )

        # cls.common_density = FloatProperty(
        #     name = 'density',
        #     description = ' gravity for physika simulaton, blender build-in gravity will not work',
        #     min = 0,
        #     default = 10,
        #     step = 100
        # )

        # for enum in discrete_types.discrete_method:
        #     exec('cls.' + enum[1] + ' = PointerProperty(type = physika_para_' + enum[1] + ')')
        for method, cates in methods.items():
            exec('cls.' + method + ' = PointerProperty(type = physika_' + method + ')')
    

    def _update_frame_rate(self, context):
        if self.frame_rate >  1/self.delt_t:
            self.frame_rate = int(1/self.delt_t)
            
            
        
    @classmethod
    def unregister(cls):
        pass
        # del bpy.types.Scene.physika_discrete
        




def register():
    for method, cates in methods.items():
        for cate,paras in cates.items():
            if cate != "blender":
                exec('bpy.utils.register_class(' + method + '_' + cate + ')')
        exec('bpy.utils.register_class(physika_' + method + ')')
    bpy.utils.register_class(physika_para)
    bpy.types.Scene.physika_para = PointerProperty(type=physika_para)
def unregister():
    for method, cates in methods.items():
        for cate,paras in cates.items():
            if cate != 'blender':
                exec('bpy.utils.unregister_class(' + method + '_' + cate + ')')
        exec('bpy.utils.unregister_class(physika_' + method + ')')
    bpy.utils.unregister_class(physika_para)
    del bpy.types.Scene.physika_para

