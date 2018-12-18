project(simple-translation)
cmake_minimum_required(VERSION 2.8)

list(APPEND CMAKE_CXX_FLAGS "-fopenmp -std=c++11 -o3 -fpermissive")

include_directories(${PROJECT_SOURCE_DIR})

find_package(Eigen3 REQUIRED)
if(EIGEN3_FOUND)
  message("-- Eigen @ ${EIGEN3_INCLUDE_DIR}")
  message("-- Eigen version: ${EIGEN3_VERSION}")
  include_directories(${EIGEN3_INCLUDE_DIR})
endif(EIGEN3_FOUND)

add_executable(simple-translation simple_translation.cpp)
