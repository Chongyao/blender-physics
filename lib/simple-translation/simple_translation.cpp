#include <libigl/include/igl/readOBJ.h>
#include <libigl/include/igl/writeOBJ.h>
#include <Eigen/Core>
#include <string>
#include <iostream>
using namespace Eigen;
using namespace igl;
using namespace std;
int main(int argc, char** argv){

  
  
  MatrixXi surf;
  MatrixXd nods;
  cout << argv[1] << endl;
  readOBJ(argv[1], nods, surf);



  string output_path = argv[2];
  
  for(size_t i = 0; i < 20; ++i){
    nods.col(0) += VectorXd::Ones(nods.rows())*2;
    
    string res = output_path + "/res" + to_string(i) + ".obj";
    writeOBJ(res.c_str(), nods, surf);

  }



  cout << "Done " << endl;
  return 0;
}