import bpy
from ..base_state import *



class physika_obstacle_ui(physika_base_ui):
    bl_label = 'Obstacle'
    physika_state = 'obstacle'
    
    def specific_draw(self, context):
        obj_props = context.scene.objects.active.physika

        box = self.layout.box()

        column = box.column(align=True)
        


            



class physika_obstacle_op_previous(physika_base_op_previous):
    physika_state = 'obstacle'
    bl_idname = 'physika_obstacle_op.previous'

    
class physika_obstacle_op_next(physika_base_op_next):
    physika_state = 'obstacle'
    bl_idname = 'physika_obstacle_op.next'

def register_state():
    state = bpy.data.scenes['Scene'].physika_state_graph.add()
    state.curr = 'obstacle'
    state.next = 'constraint'
    state.prev = 'None'

from . import (obstacle_operators,
               obstacle_properties)
               
def register():
    obstacle_properties.register()
    obstacle_operators.register()
    bpy.utils.register_class(physika_obstacle_op_previous)
    bpy.utils.register_class(physika_obstacle_op_next)
    bpy.utils.register_class(physika_obstacle_ui)

def unregister():
    obstacle_properties.unregister()
    obstacle_operators.unregister()
    bpy.utils.unregister_class(physika_obstacle_op_previous)
    bpy.utils.unregister_class(physika_obstacle_op_next)    
    bpy.utils.unregister_class(physika_obstacle_ui)
