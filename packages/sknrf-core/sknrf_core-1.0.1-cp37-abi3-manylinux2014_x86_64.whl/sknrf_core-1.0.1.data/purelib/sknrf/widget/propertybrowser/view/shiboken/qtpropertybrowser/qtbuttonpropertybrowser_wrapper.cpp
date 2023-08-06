
// default includes
#include <shiboken.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QDebug>
#include <pysidesignal.h>
#include <pysideproperty.h>
#include <pyside.h>
#include <destroylistener.h>
#include <qapp_macro.h>
#include <typeinfo>
#include <signalmanager.h>
#include <pysidemetafunction.h>
#include <algorithm>
#include <set>

// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qtbuttonpropertybrowser_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <qbytearray.h>
#include <qcursor.h>
#include <qfont.h>
#include <qfontinfo.h>
#include <qfontmetrics.h>
#include <qicon.h>
#include <qkeysequence.h>
#include <qlocale.h>
#include <qmargins.h>
#include <qobject.h>
#include <qobjectdefs.h>
#include <qpaintdevice.h>
#include <qpalette.h>
#include <qpixmap.h>
#include <qpoint.h>
#include <qrect.h>
#include <qregion.h>
#include <qsize.h>
#include <qsizepolicy.h>
#include <qtpropertybrowser.h>
#include <qwidget.h>


#include <cctype>
#include <cstring>

QT_WARNING_DISABLE_DEPRECATED



template <class T>
static const char *typeNameOf(const T &t)
{
    const char *typeName =  typeid(t).name();
    auto size = std::strlen(typeName);
#if defined(Q_CC_MSVC) // MSVC: "class QPaintDevice * __ptr64"
    if (auto lastStar = strchr(typeName, '*')) {
        // MSVC: "class QPaintDevice * __ptr64"
        while (*--lastStar == ' ') {
        }
        size = lastStar - typeName + 1;
    }
#else // g++, Clang: "QPaintDevice *" -> "P12QPaintDevice"
    if (size > 2 && typeName[0] == 'P' && std::isdigit(typeName[1])) {
        ++typeName;
        --size;
    }
#endif
    char *result = new char[size + 1];
    result[size] = '\0';
    memcpy(result, typeName, size);
    return result;
}

// Native ---------------------------------------------------------

void QtButtonPropertyBrowserWrapper::pysideInitQtMetaTypes()
{
}

QtButtonPropertyBrowserWrapper::QtButtonPropertyBrowserWrapper(QWidget * parent) : QtButtonPropertyBrowser(parent)
{
    // ... middle
}

void QtButtonPropertyBrowserWrapper::actionEvent(QActionEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "actionEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::actionEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QACTIONEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::changeEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "changeEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::changeEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::childEvent(QChildEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "childEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QObject::childEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QCHILDEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::closeEvent(QCloseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "closeEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::closeEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCLOSEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::connectNotify(const QMetaMethod & signal)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "connectNotify"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QObject::connectNotify(signal);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QMETAMETHOD_IDX]), &signal)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtButtonPropertyBrowserWrapper::contextMenuEvent(QContextMenuEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "contextMenuEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::contextMenuEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCONTEXTMENUEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

QWidget * QtButtonPropertyBrowserWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createAttributeEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyBrowser::createAttributeEditor(property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property),
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), parent),
        Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &attribute)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtButtonPropertyBrowserWrapper::createEditor(QtProperty * property, QWidget * parent)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyBrowser::createEditor(property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property),
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), parent)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::customEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "customEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QObject::customEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

