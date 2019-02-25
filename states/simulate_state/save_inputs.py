import bpy
import json,os
from ..parameter_state import discrete_types
import shutil
def valid_common_props(string):
    return string.startswith('common')

def clear_cache(context, discrete_method, input_path):
    obj_name = context.scene.physika.physika_object_name
    raw_path = os.getcwd()
    os.chdir(os.path.dirname(input_path))

    if(os.path.exists('input')):
        shutil.rmtree('input')
        os.makedirs('input')
        
    cache_dir = os.path.join('output', obj_name)
    if(os.path.exists(cache_dir)):
        shutil.rmtree(cache_dir)
        
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
        bpy.ops.export_scene.obj(filepath = file_path, use_mesh_modifiers=False, use_normals=False, axis_forward='Y', axis_up='Z', keep_vertex_order=True, use_materials=False, use_selection = True)
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
    vs_world = [obj.matrix_world * v_local.co for v_local in vs]
    with open(file_path,'w') as f:
        f.write('"vtkOriginalPointIds","Points:0","Points:1","Points:2"\n')
        for v_world,v in zip(vs_world, vs):
            f.write(str(v.index) + ',' + str(v_world[0]) +','+str(v_world[1]) + ',' + str(v_world[2]) + '\n')
    
            os.chdir(raw_path)



def save_parameters(context, discrete_method, input_path):
    raw_path = os.getcwd()
    os.chdir(input_path)
    file_path = os.path.join('../', 'blender_physics.json' )

    #read json template 
    json_temp_path = '../../../states/parameter_state/para_temp.json'
    print(json_temp_path)
    with open(json_temp_path, 'r') as json_temp_file:
        temp_data = json.load(json_temp_file)

    common_data = temp_data['common']

    json_temp = temp_data[discrete_method]
    json_temp['common'] = common_data
    #set parameters in json
    para_props = context.scene.physika_para
    for cate, paras in json_temp.items():
        for para, value in paras.items():
            if(cate == 'common'):
                json_temp[cate][para] = eval('para_props.common.' + para)
            else:
                json_temp[cate][para] = eval('para_props.' + discrete_method + '.'+ cate + '.' + para)
    json_temp['blender']['surf'] = context.scene.physika.physika_object_name
    print(json_temp)    
    #write json        
    with open(file_path, 'w') as f:
        json.dump(json_temp, f, indent = 4)

    os.chdir(raw_path)

    
def save_obstacles(context, input_path):
    raw_path = os.getcwd()
    os.chdir(input_path)
    if not os.path.exists('obstacles'):
        os.makedirs('obstacles')
    os.chdir('obstacles')

    physika_obj = context.scene.objects.active
    physika_obj.select = False

    obstacles = context.scene.physika_obstacles.objs
    for obsta in obstacles:
        obsta.obj_ptr.select = True
        
        file_path = os.path.join('./', obsta.obj_ptr.name + '.obj')
        bpy.ops.export_scene.obj(filepath = file_path, use_mesh_modifiers=False, use_normals=False, axis_forward='Y', axis_up='Z', keep_vertex_order=True, use_materials=False, use_selection = True, use_triangles = True)

        obsta.obj_ptr.select = False

    physika_obj.select = True
    os.chdir(raw_path)
