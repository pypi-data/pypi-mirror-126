win32: SRC_DIR= $$system(echo %SRC_DIR%)
unix: SRC_DIR= $$system(echo $SRC_DIR)
SRC_DIR=/Users/dylanbespalko/repos/scikit-nonlinear-core-dev
include($$SRC_DIR/sknrf/root.pri)

######## Before Script #########
win32: message($$system(before.bat))
unix: message($$system(sh before.sh))

TARGET = QEquation
TEMPLATE = app

FORMS += \
    $$PWD/QCalibration.ui

RESOURCES += \
    $$SRC_DIR/sknrf/icons/black_32.qrc

######## After Script #########
target.path = $$SRC_DIR/sknrf/build
win32: target.extra = after.bat
unix: target.extra = sh after.sh
INSTALLS += target


