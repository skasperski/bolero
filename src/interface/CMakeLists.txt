set(INCLUDE_DESTINATION include/bolero/interface)

add_library(interface INTERFACE)

target_include_directories(interface
	INTERFACE
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<INSTALL_INTERFACE:${INCLUDE_DESTINATION}>
)

target_link_libraries(interface
	INTERFACE
		PkgConfig::lib_manager
)

# Install header files
install(DIRECTORY ./
	DESTINATION ${INCLUDE_DESTINATION}
	FILES_MATCHING PATTERN "*.h"
)

# Prepare and install pkg-config file
configure_file(bolero.pc.in ${CMAKE_BINARY_DIR}/bolero.pc @ONLY)
install(FILES ${CMAKE_BINARY_DIR}/bolero.pc DESTINATION lib/pkgconfig)

