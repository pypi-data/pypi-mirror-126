#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qrangesliderpy::qrangesliderpy" for configuration "Release"
set_property(TARGET qrangesliderpy::qrangesliderpy APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qrangesliderpy::qrangesliderpy PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELEASE ""
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/qrangeslider.so"
  IMPORTED_NO_SONAME_RELEASE "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS qrangesliderpy::qrangesliderpy )
list(APPEND _IMPORT_CHECK_FILES_FOR_qrangesliderpy::qrangesliderpy "${_IMPORT_PREFIX}/lib/qrangeslider.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