int QtButtonPropertyBrowserWrapper::devType() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "devType"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::devType();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return 0;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::disconnectNotify(const QMetaMethod & signal)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "disconnectNotify"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QObject::disconnectNotify(signal);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QMETAMETHOD_IDX]), &signal)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtButtonPropertyBrowserWrapper::dragEnterEvent(QDragEnterEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dragEnterEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dragEnterEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDRAGENTEREVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::dragLeaveEvent(QDragLeaveEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dragLeaveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dragLeaveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDRAGLEAVEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::dragMoveEvent(QDragMoveEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dragMoveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dragMoveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDRAGMOVEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::dropEvent(QDropEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dropEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dropEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDROPEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::enterEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "enterEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::enterEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

bool QtButtonPropertyBrowserWrapper::event(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "event"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::event(event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    return cppResult;
}

bool QtButtonPropertyBrowserWrapper::eventFilter(QObject * watched, QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "eventFilter"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QObject::eventFilter(watched, event);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), watched),
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QEVENT_IDX]), event)
    ));
    bool invalidateArg2 = PyTuple_GET_ITEM(pyArgs, 1)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::focusInEvent(QFocusEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "focusInEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::focusInEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QFOCUSEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

bool QtButtonPropertyBrowserWrapper::focusNextPrevChild(bool next)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "focusNextPrevChild"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::focusNextPrevChild(next);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &next)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::focusOutEvent(QFocusEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "focusOutEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::focusOutEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QFOCUSEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

bool QtButtonPropertyBrowserWrapper::hasHeightForWidth() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "hasHeightForWidth"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::hasHeightForWidth();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtButtonPropertyBrowserWrapper::heightForWidth(int arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "heightForWidth"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::heightForWidth(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        arg__1
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return 0;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::hideEvent(QHideEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "hideEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::hideEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QHIDEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::initPainter(QPainter * painter) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "initPainter"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::initPainter(painter);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTER_IDX]), painter)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtButtonPropertyBrowserWrapper::inputMethodEvent(QInputMethodEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "inputMethodEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::inputMethodEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QINPUTMETHODEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

QVariant QtButtonPropertyBrowserWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "inputMethodQuery"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::inputMethodQuery(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkPySide2_QtCoreTypes[SBK_QT_INPUTMETHODQUERY_IDX])->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QVariant();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::itemChanged(QtBrowserItem * item)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemChanged"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtButtonPropertyBrowser::itemChanged(item);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtButtonPropertyBrowserWrapper::itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemInserted"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtButtonPropertyBrowser::itemInserted(item, afterItem);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), item),
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), afterItem)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtButtonPropertyBrowserWrapper::itemRemoved(QtBrowserItem * item)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemRemoved"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtButtonPropertyBrowser::itemRemoved(item);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtButtonPropertyBrowserWrapper::keyPressEvent(QKeyEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "keyPressEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::keyPressEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QKEYEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::keyReleaseEvent(QKeyEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "keyReleaseEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::keyReleaseEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QKEYEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::leaveEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "leaveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::leaveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

int QtButtonPropertyBrowserWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "metric"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::metric(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkPySide2_QtGuiTypes[SBK_QPAINTDEVICE_PAINTDEVICEMETRIC_IDX])->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return 0;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QtButtonPropertyBrowserWrapper::minimumSizeHint() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "minimumSizeHint"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::minimumSizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QSIZE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::mouseDoubleClickEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mouseDoubleClickEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mouseDoubleClickEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::mouseMoveEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mouseMoveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mouseMoveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::mousePressEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mousePressEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mousePressEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::mouseReleaseEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mouseReleaseEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mouseReleaseEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::moveEvent(QMoveEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "moveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::moveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOVEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

bool QtButtonPropertyBrowserWrapper::nativeEvent(const QByteArray & eventType, void * message, long * result)
{

    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "nativeEvent"));
    if (pyOverride.isNull()) {

        gil.release();
        return this->::QWidget::nativeEvent(eventType, message, result);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QBYTEARRAY_IDX]), &eventType),
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<void *>(), message)
    ));


    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Begin code injection

    // TEMPLATE - return_native_eventfilter_conversion - START
    bool cppResult = false;
    if (PySequence_Check(pyResult) && (PySequence_Size(pyResult) == 2)) {
    Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyResult, 0));
    Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyItem, &(cppResult));
    if (result) {
        Shiboken::AutoDecRef pyResultItem(PySequence_GetItem(pyResult, 1));
        Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<long>(), pyResultItem, (result));
    }
    }
    // TEMPLATE - return_native_eventfilter_conversion - END

    // End of code injection

    return cppResult;
}

