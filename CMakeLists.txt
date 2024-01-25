cmake_minimum_required(VERSION 3.16)
project(BOLERO 
	VERSION 1.0.0
	DESCRIPTION "Behavior Learning and Optimization for Robots")

enable_testing()

find_package(PkgConfig REQUIRED)
pkg_check_modules(lib_manager REQUIRED IMPORTED_TARGET lib_manager)

add_subdirectory(src)

