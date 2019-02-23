import bpy
from ..base_state import *


class physika_obstacle_list(bpy.types.UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        obj = item.obj
        custom_icon = "OUTLINER_OB_%s" % obj.type
        split = layout.split(0.3)
        split.label("Index: %d" % (index))
        split.prop(obj, "name", text="", emboss=False, translate=False, icon=custom_icon)

class physika_obstacle_ui(physika_base_ui):
    bl_label = 'Obstacle'
    physika_state = 'obstacle'
    
    def specific_draw(self, context):
        obta_props = context.scene.physika_obstacles
        self.layout.template_list("physika_obstacle_list", "", obta_props, "objs", obta_props, "index", rows=2)
        print(obta_props.index)

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
    bpy.utils.register_class(physika_obstacle_list)
    bpy.utils.register_class(physika_obstacle_op_previous)
    bpy.utils.register_class(physika_obstacle_op_next)
    bpy.utils.register_class(physika_obstacle_ui)

def unregister():
    obstacle_properties.unregister()
    obstacle_operators.unregister()
    bpy.utils.unregister_class(physika_obstacle_list)
    bpy.utils.unregister_class(physika_obstacle_op_previous)
    bpy.utils.unregister_class(physika_obstacle_op_next)    
    bpy.utils.unregister_class(physika_obstacle_ui)