QPaintEngine * QtButtonPropertyBrowserWrapper::paintEngine() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "paintEngine"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::paintEngine();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTENGINE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::paintEvent(QPaintEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "paintEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::paintEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

QPaintDevice * QtButtonPropertyBrowserWrapper::redirected(QPoint * offset) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "redirected"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::redirected(offset);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QPOINT_IDX]), offset)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTDEVICE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::resizeEvent(QResizeEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "resizeEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::resizeEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QRESIZEEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::setVisible(bool visible)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "setVisible"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::setVisible(visible);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &visible)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QPainter * QtButtonPropertyBrowserWrapper::sharedPainter() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "sharedPainter"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::sharedPainter();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTER_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::showEvent(QShowEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "showEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::showEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QSHOWEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

QSize QtButtonPropertyBrowserWrapper::sizeHint() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "sizeHint"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::sizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QSIZE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtButtonPropertyBrowser.sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtButtonPropertyBrowserWrapper::tabletEvent(QTabletEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "tabletEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::tabletEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QTABLETEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::timerEvent(QTimerEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "timerEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QObject::timerEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QTIMEREVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

void QtButtonPropertyBrowserWrapper::wheelEvent(QWheelEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "wheelEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::wheelEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QWHEELEVENT_IDX]), event)
    ));
    bool invalidateArg1 = PyTuple_GET_ITEM(pyArgs, 0)->ob_refcnt == 1;

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
}

const QMetaObject *QtButtonPropertyBrowserWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtButtonPropertyBrowser::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtButtonPropertyBrowserWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtButtonPropertyBrowser::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtButtonPropertyBrowserWrapper::qt_metacast(const char *_clname)
{
        if (!_clname) return {};
        SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
        if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
                return static_cast<void *>(const_cast< QtButtonPropertyBrowserWrapper *>(this));
        return QtButtonPropertyBrowser::qt_metacast(_clname);
}

