#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qprogressindicator::qprogressindicator" for configuration "Release"
set_property(TARGET qprogressindicator::qprogressindicator APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qprogressindicator::qprogressindicator PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libqprogressindicator.so.1.0.0"
  IMPORTED_SONAME_RELEASE "libqprogressindicator.so.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS qprogressindicator::qprogressindicator )
list(APPEND _IMPORT_CHECK_FILES_FOR_qprogressindicator::qprogressindicator "${_IMPORT_PREFIX}/lib/libqprogressindicator.so.1.0.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
