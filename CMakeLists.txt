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
	OUTPUT _ranking_svm.c
	COMMAND python -m cython -3 utils/_ranking_svm.pyx
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python
)

add_custom_target(pip_install ALL
	COMMAND pip install .
	DEPENDS _ranking_svm.c
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/python
)

