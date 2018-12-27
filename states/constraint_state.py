import bpy
from .base_state import *



class physika_constraint_ui(physika_base_ui):
    bl_label = 'Constraint'
    physika_state = 'constraint'
    
    def draw(self, context):
        super(physika_constraint_ui, self).draw(context)
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



class physika_constraint_op_previous(physika_base_op_previous):
    physika_state = 'constraint'
    bl_idname = 'physika_constraint_op.previous'

    
class physika_constraint_op_next(physika_base_op_next):
    physika_state = 'constraint'
    bl_idname = 'physika_constraint_op.next'

def register_state():
    state = bpy.data.scenes['Scene'].physika_state_graph.add()
    state.curr = 'constraint'
    state.next = 'parameter'
    state.prev = 'None'

    
def register():
    bpy.utils.register_class(physika_constraint_op_previous)
    bpy.utils.register_class(physika_constraint_op_next)
    bpy.utils.register_class(physika_constraint_ui)

def unregister():
    bpy.utils.unregister_class(physika_constraint_op_previous)
    bpy.utils.unregister_class(physika_constraint_op_next)    
    bpy.utils.unregister_class(physika_constraint_ui)

