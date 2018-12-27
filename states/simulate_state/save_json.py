# import bpy
import json,os
from ..parameter_state import discrete_types
def change_json_file(discrete_method):
    changed_paras = [prop[0] for prop in eval('discrete_types.' + discrete_method + '_parameter')]

    script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    assert script_path == 'blender-physics'
    
    with open(os.path.join(script_path,'lib',discrete_method,'input','input_para.json')) as f:
        json_paras = json.load(f)

    print(json_paras)

change_json_file('mass_spring')