QtButtonPropertyBrowserWrapper::~QtButtonPropertyBrowserWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtButtonPropertyBrowser_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    const char *argNames[] = {"parent"};
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtButtonPropertyBrowser >()))
        return -1;

    ::QtButtonPropertyBrowserWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_ParseTuple(args, "|O:QtButtonPropertyBrowser", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::QtButtonPropertyBrowser(QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QtButtonPropertyBrowser(QWidget*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtButtonPropertyBrowser(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowser_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtButtonPropertyBrowser(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[0]))))
                    goto Sbk_QtButtonPropertyBrowser_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QWidget *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtButtonPropertyBrowser(QWidget*)
            void *addr = PySide::nextQObjectMemoryAddr();
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            if (addr) {
                cptr = new (addr) ::QtButtonPropertyBrowserWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(0);
            } else {
                cptr = new ::QtButtonPropertyBrowserWrapper(cppArg0);
            }

            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtButtonPropertyBrowser >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtButtonPropertyBrowser_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);

    // QObject setup
    PySide::Signal::updateSourceObject(self);
    metaObject = cptr->metaObject(); // <- init python qt properties
    if (kwds && !PySide::fillQtProperties(self, metaObject, kwds, argNames, 1))
        return -1;


    return 1;

    Sbk_QtButtonPropertyBrowser_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtButtonPropertyBrowser");
        return -1;
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_attribute1(PyObject *self)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attribute1()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtButtonPropertyBrowserWrapper *>(cppSelf)->attribute1());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_attribute2(PyObject *self)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attribute2()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtButtonPropertyBrowserWrapper *>(cppSelf)->attribute2());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_attribute3(PyObject *self)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attribute3()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtButtonPropertyBrowserWrapper *>(cppSelf)->attribute3());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_attributes(PyObject *self)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attributes()const
            QList<BrowserCol > cppResult = const_cast<const ::QtButtonPropertyBrowserWrapper *>(cppSelf)->attributes();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_isExpanded(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::isExpanded(QtBrowserItem*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // isExpanded(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_isExpanded_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isExpanded(QtBrowserItem*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            bool cppResult = const_cast<const ::QtButtonPropertyBrowserWrapper *>(cppSelf)->isExpanded(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtButtonPropertyBrowserFunc_isExpanded_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.isExpanded");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_itemChanged(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemChanged(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // itemChanged(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_itemChanged_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemChanged(QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtButtonPropertyBrowserWrapper *>(cppSelf)->QtButtonPropertyBrowserWrapper::itemChanged_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_itemChanged_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.itemChanged");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_itemInserted(PyObject *self, PyObject *args)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "itemInserted", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemInserted(QtBrowserItem*,QtBrowserItem*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[1])))) {
        overloadId = 0; // itemInserted(QtBrowserItem*,QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_itemInserted_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtBrowserItem *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // itemInserted(QtBrowserItem*,QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtButtonPropertyBrowserWrapper *>(cppSelf)->QtButtonPropertyBrowserWrapper::itemInserted_protected(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_itemInserted_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtButtonPropertyBrowser.itemInserted");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_itemRemoved(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemRemoved(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // itemRemoved(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_itemRemoved_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemRemoved(QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtButtonPropertyBrowserWrapper *>(cppSelf)->QtButtonPropertyBrowserWrapper::itemRemoved_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_itemRemoved_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.itemRemoved");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_setAttribute1(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::setAttribute1(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setAttribute1(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_setAttribute1_TypeError;

    // Call function/method
    {
        ::BrowserCol cppArg0{NONE};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAttribute1(BrowserCol)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setAttribute1(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_setAttribute1_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.setAttribute1");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_setAttribute2(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::setAttribute2(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setAttribute2(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_setAttribute2_TypeError;

    // Call function/method
    {
        ::BrowserCol cppArg0{NONE};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAttribute2(BrowserCol)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setAttribute2(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_setAttribute2_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.setAttribute2");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_setAttribute3(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::setAttribute3(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setAttribute3(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_setAttribute3_TypeError;

    // Call function/method
    {
        ::BrowserCol cppArg0{NONE};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAttribute3(BrowserCol)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setAttribute3(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_setAttribute3_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.setAttribute3");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_setAttributes(PyObject *self, PyObject *pyArg)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::setAttributes(QList<BrowserCol>)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX], (pyArg)))) {
        overloadId = 0; // setAttributes(QList<BrowserCol>)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_setAttributes_TypeError;

    // Call function/method
    {
        ::QList<BrowserCol > cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAttributes(QList<BrowserCol>)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setAttributes(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_setAttributes_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtButtonPropertyBrowser.setAttributes");
        return {};
}

static PyObject *Sbk_QtButtonPropertyBrowserFunc_setExpanded(PyObject *self, PyObject *args)
{
    QtButtonPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtButtonPropertyBrowserWrapper *>(reinterpret_cast< ::QtButtonPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setExpanded", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtButtonPropertyBrowser::setExpanded(QtBrowserItem*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setExpanded(QtBrowserItem*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtButtonPropertyBrowserFunc_setExpanded_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setExpanded(QtBrowserItem*,bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setExpanded(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtButtonPropertyBrowserFunc_setExpanded_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtButtonPropertyBrowser.setExpanded");
        return {};
}

static PyMethodDef Sbk_QtButtonPropertyBrowser_methods[] = {
    {"attribute1", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_attribute1), METH_NOARGS},
    {"attribute2", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_attribute2), METH_NOARGS},
    {"attribute3", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_attribute3), METH_NOARGS},
    {"attributes", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_attributes), METH_NOARGS},
    {"isExpanded", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_isExpanded), METH_O},
    {"itemChanged", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_itemChanged), METH_O},
    {"itemInserted", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_itemInserted), METH_VARARGS},
    {"itemRemoved", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_itemRemoved), METH_O},
    {"setAttribute1", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_setAttribute1), METH_O},
    {"setAttribute2", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_setAttribute2), METH_O},
    {"setAttribute3", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_setAttribute3), METH_O},
    {"setAttributes", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_setAttributes), METH_O},
    {"setExpanded", reinterpret_cast<PyCFunction>(Sbk_QtButtonPropertyBrowserFunc_setExpanded), METH_VARARGS},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtButtonPropertyBrowser_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtButtonPropertyBrowser_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QtButtonPropertyBrowserSpecialCastFunction(void *obj, SbkObjectType *desiredType)
{
    auto me = reinterpret_cast< ::QtButtonPropertyBrowser *>(obj);
    if (desiredType == reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX]))
        return static_cast< ::QtAbstractPropertyBrowser *>(me);
    else if (desiredType == reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]))
        return static_cast< ::QWidget *>(me);
    else if (desiredType == reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]))
        return static_cast< ::QObject *>(me);
    else if (desiredType == reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTDEVICE_IDX]))
        return static_cast< ::QPaintDevice *>(me);
    return me;
}


// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtButtonPropertyBrowser_Type = nullptr;
static SbkObjectType *Sbk_QtButtonPropertyBrowser_TypeF(void)
{
    return _Sbk_QtButtonPropertyBrowser_Type;
}

static PyType_Slot Sbk_QtButtonPropertyBrowser_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtButtonPropertyBrowser_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtButtonPropertyBrowser_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtButtonPropertyBrowser_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtButtonPropertyBrowser_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtButtonPropertyBrowser_spec = {
    "qtpropertybrowser.QtButtonPropertyBrowser",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtButtonPropertyBrowser_slots
};

} //extern "C"

