add_library(bl_loader SHARED
	BLLoader.cpp
	PyOptimizer.cpp
	PyEnvironment.cpp
	PyBehavior.cpp
	PyBehaviorSearch.cpp
	PyLoadableBehavior.cpp
	PythonInterpreter.cpp
)

target_include_directories(bl_loader
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
)

target_link_libraries(bl_loader
	PUBLIC
		interface
		Python::Python
		Python::NumPy
)

