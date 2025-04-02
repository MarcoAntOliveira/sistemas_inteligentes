cmake_minimum_required(VERSION 3.10)

# Nome do projeto
project(ML_Examples)

# Definir o padrão C++ para C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Adicionar executáveis
# add_executable(elastic_net elastic_net.cpp)
# add_executable(linear_regression regressions/linear_regression.cpp)
# add_executable(test regressions/function.hpp main.cpp)
add_executable(test datasets/dataset.hpp main.cpp)
# Encontrar a biblioteca Eigen3
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

# Incluir diretórios
target_include_directories(test PRIVATE ${EIGEN3_INCLUDE_DIR})
# target_include_directories(linear_regression PRIVATE ${EIGEN3_INCLUDE_DIR})
# target_include_directories(decision_tree PRIVATE ${EIGEN3_INCLUDE_DIR})