static void *Sbk_QtButtonPropertyBrowser_typeDiscovery(void *cptr, SbkObjectType *instanceType)
{
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QObject >()))
        return dynamic_cast< ::QtButtonPropertyBrowser *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QPaintDevice >()))
        return dynamic_cast< ::QtButtonPropertyBrowser *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtButtonPropertyBrowser_PythonToCpp_QtButtonPropertyBrowser_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtButtonPropertyBrowser_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtButtonPropertyBrowser_PythonToCpp_QtButtonPropertyBrowser_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtButtonPropertyBrowser_TypeF())))
        return QtButtonPropertyBrowser_PythonToCpp_QtButtonPropertyBrowser_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtButtonPropertyBrowser_PTR_CppToPython_QtButtonPropertyBrowser(const void *cppIn) {
    return PySide::getWrapperForQObject(reinterpret_cast<::QtButtonPropertyBrowser *>(const_cast<void *>(cppIn)), Sbk_QtButtonPropertyBrowser_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtButtonPropertyBrowser_SignatureStrings[] = {
    "qtpropertybrowser.QtButtonPropertyBrowser(parent:PySide2.QtWidgets.QWidget=nullptr)",
    "qtpropertybrowser.QtButtonPropertyBrowser.attribute1()->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtButtonPropertyBrowser.attribute2()->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtButtonPropertyBrowser.attribute3()->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtButtonPropertyBrowser.attributes()->QList[qtpropertybrowser.BrowserCol]",
    "qtpropertybrowser.QtButtonPropertyBrowser.isExpanded(item:qtpropertybrowser.QtBrowserItem)->bool",
    "qtpropertybrowser.QtButtonPropertyBrowser.itemChanged(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtButtonPropertyBrowser.itemInserted(item:qtpropertybrowser.QtBrowserItem,afterItem:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtButtonPropertyBrowser.itemRemoved(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtButtonPropertyBrowser.setAttribute1(attribute:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtButtonPropertyBrowser.setAttribute2(attribute:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtButtonPropertyBrowser.setAttribute3(attribute:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtButtonPropertyBrowser.setAttributes(attributeList:QList[qtpropertybrowser.BrowserCol])",
    "qtpropertybrowser.QtButtonPropertyBrowser.setExpanded(item:qtpropertybrowser.QtBrowserItem,expanded:bool)",
    nullptr}; // Sentinel

void init_QtButtonPropertyBrowser(PyObject *module)
{
    _Sbk_QtButtonPropertyBrowser_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtButtonPropertyBrowser",
        "QtButtonPropertyBrowser*",
        &Sbk_QtButtonPropertyBrowser_spec,
        QtButtonPropertyBrowser_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtButtonPropertyBrowser >,
        reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX]),
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread    );
    
    SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtButtonPropertyBrowser_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtButtonPropertyBrowser_TypeF(),
        QtButtonPropertyBrowser_PythonToCpp_QtButtonPropertyBrowser_PTR,
        is_QtButtonPropertyBrowser_PythonToCpp_QtButtonPropertyBrowser_PTR_Convertible,
        QtButtonPropertyBrowser_PTR_CppToPython_QtButtonPropertyBrowser);

    Shiboken::Conversions::registerConverterName(converter, "QtButtonPropertyBrowser");
    Shiboken::Conversions::registerConverterName(converter, "QtButtonPropertyBrowser*");
    Shiboken::Conversions::registerConverterName(converter, "QtButtonPropertyBrowser&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtButtonPropertyBrowser).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtButtonPropertyBrowserWrapper).name());


    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]));
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QtButtonPropertyBrowser_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QtButtonPropertyBrowser_TypeF(), &Sbk_QtButtonPropertyBrowserSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtButtonPropertyBrowser_TypeF(), &Sbk_QtButtonPropertyBrowser_typeDiscovery);

    PySide::Signal::registerSignals(Sbk_QtButtonPropertyBrowser_TypeF(), &::QtButtonPropertyBrowser::staticMetaObject);

    QtButtonPropertyBrowserWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(Sbk_QtButtonPropertyBrowser_TypeF(), &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(Sbk_QtButtonPropertyBrowser_TypeF(), &::QtButtonPropertyBrowser::staticMetaObject, sizeof(::QtButtonPropertyBrowser));
}
