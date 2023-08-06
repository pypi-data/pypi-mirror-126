cmake_minimum_required(VERSION 3.12.0)
project(qrangeslider)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Widgets REQUIRED)

# Build
add_library(qrangeslider SHARED
    qrangeslider.cpp)
set(headers
    qrangeslider.h)
set_target_properties(qrangeslider PROPERTIES VERSION ${SKNRF_VERSION} SOVERSION ${SKNRF_VERSION_MAJOR})
set_target_properties(qrangeslider PROPERTIES PUBLIC_HEADER "${headers}")
target_compile_definitions(qrangeslider PRIVATE QRANGESLIDER_COMPILE_LIBRARY) # export WIN32 symbols in .lib file

# Linking Flags
target_link_libraries(qrangeslider Qt5::Widgets)

# Install
install(TARGETS qrangeslider EXPORT qrangesliderTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    PUBLIC_HEADER DESTINATION include)
export_package(qrangeslider ${SKNRF_VERSION})
