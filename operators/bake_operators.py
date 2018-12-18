import bpy

from .. import bake

class BakePhysiKaSimulation(bpy.types.Operator):
    bl_idname = "physika_operators.bake_physika_simulation"
    bl_label = "Bake Fluid Simulation"
    bl_description = "Run fluid simulation"
    bl_options = {'REGISTER'}


    def export_model(self):
        filepath = '.config/blender/2.79/scripts/addons/blender-physics/lib/simple-translation/build/input.obj'
        bpy.ops.export_scene.obj(filepath = filepath, use_materials=False, use_triangles=True, use_normals=False, use_uvs=False)
        
    def run_simulation(self, obj):
        self.export_model();
        res = bake.bake()
        if res is 0:
            
    
    def execute(self, context):
        print(context.scene)
        obj = context.scene.objects.active
        if obj.physika.is_active is True:
            self.run_simulation(obj)
        return {'RUNNING_MODAL'}
def register():
    bpy.utils.register_class(BakePhysiKaSimulation)

def unregister():
    bpy.utils.unregister_class(BakePhysiKaSimulation)
