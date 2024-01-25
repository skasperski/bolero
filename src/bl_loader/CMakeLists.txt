add_library(bl_loader SHARED 
	PyOptimizer.cpp
	PyEnvironment.cpp
	PyBehavior.cpp
	PyBehaviorSearch.cpp
	PyLoadableBehavior.cpp
	PythonInterpreter.cpp
)

target_include_directories(bl_loader
	PUBLIC
		$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<INSTALL_INTERFACE:include>
)

#target_link_libraries(${PROJECT_NAME}
#                      ${LIB_MANAGER_LIBRARIES}
#                      ${EXTRA_LIBRARIES}
#                      ${YAML_LIBRARIES})

