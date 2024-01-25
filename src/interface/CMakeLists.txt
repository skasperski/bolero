add_library(interface INTERFACE)

target_include_directories(interface
	INTERFACE
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<INSTALL_INTERFACE:include>
)

target_link_libraries(interface
	INTERFACE
		PkgConfig::lib_manager
)
