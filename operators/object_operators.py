# Blender FLIP Fluid Add-on
# Copyright (C) 2018 Ryan L. Guy
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import bpy,importlib.util,os,types,sys


class PhysiKaAdd(bpy.types.Operator):
    bl_idname = "physika_operators.physika_add"
    bl_label = "Add PhysiKa object"
    bl_description = "Add active object as PhysiKa"
    bl_options = {'REGISTER'}

    def init_state_graph(self, constext):

        # script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # sys.path.append(script_path + '/states')
        # state_names = [f.split('.')[0] for f in os.listdir(script_path + '/states') if f.endswith('_state.py')]
        # print(state_names)
        # for state in state_names:
        #     importlib.import_module(state)
        
        #     state_path = script_path + '/states/' + state + '.py'
        #     print(state_path)
        #     loader = importlib.machinery.SourceFileLoader(state, state_path)
        #     mod = types.ModuleType(loader.name)
        #     loader.exec_module(mod)
        #     mod.register_state()
        """TODO auto import"""
        from ..states import (simulate_state,
                              constraint_state,
                              animate_state)
        simulate_state.register_state()
        constraint_state.register_state()
        animate_state.register_state()
        

        
    def execute(self, context):

        obj = context.scene.objects.active
        obj.physika.is_active = True
        context.scene.physika.physika_object_name = obj.name

        self.init_state_graph(context)
        return {'FINISHED'}


class PhysiKaRemove(bpy.types.Operator):
    bl_idname = "physika_operators.physika_remove"
    bl_label = "Remove PhysiKa object"
    bl_description = "Remove PhysiKa settings from Object"
    bl_options = {'REGISTER'}
    
    def uninit_state_graph(self, context):
        context.scene.physika_state_graph.clear()
        
    def execute(self, context):
        obj = context.scene.objects.active
        # obj.physika.object_type = 'TYPE_NONE'
        obj.physika.is_active = False
        context.scene.physika.physika_object_name = ''
        self.uninit_state_graph(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(PhysiKaAdd)
    bpy.utils.register_class(PhysiKaRemove)


def unregister():
    bpy.utils.unregister_class(PhysiKaAdd)
    bpy.utils.unregister_class(PhysiKaRemove)
