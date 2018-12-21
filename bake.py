import bpy,subprocess,shlex,os,pathlib



def bake():
    """ Wirte by this way temporarily"""
    raw_path = os.getcwd()
    script_path = os.path.dirname(os.path.realpath(__file__))
    assert os.path.basename(script_path) is 'blender-physics'
    os.chdir(script_path)
    os.chdir('lib/simple-translation/build')
    
    res = subprocess.run(['./simple-translation', '../input/input.obj','../output'])
    os.chdir(raw_path)
    return res.returncode
