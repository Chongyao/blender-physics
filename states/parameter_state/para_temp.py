import bpy,sys
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty
        )
class Property_add_subproperty():
    def add_int_parameter(self, Property, attr, attr_default = 0, attr_min = -2**31, attr_max =2**31 - 1):
        assert isinstance(Property, bpy.types.PropertyGroup)
        
        setattr(Property, attr, IntProperty(
            min = attr_min,
            max = attr_max,
            default = attr_min,
        ))
        
    def add_float_parameter(self, Property, attr, attr_default = 0, atrr_min = sys.float_info.min, attr_max = sys.float_info.max):
        assert isinstance(Property, bpy.types.PropertyGroup)
        setattr(Property, attr, IntProperty(
            min = attr_min,
            max = attr_max,
            default = attr_min,
        ))
        
        
