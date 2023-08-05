# SPDX-FileCopyrightText: 2006-2021 Istituto Italiano di Tecnologia (IIT)
# SPDX-License-Identifier: BSD-3-Clause


# For static builds, all the dependencies used by targets in YARP_osTargets.cmake
# must be available before including the file, but due to the recursive
# dependencies in YARP_init, we are forced to use a hack


set(YARP_os_VERSION 3.5.0+316-20211103.6+git1b6fb0d6f)


####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was YARP_osConfigStatic.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

####################################################################################

function(_YARP_INCLUDE_TARGETS_FILE _component)
  set(CMAKE_FIND_PACKAGE_NAME ${_component}_static_hack)

  if(EXISTS "${YARP_CMAKECONFIG_DIR}/${_component}/${_component}Targets.cmake")
    include("${YARP_CMAKECONFIG_DIR}/${_component}/${_component}Targets.cmake")
    if(NOT "${_component}" STREQUAL "YARP_os")
      list(APPEND _yarp_included_components ${_component})
    endif()

    # Extract missing targets from the error message (WARNING, not really safe
    # towards new CMake versions).
    string(REGEX REPLACE ".+:  (.+)" "\\1" _${_component}_targets "${${_component}_static_hack_NOT_FOUND_MESSAGE}")
    string(REGEX REPLACE " " ";" _${_component}_targets "${_${_component}_targets}")
    list(APPEND _yarp_expected_targets ${_${_component}_targets})
    string(REGEX REPLACE "YARP::" "" _${_component}_targets "${_${_component}_targets}")

    foreach(_next_target ${_${_component}_targets})
      if(NOT "${_next_target}" MATCHES "YARP_")
        set(_next_component "YARP_${_next_target}")
      else()
        set(_next_component "${_next_target}")
      endif()
      if(NOT TARGET YARP::${_next_target})
        _yarp_include_targets_file(${_next_component})
      endif()
    endforeach()
  endif()

  if(NOT "${_yarp_included_components}" STREQUAL "")
    list(REMOVE_DUPLICATES _yarp_included_components)
  endif()
  set(_yarp_included_components ${_yarp_included_components} PARENT_SCOPE)

  if(NOT "${_yarp_expected_targets}" STREQUAL "")
    list(REMOVE_DUPLICATES _yarp_expected_targets)
  endif()
  set(_yarp_expected_targets ${_yarp_expected_targets} PARENT_SCOPE)
endfunction()


#### Expanded from @PACKAGE_DEPENDENCIES@ by install_basic_package_files() ####

include(CMakeFindDependencyMacro)
find_dependency(YARP_conf HINTS "${CMAKE_CURRENT_LIST_DIR}/.." NO_DEFAULT_PATH)
find_dependency(ACE)

###############################################################################




unset(_yarp_included_components)
unset(_yarp_expected_targets)

_yarp_include_targets_file(YARP_os)

# Properly find the dependencies. This will force to include all the
# dependencies also for packages in other exports
foreach(_component ${_yarp_included_components})
  find_dependency(${_component}
                  HINTS "${YARP_CMAKECONFIG_DIR}"
                  NO_DEFAULT_PATH)
endforeach()


# Finally perform the check, usually performed inside the target files
foreach(_target ${_yarp_expected_targets})
  if(NOT TARGET "${_target}" )
    message(FATAL_ERROR "set(${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets \"${${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets} ${_target}\")")
    set(${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets "${${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets} ${_target}")
  endif()
endforeach()

if(DEFINED ${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets)
  if(CMAKE_FIND_PACKAGE_NAME)
    set( ${CMAKE_FIND_PACKAGE_NAME}_FOUND FALSE)
    set( ${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE "The following imported targets are referenced, but are missing: ${${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets}")
  else()
    message(FATAL_ERROR "The following imported targets are referenced, but are missing: ${${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets}")
  endif()
endif()
unset(${CMAKE_FIND_PACKAGE_NAME}_NOT_FOUND_MESSAGE_targets)



