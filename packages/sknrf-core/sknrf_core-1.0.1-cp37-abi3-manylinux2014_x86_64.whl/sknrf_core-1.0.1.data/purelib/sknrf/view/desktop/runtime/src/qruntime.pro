win32: SRC_DIR= $$system(echo %SRC_DIR%)
unix: SRC_DIR= $$system(echo $SRC_DIR)
include($$SRC_DIR/sknrf/root.pri)

######## Before Script #########
win32: message($$system(before.bat))
unix: message($$system(sh before.sh))

TARGET = QDeviceMenuView
TEMPLATE = app

FORMS += \
    $$PWD/QRuntime.ui \
    $$PWD/QRuntimePortFrame.ui \
    $$PWD/QProgressFrame.ui \
    $$PWD/QBusyFrame.ui \

RESOURCES += \
    $$SRC_DIR/sknrf/icons/black_32.qrc \
    $$SRC_DIR/sknrf/icons/green_32.qrc \
    $$SRC_DIR/sknrf/icons/red_32.qrc \

######## After Script #########
target.path = $$SRC_DIR/sknrf/build
win32: target.extra = after.bat
unix: target.extra = sh after.sh
INSTALLS += target

DISTFILES += \
    RFGauge.qml

