# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "main_control: 0 messages, 1 services")

set(MSG_I_FLAGS "")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(main_control_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" NAME_WE)
add_custom_target(_main_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "main_control" "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(main_control
  "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/main_control
)

### Generating Module File
_generate_module_cpp(main_control
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/main_control
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(main_control_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(main_control_generate_messages main_control_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" NAME_WE)
add_dependencies(main_control_generate_messages_cpp _main_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(main_control_gencpp)
add_dependencies(main_control_gencpp main_control_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS main_control_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(main_control
  "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/main_control
)

### Generating Module File
_generate_module_eus(main_control
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/main_control
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(main_control_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(main_control_generate_messages main_control_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" NAME_WE)
add_dependencies(main_control_generate_messages_eus _main_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(main_control_geneus)
add_dependencies(main_control_geneus main_control_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS main_control_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(main_control
  "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/main_control
)

### Generating Module File
_generate_module_lisp(main_control
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/main_control
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(main_control_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(main_control_generate_messages main_control_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" NAME_WE)
add_dependencies(main_control_generate_messages_lisp _main_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(main_control_genlisp)
add_dependencies(main_control_genlisp main_control_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS main_control_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(main_control
  "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/main_control
)

### Generating Module File
_generate_module_nodejs(main_control
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/main_control
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(main_control_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(main_control_generate_messages main_control_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" NAME_WE)
add_dependencies(main_control_generate_messages_nodejs _main_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(main_control_gennodejs)
add_dependencies(main_control_gennodejs main_control_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS main_control_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(main_control
  "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/main_control
)

### Generating Module File
_generate_module_py(main_control
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/main_control
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(main_control_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(main_control_generate_messages main_control_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/littled3092/quick-food/src/main_control/srv/main2nav.srv" NAME_WE)
add_dependencies(main_control_generate_messages_py _main_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(main_control_genpy)
add_dependencies(main_control_genpy main_control_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS main_control_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/main_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/main_control
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_srvs_generate_messages_cpp)
  add_dependencies(main_control_generate_messages_cpp std_srvs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/main_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/main_control
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_srvs_generate_messages_eus)
  add_dependencies(main_control_generate_messages_eus std_srvs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/main_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/main_control
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_srvs_generate_messages_lisp)
  add_dependencies(main_control_generate_messages_lisp std_srvs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/main_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/main_control
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_srvs_generate_messages_nodejs)
  add_dependencies(main_control_generate_messages_nodejs std_srvs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/main_control)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/main_control\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/main_control
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_srvs_generate_messages_py)
  add_dependencies(main_control_generate_messages_py std_srvs_generate_messages_py)
endif()
