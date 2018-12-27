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

if "bpy" in locals():
    import importlib
    reloadable_modules = [
        'constraint_state',
        'animate_state',
        'simulate_state',
        'parameter_state',
        'export_state'
    ]
    for module_name in reloadable_modules:
        if module_name in locals():
            importlib.reload(locals()[module_name])

import bpy

from . import (
    simulate_state,
    constraint_state,
    animate_state,
    parameter_state,
    export_state
)


def register():
    constraint_state.register()
    simulate_state.register()
    animate_state.register()
    parameter_state.register()
    export_state.register()

def unregister():
    constraint_state.unregister()
    simulate_state.unregister()
    animate_state.unregister()
    parameter_state.unregister()
    export_state_unregister()
