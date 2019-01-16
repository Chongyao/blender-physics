#include <libigl/include/igl/readOBJ.h>
#include <libigl/include/igl/writeOBJ.h>
#include <Eigen/Core>
#include <string>
#include <iostream>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <boost/filesystem.hpp>
using namespace Eigen;
using namespace igl;
using namespace std;
int main(int argc, char** argv){
  boost::property_tree::ptree pt;{
    const string jsonfile_path = argv[1];
    
    cout << jsonfile_path << endl;
    const size_t ext = jsonfile_path.rfind(".json");
    if (ext != std::string::npos){
      read_json(jsonfile_path, pt);
      cout << "read json successful" <<endl;
    }
    else{
      cout << "json file extension error" << endl;
      return 0;
    }
  }
  
  auto common = pt.get_child("common");
  auto blender = pt.get_child("blender");
  auto physics_para = pt.get_child("physics_para");
  auto simulation_para = pt.get_child("simulation_para");
  
  cout << "[INFO]>>>>>>>>>>>>>>>>>>>IMPORT MESH<<<<<<<<<<<<<<<<<<" << endl;
  const string mesh_name = blender.get<string>("surf");
  const string indir = "../input/";
  const string outdir = "../output/" + mesh_name;
  //mkdir
  boost::filesystem::path outpath(outdir);
  if ( !boost::filesystem::exists(outdir) )
    boost::filesystem::create_directories(outdir);

  MatrixXi surf;
  MatrixXd nods;
  readOBJ((indir+mesh_name+".obj").c_str(), nods, surf);
  cout << "surf: " << surf.rows() << " " << surf.cols() << endl << "nods: " << nods.rows() << " " << nods.cols() << endl;

  float total_time = common.get<float>("total_time");
  float delt_t = common.get<float>("time_step");
  float gravity = common.get<float>("gravity");
  size_t max_iter = static_cast<size_t>(ceil(total_time / delt_t));
  cout << "max iter is " << max_iter << endl;
  for(size_t i = 0; i < max_iter; ++i){
    nods.col(0) += VectorXd::Ones(nods.rows())*delt_t * gravity;
    
    string res = outdir + '/' + mesh_name + to_string(i) + ".obj";
    writeOBJ(res.c_str(), nods, surf);

  }

  cout << "Done " << endl;
  return 0;
}
