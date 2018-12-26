import bpy
from base_ui import *

class physika_base_union(object):

    class state_ui(physika_base_ui):
        bl_label = self.physika_state

    class state_op_next(physika_base_op_next):
        bl_idname = 'physika_' + physika_state + ".next"

    class state_op_previous(physika_base_op_previous):
        bl_idname = 'physika_' + physika_state + ".previous"
    
    def __init__(self, state):
        self.physika_state = state

    def register(self):
        bpy.utils.register_class()
    
