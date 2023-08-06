cmake_minimum_required(VERSION 3.12.0)
project(qrangeslider_top)

# Include
include("${PROJECT_SOURCE_DIR}/cmake/root.cmake")

# Top-Level Macros
## Find package only when it is not a subproject
macro(find_package)
    if(NOT ${ARGV0} IN_LIST subprojects)
        _find_package(${ARGV})
    endif()
endmacro()

# List Subprojects
set(subprojects qrangeslider qrangesliderplugin)
add_subdirectory(view/src)
add_subdirectory(view/plugin)
add_subdirectory(view/shiboken)
