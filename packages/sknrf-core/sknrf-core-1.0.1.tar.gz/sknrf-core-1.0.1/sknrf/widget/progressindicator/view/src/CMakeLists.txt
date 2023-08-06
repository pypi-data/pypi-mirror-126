cmake_minimum_required(VERSION 3.12.0)
project(qprogressindicator)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Widgets REQUIRED)

# Build
add_library(qprogressindicator SHARED
    qprogressindicator.cpp)
set(headers
    qprogressindicator.h)
set_target_properties(qprogressindicator PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
set_target_properties(qprogressindicator PROPERTIES PUBLIC_HEADER "${headers}")
target_compile_definitions(qprogressindicator PRIVATE QPROGRESSINDICATOR_COMPILE_LIBRARY) # export WIN32 symbols in .lib file

# Linking Flags
target_link_libraries(qprogressindicator Qt5::Widgets)

# Install
install(TARGETS qprogressindicator EXPORT qprogressindicatorTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    PUBLIC_HEADER DESTINATION include)
export_package(qprogressindicator ${SKNRF_VERSION})
