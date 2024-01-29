add_executable(bolero_controller 
	Controller.cpp
	main.cpp
)

target_link_libraries(bolero_controller
	PRIVATE
		bl_loader
		PkgConfig::configmaps
)

install(TARGETS bolero_controller)

