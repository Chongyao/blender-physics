import bpy,os

class PhysikaMeshCache(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        pass

    @classmethod
    def unregister(cls):
        pass


    def get_mesh_filepath(self, frame_id):
        file_name = 'res' + str(frame_id)
        file_path = 'lib/simple-translation/output/'
        return file_path + file_name

    def import_function(self, file_path):
        """ simple read form obj"""
        with open(file_path) as f:
            obj_data = f.readlines()

        vertexs =[]
        triangles = []

        for line in obj_data:
            if line[0][0] is 'v':
                vertexs.append(tuple(map(int, a[0].replace('v','').replace('\n','').split())))
            elif line[0][0] is 'f':
                triangles.append(tuple(map(float, a[0].replace('f','').replace('\n','').split())))
                
        return vertexs, triangles
    
    def import_frame_mesh(self, frame_id):
        raw_path = os.getcwd()
        script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        assert os.path.basename(script_path) is 'blender-physics'
        os.chdir(script_path)

        file_path = self.get_mesh_filepath(frame_id)
        
        vertexs, triangles = self.import_function(file_path)

        new_mesh_data_name = 'frame' + str(frame_id)
        new_mesh_data = bpy.data.meshes.new(new_mesh_data_name)
        new_mesh_data.from_pydata(vertices, [], triangles)

        

        
        

        
