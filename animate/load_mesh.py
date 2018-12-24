import bpy
import os,mathutils

class MeshLoader(object):
# class MeshLoader(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        pass

    @classmethod
    def unregister(cls):
        pass


    def get_mesh_filepath(self, frame_id):
        file_name = 'res' + str(frame_id) +'.obj'
        file_path = 'lib/simple-translation/output/'
        return file_path + file_name

    def import_function(self, file_path):
        """ simple read form obj"""
        with open(file_path) as f:
            obj_data = f.readlines()

        vertexs =[]
        triangles = []

        for line in obj_data:
            if line[0] is 'v':
                vertexs.append(tuple(map(float, line.replace('v','').replace('\n','').split())))
            elif line[0] is 'f':
                triangles.append(tuple(map(int, line.replace('f','').replace('\n','').split())))
                
        print(vertexs)
        print(triangles)
        return vertexs, triangles
    
    def import_frame_mesh(self, frame_id):
        raw_path = os.getcwd()
        script_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        assert os.path.basename(script_path) == 'blender-physics', 'script_path is wrong'
        os.chdir(script_path)

        file_path = self.get_mesh_filepath(frame_id)
        
        vertexs, triangles = self.import_function(file_path)

        """NEW METHOD"""
        # vertexs_new = []
        # for v in vertexs:
        #     for coor in v:
        #         vertexs_new.append(coor)
        # cache_object = self.get_physika_object()
        #  cache_object.data.vertices.foreach_set('co', vertexs_new)
        # cache_object.data.update()



        triangles_new =[]
        for tri in triangles:
            triangles_new.append((tri[0]-1, tri[1]-1,tri[2]-1))
        print(triangles_new)
        
        """OLD METHOD"""
        new_mesh_data_name = 'frame' + str(frame_id)
        new_mesh_data = bpy.data.meshes.new(new_mesh_data_name)
        
        new_mesh_data.from_pydata(vertexs, [], triangles_new)
        print("validate: ", new_mesh_data.validate())

        cache_object = self.get_physika_object()
        print("rawdata:")
        for v in cache_object.data.vertices:
            print(v.co)

        for poly in cache_object.data.polygons:
            for loop_index in range(poly.loop_start,poly.loop_start + poly.loop_total):
                print(cache_object.data.loops[loop_index].vertex_index)
            print(" ")

        print("new mesh data::")
        for v in new_mesh_data.vertices:
            print(v.co)

        for poly in new_mesh_data.polygons:
            for loop_index in range(poly.loop_start,poly.loop_start + poly.loop_total):
                print(new_mesh_data.loops[loop_index].vertex_index)
            print(" ")        
        
        old_mesh_data = cache_object.data
        cache_object.data = new_mesh_data

        
        old_mesh_data.user_clear()
        bpy.data.meshes.remove(old_mesh_data)

        """transform"""
        #cache_object.scale = (1,1,1)
        cache_object.data.transform(mathutils.Matrix.Identity(4))        
        cache_object.matrix_world = mathutils.Matrix.Identity(4)
        print("here", cache_object.location)
        
    def get_physika_object(self):
        for obj in bpy.data.objects:
            if obj.physika.is_active == True:
                return obj
            

    def update_transforms(self):
        cache_object = self.get_cache_object()
        transvect = mathutils.Vector((self.bounds.x, self.bounds.y, self.bounds.z))
        transmat = mathutils.Matrix.Translation(-transvect)
        cache_object.data.transform(transmat)
        domain_object = self._get_domain_object()
        domain_bounds = AABB.from_blender_object(domain_object)

        domain_pos = mathutils.Vector((domain_bounds.x, domain_bounds.y, domain_bounds.z))
        scalex = (math.ceil(domain_bounds.xdim / self.bounds.dx) * self.bounds.dx) / self.bounds.width
        scaley = (math.ceil(domain_bounds.ydim / self.bounds.dx) * self.bounds.dx) / self.bounds.height
        scalez = (math.ceil(domain_bounds.zdim / self.bounds.dx) * self.bounds.dx) / self.bounds.depth
        scale = min(scalex, scaley, scalez)
        cache_object.matrix_world = mathutils.Matrix.Identity(4)
        cache_object.matrix_parent_inverse = domain_object.matrix_world.inverted()
        cache_object.scale = (scale, scale, scale)
        cache_object.location = domain_pos
    
            
        
# def register():
#     bpy.utils.register_class(PhysikaMeshCache)

# def unregister():
#     bpy.utils.unregister_class(PhysikaMeshCache)
        

        
        

        
