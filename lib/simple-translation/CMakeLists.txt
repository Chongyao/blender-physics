project(simple-translation)
cmake_minimum_required(VERSION 2.8)

list(APPEND CMAKE_CXX_FLAGS " -std=c++11 -O3 -fpermissive")

include_directories(${PROJECT_SOURCE_DIR})
include_directories(libigl)
find_package(Eigen3 REQUIRED)
if(EIGEN3_FOUND)
  message("-- Eigen @ ${EIGEN3_INCLUDE_DIR}")
  message("-- Eigen version: ${EIGEN3_VERSION}")
  include_directories(${EIGEN3_INCLUDE_DIR})
endif(EIGEN3_FOUND)

add_executable(meshless simple_translation.cpp)
