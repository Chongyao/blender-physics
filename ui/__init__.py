import bpy

from . import(
    simulate_ui
)


def append_to_PHYSICS_PT_add_panel(self, context):
    obj = context.scene.objects.active
    if not obj.type == 'MESH':
        return

    column = self.layout.column(align=True)
    split = column.split(percentage=0.5)
    column_left = split.column()
    column_right = split.column()

    if obj.flip_fluid.is_active:
        column_right.operator(
                "flip_fluid_operators.flip_fluid_remove", 
                 text="Marvel Physics", 
                 icon='X'
                )
    else:
        icon = context.scene.flip_fluid.get_logo_icon()
        if icon is not None:
            # Icon needs to be reworked
            """
            column_right.operator(
                    "flip_fluid_operators.flip_fluid_add", 
                    text="FLIP Fluid", 
                    icon_value=context.scene.flip_fluid.get_logo_icon().icon_id
                    )
            """
            column_right.operator(
                    "flip_fluid_operators.flip_fluid_add", 
                    text="Marvel Physics", 
                    icon='MOD_FLUIDSIM'
                    )
        else:
            column_right.operator(
                    "flip_fluid_operators.flip_fluid_add", 
                    text="Marvel Physics", 
                    icon='MOD_FLUIDSIM'
                    )


def register():
    simulate_ui.register()
    bpy.types.PHYSICS_PT_add.append(append_to_PHYSICS_PT_add_panel)

def unregister():
    simulate_ui.unregister()
    bpy.types.PHYSICS_PT_add.remove(append_to_PHYSICS_PT_add_panel)

