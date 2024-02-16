cmake_minimum_required(VERSION 3.16)
project(BOLERO 
	VERSION 1.0.0
	DESCRIPTION "Behavior Learning and Optimization for Robots")

enable_testing()

find_package(PkgConfig REQUIRED)
pkg_check_modules(lib_manager REQUIRED IMPORTED_TARGET lib_manager)
pkg_check_modules(configmaps REQUIRED IMPORTED_TARGET configmaps)

add_subdirectory(src)

add_custom_target(pip_install ALL
	COMMAND pip install .
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python
)

