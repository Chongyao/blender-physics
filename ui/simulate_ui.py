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


    def draw_bake_operator(self, context, box):
        column = box.column(align=True)
        column.operator("physika_operators.bake_physika_simulation",
                        text = "Bake")

    
    def draw(self, context):
        obj_props = context.scene.objects.active.physika

        column = self.layout.column()
        # column.prop(obj_props, "object_type")
        
        box = self.layout.box()

        col_test = box.column()

        self.draw_bake_operator(context, box)

    




def register():
    bpy.utils.register_class(simulation_panel)


def unregister():
    bpy.utils.unregister_class(simulation_panel)


if __name__ == "__main__":
    register()

    
