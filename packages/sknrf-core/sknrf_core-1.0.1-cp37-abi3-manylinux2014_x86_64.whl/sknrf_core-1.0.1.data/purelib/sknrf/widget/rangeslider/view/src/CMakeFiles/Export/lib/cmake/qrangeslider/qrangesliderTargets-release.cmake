#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qrangeslider::qrangeslider" for configuration "Release"
set_property(TARGET qrangeslider::qrangeslider APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qrangeslider::qrangeslider PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libqrangeslider.so.1.0.0"
  IMPORTED_SONAME_RELEASE "libqrangeslider.so.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS qrangeslider::qrangeslider )
list(APPEND _IMPORT_CHECK_FILES_FOR_qrangeslider::qrangeslider "${_IMPORT_PREFIX}/lib/libqrangeslider.so.1.0.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
