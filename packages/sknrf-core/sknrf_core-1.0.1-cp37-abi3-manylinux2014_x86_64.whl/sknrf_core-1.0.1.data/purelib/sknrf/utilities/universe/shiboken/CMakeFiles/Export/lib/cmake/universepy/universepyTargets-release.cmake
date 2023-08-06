#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "universepy::universepy" for configuration "Release"
set_property(TARGET universepy::universepy APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(universepy::universepy PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELEASE ""
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/universe.so"
  IMPORTED_NO_SONAME_RELEASE "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS universepy::universepy )
list(APPEND _IMPORT_CHECK_FILES_FOR_universepy::universepy "${_IMPORT_PREFIX}/lib/universe.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
