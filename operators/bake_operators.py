import bpy,os

from .. import bake

class BakePhysiKaSimulation(bpy.types.Operator):
    bl_idname = "physika_operators.bake_physika_simulation"
    bl_label = "Bake Fluid Simulation"
    bl_description = "Run fluid simulation"
    bl_options = {'REGISTER'}


    def export_model(self):
        script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        export_path = os.path.join(script_path, 'lib', 'simple-translation','input','input.obj')
        bpy.ops.export_scene.obj(filepath = export_path, axis_forward='Y', axis_up='Z',use_materials=False, use_triangles=True, use_normals=False, use_uvs=False)
        
    def run_simulation(self, obj):
        self.export_model();
        res = bake.bake()
        if res is 0:
            obj.physika.bake.is_bake_finished = True
            
    
    
    def execute(self, context):
        print(os.path.realpath(__file__))
        obj = context.scene.objects.active
        if obj.physika.is_active is True:
            self.run_simulation(obj)
        return {'RUNNING_MODAL'}
def register():
    bpy.utils.register_class(BakePhysiKaSimulation)

def unregister():
    bpy.utils.unregister_class(BakePhysiKaSimulation)
