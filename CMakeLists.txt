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
	COMMAND python -m cython -3 bolero/utils/_ranking_svm.pyx
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

set(SETUP_PY "${CMAKE_CURRENT_SOURCE_DIR}/setup.py")
add_custom_target(python_build ALL
	COMMAND python setup.py build_ext
	DEPENDS _ranking_svm.c
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

install(CODE "execute_process(
	COMMAND python setup.py install --prefix=${CMAKE_INSTALL_PREFIX}
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})"
)

