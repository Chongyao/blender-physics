import bpy


class physika_obstacle_list_operators(bpy.types.Operator):
    """Move items up and down, add and remove"""
    bl_idname = "physika_operators.list_action"
    bl_label = "List Actions"
    bl_description = "Move items up and down, add and remove"
    bl_options = {'REGISTER'}
    
    action = bpy.props.EnumProperty(
        items=(
            ('UP', "Up", ""),
            ('DOWN', "Down", ""),
            ('REMOVE', "Remove", ""),
            ('ADD', "Add", "")))

    def invoke(self, context, event):
        obta_props = context.scene.physika_obstacles
        idx = obta_props.index

        try:
            item = obta_props.objs[idx]
        except IndexError:
            pass
        else:
            if self.action == 'DOWN' and idx < len(obta_props.objs) - 1:
                item_next = obta_props.objs[idx+1].name
                obta_props.objs.move(idx, idx+1)
                obta_props.index += 1
                info = 'Item "%s" moved to position %d' % (item.name, obta_props.index + 1)
                self.report({'INFO'}, info)

            elif self.action == 'UP' and idx >= 1:
                item_prev = obta_props.objs[idx-1].name
                obta_props.objs.move(idx, idx-1)
                obta_props.index -= 1
                info = 'Item "%s" moved to position %d' % (item.name, obta_props.index + 1)
                self.report({'INFO'}, info)

            elif self.action == 'REMOVE':
                info = 'Item "%s" removed from list' % (obta_props.objs[idx].name)
                obta_props.index -= 1
                obta_props.objs.remove(idx)
                self.report({'INFO'}, info)
                
        if self.action == 'ADD':
            if context.object:
                item = obta_props.objs.add()
                item.name = context.object.name
                print(item.name)
                item.obj_ptr = context.object
                obta_props.index = len(obta_props.objs)-1
                info = '"%s" added to list' % (item.name)
                self.report({'INFO'}, info)
            else:
                self.report({'INFO'}, "Nothing selected in the Viewport")
        return {"FINISHED"}



def register():
    bpy.utils.register_class(physika_obstacle_list_operators)

def unregister():
    bpy.utils.unregister_class(physika_obstacle_list_operators)
