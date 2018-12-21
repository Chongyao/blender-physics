import bpy

class animate_panel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "physics"
    bl_category = "PhysiKa"
    bl_label = "Animate"

    @classmethod
    def poll(cls, context):
        obj_props = context.scene.objects.active.physika
        return obj_props.is_active

    def draw(self, context):
        obj_props = context.scene.objects.active.physika

        box = self.layout.box()

        column = box.column(align=True)
        column.operator("physika_operators.animate",
                          text = "Animate")


def register():
    bpy.utils.register_class(animate_panel)

def unregister():
    bpy.utils.unregister_class(animate_panel)
