#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qprogressindicatorpy::qprogressindicatorpy" for configuration "Release"
set_property(TARGET qprogressindicatorpy::qprogressindicatorpy APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qprogressindicatorpy::qprogressindicatorpy PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELEASE ""
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/qprogressindicator.so"
  IMPORTED_NO_SONAME_RELEASE "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS qprogressindicatorpy::qprogressindicatorpy )
list(APPEND _IMPORT_CHECK_FILES_FOR_qprogressindicatorpy::qprogressindicatorpy "${_IMPORT_PREFIX}/lib/qprogressindicator.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
