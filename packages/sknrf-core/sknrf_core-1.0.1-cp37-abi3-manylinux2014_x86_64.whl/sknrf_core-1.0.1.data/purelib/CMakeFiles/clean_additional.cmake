# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Release")
  file(REMOVE_RECURSE
  "sknrf/widget/progressindicator/view/plugin/CMakeFiles/qprogressindicatorplugin_autogen.dir/AutogenUsed.txt"
  "sknrf/widget/progressindicator/view/plugin/CMakeFiles/qprogressindicatorplugin_autogen.dir/ParseCache.txt"
  "sknrf/widget/progressindicator/view/plugin/qprogressindicatorplugin_autogen"
  "sknrf/widget/progressindicator/view/src/CMakeFiles/qprogressindicator_autogen.dir/AutogenUsed.txt"
  "sknrf/widget/progressindicator/view/src/CMakeFiles/qprogressindicator_autogen.dir/ParseCache.txt"
  "sknrf/widget/progressindicator/view/src/qprogressindicator_autogen"
  "sknrf/widget/propertybrowser/view/plugin/CMakeFiles/qttreepropertybrowserplugin_autogen.dir/AutogenUsed.txt"
  "sknrf/widget/propertybrowser/view/plugin/CMakeFiles/qttreepropertybrowserplugin_autogen.dir/ParseCache.txt"
  "sknrf/widget/propertybrowser/view/plugin/qttreepropertybrowserplugin_autogen"
  "sknrf/widget/propertybrowser/view/src/CMakeFiles/qtpropertybrowser_autogen.dir/AutogenUsed.txt"
  "sknrf/widget/propertybrowser/view/src/CMakeFiles/qtpropertybrowser_autogen.dir/ParseCache.txt"
  "sknrf/widget/propertybrowser/view/src/qtpropertybrowser_autogen"
  "sknrf/widget/rangeslider/view/plugin/CMakeFiles/qrangesliderplugin_autogen.dir/AutogenUsed.txt"
  "sknrf/widget/rangeslider/view/plugin/CMakeFiles/qrangesliderplugin_autogen.dir/ParseCache.txt"
  "sknrf/widget/rangeslider/view/plugin/qrangesliderplugin_autogen"
  "sknrf/widget/rangeslider/view/src/CMakeFiles/qrangeslider_autogen.dir/AutogenUsed.txt"
  "sknrf/widget/rangeslider/view/src/CMakeFiles/qrangeslider_autogen.dir/ParseCache.txt"
  "sknrf/widget/rangeslider/view/src/qrangeslider_autogen"
  )
endif()
