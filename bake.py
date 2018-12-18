import bpy,subprocess,shlex



def bake():
    """ Wirte by this way temporarily"""
    physika_exe_path = "/home/zcy/.config/blender/2.79/scripts/addons/blender-physics/lib/simple-translation/build/"
    physika_exe = "simple-translation"
    exe_cmd = physika_exe_path + physika_exe  + " " + physika_exe_path + "input.obj" + " " + physika_exe_path + "output"
    args = shlex.split(exe_cmd)
    res = subprocess.run(args)
    return res.returncode
