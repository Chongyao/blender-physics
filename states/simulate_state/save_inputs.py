import bpy
import json,os
from ..parameter_state import discrete_types
import shutil
def valid_common_props(string):
    return string.startswith('common')

def clear_cache(context, discrete_method, input_path):
    obj_name = context.scene.physika.physika_object_name
    raw_path = os.getcwd()
    os.chdir(input_path)

    cache_dir = os.path.join('../', 'output', obj_name)
    print(cache_dir)
    if(os.path.exists(cache_dir)):
        shutil.rmtree(cache_dir)
        print("clear cache")
    
    os.chdir(raw_path)
    
def save_model(context, discrete_method, input_path):
    #TODO get physika object
    obj = context.scene.objects.active
    ext = eval('context.scene.physika_para.' + discrete_method + '.blender.input_format')
    raw_path = os.getcwd()
    os.chdir(input_path)

    if_tetgen = False
    if(ext == 'obj'):
        file_path = os.path.join('./', obj.name + '.obj')
        bpy.ops.export_scene.obj(filepath = file_path, use_mesh_modifiers=False, use_normals=False)
        if_tetgen = False
    elif(ext == 'vtk'):
        file_path = os.path.join('./', obj.name + '.ply')
        bpy.ops.export_mesh.ply(filepath = file_path, use_mesh_modifiers=False, use_normals=False, use_uv_coords=False, use_colors=False)
        if_tetgen = True 
    os.chdir(raw_path)
    return if_tetgen
        


def save_constraint(context, input_path):
    obj = context.scene.objects.active
    raw_path = os.getcwd()
    os.chdir(input_path)
    file_path = os.path.join('./', obj.name+'.csv')
    vg_idx = -1
    for group in obj.vertex_groups:
        if group.name == 'PhysikaConstraint':
            vg_idx = group.index
            
            
    vs = [ v for v in obj.data.vertices if vg_idx in [ vg.group for vg in v.groups ] ]
    with open(file_path,'w') as f:
        f.write('"vtkOriginalPointIds","Points:0","Points:1","Points:2"\n')
        for v in vs:
            f.write(str(v.index) + ',' + str(v.co[0]) +','+str(v.co[1]) + ',' + str(v.co[2]) + '\n')
    
            os.chdir(raw_path)

# def save_parameters(context, discrete_method, input_path):
#     raw_path = os.getcwd()
#     os.chdir(input_path)
#     print("here is " , os.getcwd())
#     obj = context.scene.objects.active
#     file_path = os.path.join('./', 'input_para.json' )


#     with open(file_path) as f:
#         json_paras = json.load(f)

        
#     changed_paras = [prop[0] for prop in eval('discrete_types.' + discrete_method + '_parameter')]
#     for para in changed_paras:
#         exec('json_paras[para] = context.scene.physika_para.' + discrete_method + '.' + para)
        
#     _common_paras = list(filter(valid_common_props, dir(context.scene.physika_para)))
#     common_paras = [para.replace('common_', '') for para in _common_paras]
#     for para in common_paras:
#         exec('json_paras[para] = context.scene.physika_para.common_' + para)

#     json_paras['object_name'] = obj.name
#     json_paras['out_dir_simulator'] = '../../output/' + obj.name
#     json_paras['input_object'] = '../../input/' + obj.name +'/' + obj.name + '.vtk'
#     json_paras['input_constraint'] = '../../input/' + obj.name +'/'+obj.name + '.csv'

#     with open(file_path, 'w') as f:
#         json.dump(json_paras, f,indent = 4)

#     os.chdir(raw_path)

def save_parameters(context, discrete_method, input_path):
    raw_path = os.getcwd()
    os.chdir(input_path)
    file_path = os.path.join('../', 'blender_physics.json' )

    #read json template 
    json_temp_path = '../../../states/parameter_state/para_temp.json'
    print(json_temp_path)
    with open(json_temp_path, 'r') as json_temp_file:
        json_temp = json.load(json_temp_file)[discrete_method]

    #set parameters in json
    para_props = eval('context.scene.physika_para.' + discrete_method)
    for cate, paras in json_temp.items():
        for para, value in paras.items():
            json_temp[cate][para] = eval('para_props.' + cate + '.' + para)
    json_temp['blender']['surf'] = context.scene.physika.physika_object_name
    
    #write json        
    with open(file_path, 'w') as f:
        json.dump(json_temp, f, indent = 4)

    os.chdir(raw_path)

    
