cmake_minimum_required(VERSION 3.12.0)
project(qprogressindicatorpy)

# Include
include("${PROJECT_SOURCE_DIR}/../../cmake/root.cmake")
include("${PROJECT_SOURCE_DIR}/../../cmake/export_package.cmake")

# Variables
pyside2_config(--shiboken2-generator-path shiboken2_generator_path)
pyside2_config(--shiboken2-generator-include-path shiboken_include_dir 1)
pyside2_config(--shiboken2-module-shared-libraries-cmake shiboken_shared_libraries 0)

# Dependencies
find_package(qprogressindicator REQUIRED)
find_package(Qt5 COMPONENTS Widgets REQUIRED)

# Build
## Generate the binding cpp files.
set(generated_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/qprogressindicator/qprogressindicator_module_wrapper.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/qprogressindicator/qprogressindicator_wrapper.cpp)
set(BINDINGS_H ${CMAKE_CURRENT_SOURCE_DIR}/bindings.h)
set(BINDINGS_XML ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml)
add_custom_command(OUTPUT ${generated_sources}
                   COMMAND ${shiboken_generator}
                   "--enable-pyside-extensions"
                   ${SHIBOKEN_OPT} ${BINDINGS_H} ${BINDINGS_XML}
                   DEPENDS ${BINDINGS_H} ${BINDINGS_XML} qprogressindicator::qprogressindicator
                   IMPLICIT_DEPENDS CXX ${BINDINGS_H}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running binding generator for ${CMAKE_CURRENT_SOURCE_DIR}.")
## Build the Python binding.
add_library(qprogressindicatorpy MODULE ${generated_sources})
## Define Python module_name.so
set_target_properties(qprogressindicatorpy PROPERTIES PREFIX "")
set_target_properties(qprogressindicatorpy PROPERTIES OUTPUT_NAME "qprogressindicator")
if(WIN32)
    set_target_properties(qprogressindicatorpy PROPERTIES SUFFIX ".pyd")
    target_compile_definitions(qprogressindicatorpy PRIVATE QPROGRESSINDICATOR_USE_LIBRARY) # export WIN32 symbols in .lib file
endif()

# Include Flags
target_include_directories(qprogressindicatorpy PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../src)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/include)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/include/QtWidgets)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/include/QtGui)
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/include/QtCore)
target_include_directories(qprogressindicatorpy PRIVATE ${shiboken_include_dir})
target_include_directories(qprogressindicatorpy PRIVATE ${PYTHON_INC})
target_include_directories(qprogressindicatorpy PRIVATE ${Qt5Widgets_INCLUDE_DIRS})

# Link Flags
target_link_libraries(qprogressindicatorpy PRIVATE qprogressindicator::qprogressindicator)
if(WIN32)
    target_link_libraries(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/pyside2.cp${Python_VERSION_MAJOR}${Python_VERSION_MINOR}-win_amd64${CMAKE_STATIC_LIBRARY_SUFFIX})
    target_link_libraries(qprogressindicatorpy PRIVATE ${CONDA_PREFIX}/libs/python${PYTHONVERSION}${CMAKE_STATIC_LIBRARY_SUFFIX})
elseif(APPLE)
    target_link_libraries(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/libpyside2.cpython-${Python_VERSION_MAJOR}${Python_VERSION_MINOR}m-darwin.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR}${CMAKE_SHARED_LIBRARY_SUFFIX})
    set_target_properties(qprogressindicatorpy PROPERTIES LINK_FLAGS "-undefined dynamic_lookup")
else()
    target_link_libraries(qprogressindicatorpy PRIVATE ${PYTHON_SP_DIR}/PySide2/libpyside2.cpython-${Python_VERSION_MAJOR}${Python_VERSION_MINOR}m-x86_64-linux-gnu${CMAKE_SHARED_LIBRARY_SUFFIX}.${Qt_VERSION_MAJOR}.${Qt_VERSION_MINOR})
endif() 
target_link_libraries(qprogressindicatorpy PRIVATE ${shiboken_shared_libraries})
target_link_libraries(qprogressindicatorpy PRIVATE Qt5::Widgets)

# Install
if (WIN32)
    install (TARGETS qprogressindicatorpy EXPORT qprogressindicatorpyTargets
             DESTINATION bin)
else()
    install (TARGETS qprogressindicatorpy EXPORT qprogressindicatorpyTargets
             DESTINATION lib)
endif()
export_package(qprogressindicatorpy ${SKNRF_VERSION})
