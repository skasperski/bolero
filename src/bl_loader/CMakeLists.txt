set(TARGET_NAME bl_loader)
set(INCLUDE_DESTINATION include/bolero/bl_loader)

add_library(${TARGET_NAME} SHARED
	BLLoader.cpp
)

target_include_directories(${TARGET_NAME}
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
		$<INSTALL_INTERFACE:${INCLUDE_DESTINATION}>
)

target_link_libraries(${TARGET_NAME}
	PUBLIC
		interface
)

install(TARGETS ${TARGET_NAME} EXPORT bolero-targets)

install(
	FILES BLLoader.h
	DESTINATION ${INCLUDE_DESTINATION}
)

configure_file(bl_loader.pc.in bl_loader.pc @ONLY)
install(
	FILES ${PROJECT_BINARY_DIR}/src/bl_loader/bl_loader.pc
	DESTINATION lib/pkgconfig
)

