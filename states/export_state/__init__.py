import bpy
from ..base_state import *



class physika_export_ui(physika_base_ui):
    bl_label = 'Export'
    physika_state = 'export'
    
    def draw(self, context):
        super(physika_export_ui, self).draw(context)


class physika_export_op_previous(physika_base_op_previous):
    physika_state = 'export'
    bl_idname = 'physika_export_op.previous'

    
class physika_export_op_next(physika_base_op_next):
    physika_state = 'export'
    bl_idname = 'physika_export_op.next'

def register_state():
    state = bpy.data.scenes['Scene'].physika_state_graph.add()
    state.curr = 'export'
    state.next = 'None'
    state.prev = 'Animate'

    
def register():
    bpy.utils.register_class(physika_export_op_previous)
    bpy.utils.register_class(physika_export_op_next)
    bpy.utils.register_class(physika_export_ui)

def unregister():
    bpy.utils.unregister_class(physika_export_op_previous)
    bpy.utils.unregister_class(physika_export_op_next)    
    bpy.utils.unregister_class(physika_export_ui)

