set(TARGET_NAME mars_environment)
set(INCLUDE_DESTINATION include/bolero/mars_environment)

pkg_check_modules(Mars IMPORTED_TARGET mars_app)

# This is somehow needed for QT stuff
find_package(lib_manager REQUIRED)
lib_defaults()
define_module_info()
setup_qt()

set(SOURCES
	MARSEnvironment.cpp
	MARSEnvironmentHelper.cpp
	MARSEnvPlugin.cpp
	MARSThread.cpp
	MARSReceiver.cpp
)

set(HEADERS
	MARSEnvironment.h
	MARSEnvironmentHelper.h
	MARSEnvPlugin.h
	MARSReceiver.h
)

add_library(${TARGET_NAME} SHARED ${SOURCES})

target_link_libraries(${TARGET_NAME}
	PUBLIC
		interface
		PkgConfig::Mars
)

# Install the library into the lib folder
install(TARGETS ${TARGET_NAME} EXPORT bolero-targets)

# Install headers into mars include directory
install(FILES ${HEADERS} DESTINATION ${INCLUDE_DESTINATION})

# Prepare and install necessary files to support finding of the library 
# using pkg-config
configure_file(mars_environment.pc.in ${CMAKE_BINARY_DIR}/mars_environment.pc @ONLY)
install(FILES ${CMAKE_BINARY_DIR}/mars_environment.pc DESTINATION lib/pkgconfig)
#install(DIRECTORY input_data DESTINATION configuration/learning_controller_default)
