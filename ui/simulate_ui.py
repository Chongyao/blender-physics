import bpy

class simulation_panel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    # bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "physics"
    bl_category = "PhysiKa"
    bl_label = "PhysiKa"
    
    #deteminate when the panel will show
    @classmethod
    def poll(cls, context):
        obj_props = context.scene.objects.active.physika
        return obj_props.is_active
    
    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        # Big Bake
        layout.label(text="Bake:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("render.render")




def register():
    bpy.utils.register_class(simulation_panel)


def unregister():
    bpy.utils.unregister_class(simulation_panel)


if __name__ == "__main__":
    register()
