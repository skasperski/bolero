set(TARGET_NAME bl_loader)
set(INCLUDE_DESTINATION include/bolero/bl_loader)

find_package(Python COMPONENTS Development NumPy)
if(TARGET Python::Python AND TARGET Python::NumPy)
	set(PYTHON_SUPPORT TRUE)
endif()
find_package(yaml-cpp REQUIRED)

list(APPEND HEADERS BLLoader.h)
list(APPEND SOURCES BLLoader.cpp)

if(PYTHON_SUPPORT)

	list(APPEND HEADERS
		PyOptimizer.h
		PyEnvironment.h
		PyBehavior.h
		PyBehaviorSearch.h
		PyLoadableBehavior.h
		PyLoadable.h
		PythonInterpreter.hpp
	)
	
	list(APPEND SOURCES
		PyOptimizer.cpp
		PyEnvironment.cpp
		PyBehavior.cpp
		PyBehaviorSearch.cpp
		PyLoadableBehavior.cpp
		PythonInterpreter.cpp
	)
endif()


add_library(${TARGET_NAME} SHARED
	${SOURCES}
)

target_include_directories(${TARGET_NAME}
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<INSTALL_INTERFACE:${INCLUDE_DESTINATION}>
)

target_link_libraries(${TARGET_NAME}
	PUBLIC
		interface
		yaml-cpp
)

if(PYTHON_SUPPORT)
	target_compile_definitions(${TARGET_NAME}
		PUBLIC
			PYTHON_SUPPORT
	)

	target_link_libraries(${TARGET_NAME}
		PUBLIC
			Python::Python
			Python::NumPy
	)
endif()

install(TARGETS ${TARGET_NAME} EXPORT bolero-targets)

install(
	FILES ${HEADERS}
	DESTINATION ${INCLUDE_DESTINATION}
)

configure_file(bl_loader.pc.in bl_loader.pc @ONLY)
install(
	FILES ${PROJECT_BINARY_DIR}/src/bl_loader/bl_loader.pc
	DESTINATION lib/pkgconfig
)

