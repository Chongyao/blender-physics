import bpy
class physika_export_operator(bpy.types.Operator):
    bl_idname = "physika_operators.export_result"
    bl_label = "Export Results"
    bl_options = {'REGISTER'}

    def execute(self, context):
        pass


def register():
    bpy.utils.register_class(physika_export_operator)

def unregister():
    bpy.utils.unregister_class(physika_export_operator)
