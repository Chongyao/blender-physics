import bpy

class constraint_panel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "physics"
    bl_category = "PhysiKa"
    bl_label = "Constraint"

    @classmethod
    def poll(cls, context):
        obj_props = context.scene.objects.active.physika
        return obj_props.is_active

    def draw(self, context):
        obj_props = context.scene.objects.active.physika

        box = self.layout.box()

        column = box.column(align=True)
        

        
        if obj_props.enable_constraint:
            column.operator("physika_operators.enable_constraint",
                          text = "Disable Constraint")            
            column = box.column(align=True)
            split = column.split(percentage=0.5)
            column_left = split.column()
            column_right = split.column()

            column_left.operator("physika_operators.add_constraint",
                                 text = "Add Constraint")
            column_right.operator("physika_operators.clear_constraint",
                              text = "Clear Constraint")
        else:
            column.operator("physika_operators.enable_constraint",
                          text = "Enable Constraint")                        


def register():
    bpy.utils.register_class(constraint_panel)

def unregister():
    bpy.utils.unregister_class(constraint_panel)
    
