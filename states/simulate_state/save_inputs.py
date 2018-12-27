import bpy
import json,os
from ..parameter_state import discrete_types

def valid_common_props(string):
    return string.startswith('common')

def save_model(context, discrete_method, input_path):
    obj = context.scene.objects.active
    raw_path = os.getcwd()
    os.chdir(input_path)
    file_path = os.path.join('./', obj.name+'.ply')
    bpy.ops.export_mesh.ply(filepath = file_path, use_mesh_modifiers=False, use_normals=False, use_uv_coords=False, use_colors=False)
    os.chdir(raw_path)


def save_constraint(context, discrete_method, input_path):
    obj = context.scene.objects.active
    raw_path = os.getcwd()
    os.chdir(input_path)
    file_path = os.path.join('./', obj.name+'.csv')
    vs = [ v for v in obj.data.vertices if vg_idx in [ vg.group for vg in v.groups ] ]
    with open(file_path,'w') as f:
        f.write("vtkOriginalPointIds","Points:0","Points:1","Points:2\n")
        for v in vs:
            f.write(v.index,',',v.co[0],',',v.co[1],',',v.co[2],'\n')
    
    os.chdir(raw_path)

def save_parameters(context, discrete_method, input_path):
    raw_path = os.getcwd()
    os.chdir(input_path)
    print("here is " , os.getcwd())
    obj = context.scene.objects.active
    file_path = os.path.join('./', 'input_para.json' )


    with open(file_path) as f:
        json_paras = json.load(f)

        
    changed_paras = [prop[0] for prop in eval('discrete_types.' + discrete_method + '_parameter')]
    for para in changed_paras:
        exec('json_paras[para] = context.scene.physika_para.' + discrete_method + '.' + para)
        
    _common_paras = list(filter(valid_common_props, dir(context.scene.physika_para)))
    common_paras = [para.replace('common_', '') for para in _common_paras]
    for para in common_paras:
        exec('json_paras[para] = context.scene.physika_para.common_' + para)

    json_paras['object_name'] = obj.name
    json_paras['out_dir_simulator'] = '../../output/' + obj.name
    json_paras['input_object'] = '../../input/' + obj.name +'/' + obj.name + '.vtk'
    json_paras['input_constraint'] = '../../input/' + obj.name +'/'+obj.name + '.csv'

    with open(file_path, 'w') as f:
        json.dump(json_paras, f)

    os.chdir(raw_path)
