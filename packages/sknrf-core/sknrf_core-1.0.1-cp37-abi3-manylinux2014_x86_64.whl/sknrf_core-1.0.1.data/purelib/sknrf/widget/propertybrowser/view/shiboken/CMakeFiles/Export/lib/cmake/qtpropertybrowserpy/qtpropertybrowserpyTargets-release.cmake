#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qtpropertybrowserpy::qtpropertybrowserpy" for configuration "Release"
set_property(TARGET qtpropertybrowserpy::qtpropertybrowserpy APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qtpropertybrowserpy::qtpropertybrowserpy PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELEASE ""
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/qtpropertybrowser.so"
  IMPORTED_NO_SONAME_RELEASE "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS qtpropertybrowserpy::qtpropertybrowserpy )
list(APPEND _IMPORT_CHECK_FILES_FOR_qtpropertybrowserpy::qtpropertybrowserpy "${_IMPORT_PREFIX}/lib/qtpropertybrowser.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
