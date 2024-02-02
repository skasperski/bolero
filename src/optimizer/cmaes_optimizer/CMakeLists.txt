set(TARGET_NAME cmaes_optimizer)
set(INCLUDE_DESTINATION include/bolero/cmaes_optimizer)
set(SOURCES
	CMAESOptimizer.cpp
	c_cmaes/cmaes.c
)
set(HEADERS
	CMAESOptimizer.h
	c_cmaes/cmaes_interface.h
	c_cmaes/cmaes.h
)

add_library(${TARGET_NAME} SHARED ${SOURCES})

target_include_directories(${TARGET_NAME}
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>/c_cmaes
		$<INSTALL_INTERFACE:${INCLUDE_DESTINATION}>
)

target_link_libraries(${TARGET_NAME}
	PUBLIC
		interface
		PkgConfig::configmaps
)

# Install the library into the lib folder
install(TARGETS ${TARGET_NAME})

# Install headers into mars include directory
install(FILES ${HEADERS} DESTINATION ${INCLUDE_DESTINATION})

# Prepare and install pkg-config files
configure_file(cmaes_optimizer.pc.in ${CMAKE_BINARY_DIR}/cmaes_optimizer.pc @ONLY)
install(FILES ${CMAKE_BINARY_DIR}/cmaes_optimizer.pc DESTINATION lib/pkgconfig)

