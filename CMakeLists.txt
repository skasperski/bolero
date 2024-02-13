cmake_minimum_required(VERSION 3.16)
project(BOLERO 
	VERSION 1.0.0
	DESCRIPTION "Behavior Learning and Optimization for Robots")

enable_testing()

find_package(PkgConfig REQUIRED)
pkg_check_modules(lib_manager REQUIRED IMPORTED_TARGET lib_manager)
pkg_check_modules(configmaps REQUIRED IMPORTED_TARGET configmaps)

add_subdirectory(src)


# Build all python components.

add_custom_command(
	OUTPUT _ranking_svm.cpp
	COMMAND python -m cython -3 --cplus _ranking_svm.pyx
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python/bolero/utils
)

add_custom_command(
	OUTPUT _wrapper.cpp
	COMMAND python -m cython -3 --cplus _wrapper.pyx 
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python/bolero/wrapper
)

add_custom_target(pip_install ALL
	COMMAND pip install .
	DEPENDS _ranking_svm.cpp _wrapper.cpp
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python
)

