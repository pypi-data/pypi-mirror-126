#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "universe::universe" for configuration "Release"
set_property(TARGET universe::universe APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(universe::universe PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libuniverse.so.1.0.1"
  IMPORTED_SONAME_RELEASE "libuniverse.so.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS universe::universe )
list(APPEND _IMPORT_CHECK_FILES_FOR_universe::universe "${_IMPORT_PREFIX}/lib/libuniverse.so.1.0.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
