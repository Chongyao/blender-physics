import bpy,subprocess,shlex,os,pathlib



def tetgen(discrete_method, obj_name):
    raw_path = os.getcwd()
    script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    
    os.chdir(os.path.join(script_path, 'lib', 'tetgen1.5.1','build'))
    
    exe = './tetgen'
    model_path = '../../' + discrete_method + '/input/' + obj_name +'.ply'
    res_path = '../../' + discrete_method + '/input/' + obj_name +'.1.vtk'
    vtk_path = '../../' + discrete_method + '/input/' + obj_name +'.vtk'
    res = subprocess.run(['./tetgen', '-k', model_path])
    os.rename(res_path, vtk_path)
    os.chdir(raw_path)
    return res

def bake(discrete_method, obj):
    """ Wirte by this way temporarily"""
    tet_res = tetgen(discrete_method, obj.name)
    
    raw_path = os.getcwd()
    script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    os.chdir(os.path.join(script_path,'lib', discrete_method,'build','bin'))
    json_path = '../../input/input_para.json'
    sim_res = subprocess.run(['./' + discrete_method, json_path])
    os.chdir(raw_path)
    return res.returncode and sim_res.returncode