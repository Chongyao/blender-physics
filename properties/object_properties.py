if "bpy" in locals():
    import importlib
    reloadable_modules = [

    ]
    for module_name in reloadable_modules:
        if module_name in locals():
            importlib.reload(locals()[module_name])

import bpy
from bpy.props import(
    BoolProperty,
    EnumProperty,
    PointerProperty,
)
from .. import types
class PhysiKaObjectProperties(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Object.physika = PointerProperty(
            name="PhysiKa Object Properties",
            description="",
            type=cls
        )
        """DO NOT WHAT THIS IS FOR"""
        cls.object_type = EnumProperty(
                name="Type",
                description="Type of participation in the FLIP fluid simulation",
                items=types.object_types,
                default='TYPE_NONE',
                get=lambda self: self._get_object_type(),
                set=lambda self, value: self._set_object_type(value),
                update=lambda self, context: self._update_object_type(context),
                )
        cls.is_active = BoolProperty(default=False)
        
    @classmethod    
    def unregister(cls):
        del bpy.types.Object.physika

    def get_object_type():
        return self.object_type
    
    def set_object_type(value):
        pass

    def update_object_type(context):
        pass
        
def register():
    bpy.utils.register_class(PhysiKaObjectProperties)

def unregister():
    bpy.utils.unregister_class(PhysiKaObjectProperties)
