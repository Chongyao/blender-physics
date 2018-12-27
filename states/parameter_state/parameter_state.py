import bpy
from .base_state import *



class physika_parameter_ui(physika_base_ui):
    bl_label = 'parameter'
    physika_state = 'parameter'
    
    def draw(self, context):
        super(physika_parameter_ui, self).draw(context)


class physika_parameter_op_previous(physika_base_op_previous):
    physika_state = 'parameter'
    bl_idname = 'physika_parameter_op.previous'

    
class physika_parameter_op_next(physika_base_op_next):
    physika_state = 'parameter'
    bl_idname = 'physika_parameter_op.next'

def register_state():
    state = bpy.data.scenes['Scene'].physika_state_graph.add()
    state.curr = 'parameter'
    state.next = 'simulate'
    state.prev = 'constraint'

    
def register():
    bpy.utils.register_class(physika_parameter_op_previous)
    bpy.utils.register_class(physika_parameter_op_next)
    bpy.utils.register_class(physika_parameter_ui)

def unregister():
    bpy.utils.unregister_class(physika_parameter_op_previous)
    bpy.utils.unregister_class(physika_parameter_op_next)    
    bpy.utils.unregister_class(physika_parameter_ui)

