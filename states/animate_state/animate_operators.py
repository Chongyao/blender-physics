import bpy,os

"""TODO: enable AnimaAll"""
import addon_utils
#addon_utils.enable("")


from . import load_mesh

class AnimatePhysika(bpy.types.Operator):
    bl_idname = "physika_operators.animate"
    bl_label = "Animate Physika Simulation"
    bl_description = "Display Physika Simulation Results"
    bl_options = {'REGISTER'}


    def get_physika_object(self):
        for obj in bpy.data.objects:
            if obj.physika.is_active == True:
                return obj

    
    def execute(self, context):
        scene = context.scene
        ver_num = len(context.object.data.vertices)
        mesh_loader = load_mesh.MeshLoader(scene.physika_para.physika_discrete, scene.obj.name, ver_num);
        obj = self.get_physika_object()
        obj.select = True
        bpy.data.window_managers["WinMan"].key_points = True

        frames = context.scene.physika_para.common_frames

        for frame_id in range(frames):
            scene.frame_set(frame_id)

            mesh_loader.import_frame_mesh(frame_id)
            bpy.ops.anim.insert_keyframe_animall()

            
            

        return {"FINISHED"}


def register():
    bpy.utils.register_class(AnimatePhysika)

def unregister():
    bpy.utils.unregister_class(AnimatePhysika)

