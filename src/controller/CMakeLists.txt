add_executable(controller 
	Controller.cpp
	main.cpp
)

target_link_libraries(controller
	PRIVATE
		bl_loader
		PkgConfig::configmaps
)

