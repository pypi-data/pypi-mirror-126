#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "qtpropertybrowser::qtpropertybrowser" for configuration "Release"
set_property(TARGET qtpropertybrowser::qtpropertybrowser APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(qtpropertybrowser::qtpropertybrowser PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libqtpropertybrowser.so.1.0.0"
  IMPORTED_SONAME_RELEASE "libqtpropertybrowser.so.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS qtpropertybrowser::qtpropertybrowser )
list(APPEND _IMPORT_CHECK_FILES_FOR_qtpropertybrowser::qtpropertybrowser "${_IMPORT_PREFIX}/lib/libqtpropertybrowser.so.1.0.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
