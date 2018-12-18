import bpy

class BakePhysiKaSimulation(bpy.types.Operator):
    bl_idname = "physika_operators.bake_physika_simulation"
    bl_label = "Bake Fluid Simulation"
    bl_description = "Run fluid simulation"
    bl_options = {'REGISTER'}

    def execute(self, context):
        return {'RUNNING_MODAL'}

def register():
    bpy.utils.register_class(BakePhysiKaSimulation)

def unregister():
    bpy.utils.unregister_class(BakePhysiKaSimulation)
