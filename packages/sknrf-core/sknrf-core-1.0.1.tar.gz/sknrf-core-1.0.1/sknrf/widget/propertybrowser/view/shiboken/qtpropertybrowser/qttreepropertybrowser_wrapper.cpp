
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
#include "qttreepropertybrowser_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <qbytearray.h>
#include <qcolor.h>
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

void QtTreePropertyBrowserWrapper::pysideInitQtMetaTypes()
{
    qRegisterMetaType< ::QtTreePropertyBrowser::ResizeMode >("QtTreePropertyBrowser::ResizeMode");
}

QtTreePropertyBrowserWrapper::QtTreePropertyBrowserWrapper(QWidget * parent) : QtTreePropertyBrowser(parent)
{
    // ... middle
}

void QtTreePropertyBrowserWrapper::actionEvent(QActionEvent * event)
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

void QtTreePropertyBrowserWrapper::changeEvent(QEvent * event)
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

void QtTreePropertyBrowserWrapper::childEvent(QChildEvent * event)
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

void QtTreePropertyBrowserWrapper::closeEvent(QCloseEvent * event)
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

void QtTreePropertyBrowserWrapper::connectNotify(const QMetaMethod & signal)
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

void QtTreePropertyBrowserWrapper::contextMenuEvent(QContextMenuEvent * event)
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

QWidget * QtTreePropertyBrowserWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtTreePropertyBrowserWrapper::createEditor(QtProperty * property, QWidget * parent)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::customEvent(QEvent * event)
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

int QtTreePropertyBrowserWrapper::devType() const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::disconnectNotify(const QMetaMethod & signal)
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

void QtTreePropertyBrowserWrapper::dragEnterEvent(QDragEnterEvent * event)
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

void QtTreePropertyBrowserWrapper::dragLeaveEvent(QDragLeaveEvent * event)
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

void QtTreePropertyBrowserWrapper::dragMoveEvent(QDragMoveEvent * event)
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

void QtTreePropertyBrowserWrapper::dropEvent(QDropEvent * event)
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

void QtTreePropertyBrowserWrapper::enterEvent(QEvent * event)
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

bool QtTreePropertyBrowserWrapper::event(QEvent * event)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    return cppResult;
}

bool QtTreePropertyBrowserWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    return cppResult;
}

void QtTreePropertyBrowserWrapper::focusInEvent(QFocusEvent * event)
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

bool QtTreePropertyBrowserWrapper::focusNextPrevChild(bool next)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::focusOutEvent(QFocusEvent * event)
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

bool QtTreePropertyBrowserWrapper::hasHeightForWidth() const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtTreePropertyBrowserWrapper::heightForWidth(int arg__1) const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::hideEvent(QHideEvent * event)
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

void QtTreePropertyBrowserWrapper::initPainter(QPainter * painter) const
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

void QtTreePropertyBrowserWrapper::inputMethodEvent(QInputMethodEvent * event)
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

QVariant QtTreePropertyBrowserWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::itemChanged(QtBrowserItem * item)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemChanged"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtTreePropertyBrowser::itemChanged(item);
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

void QtTreePropertyBrowserWrapper::itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemInserted"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtTreePropertyBrowser::itemInserted(item, afterItem);
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

void QtTreePropertyBrowserWrapper::itemRemoved(QtBrowserItem * item)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemRemoved"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtTreePropertyBrowser::itemRemoved(item);
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

void QtTreePropertyBrowserWrapper::keyPressEvent(QKeyEvent * event)
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

void QtTreePropertyBrowserWrapper::keyReleaseEvent(QKeyEvent * event)
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

void QtTreePropertyBrowserWrapper::leaveEvent(QEvent * event)
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

int QtTreePropertyBrowserWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QtTreePropertyBrowserWrapper::minimumSizeHint() const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::mouseDoubleClickEvent(QMouseEvent * event)
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

void QtTreePropertyBrowserWrapper::mouseMoveEvent(QMouseEvent * event)
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

void QtTreePropertyBrowserWrapper::mousePressEvent(QMouseEvent * event)
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

void QtTreePropertyBrowserWrapper::mouseReleaseEvent(QMouseEvent * event)
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

void QtTreePropertyBrowserWrapper::moveEvent(QMoveEvent * event)
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

bool QtTreePropertyBrowserWrapper::nativeEvent(const QByteArray & eventType, void * message, long * result)
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

QPaintEngine * QtTreePropertyBrowserWrapper::paintEngine() const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::paintEvent(QPaintEvent * event)
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

QPaintDevice * QtTreePropertyBrowserWrapper::redirected(QPoint * offset) const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::resizeEvent(QResizeEvent * event)
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

void QtTreePropertyBrowserWrapper::setVisible(bool visible)
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

QPainter * QtTreePropertyBrowserWrapper::sharedPainter() const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::showEvent(QShowEvent * event)
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

QSize QtTreePropertyBrowserWrapper::sizeHint() const
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtTreePropertyBrowser.sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtTreePropertyBrowserWrapper::tabletEvent(QTabletEvent * event)
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

void QtTreePropertyBrowserWrapper::timerEvent(QTimerEvent * event)
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

void QtTreePropertyBrowserWrapper::wheelEvent(QWheelEvent * event)
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

const QMetaObject *QtTreePropertyBrowserWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtTreePropertyBrowser::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtTreePropertyBrowserWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtTreePropertyBrowser::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtTreePropertyBrowserWrapper::qt_metacast(const char *_clname)
{
        if (!_clname) return {};
        SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
        if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
                return static_cast<void *>(const_cast< QtTreePropertyBrowserWrapper *>(this));
        return QtTreePropertyBrowser::qt_metacast(_clname);
}

QtTreePropertyBrowserWrapper::~QtTreePropertyBrowserWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtTreePropertyBrowser_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    const char *argNames[] = {"parent"};
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtTreePropertyBrowser >()))
        return -1;

    ::QtTreePropertyBrowserWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_ParseTuple(args, "|O:QtTreePropertyBrowser", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::QtTreePropertyBrowser(QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QtTreePropertyBrowser(QWidget*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtTreePropertyBrowser(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowser_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtTreePropertyBrowser(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[0]))))
                    goto Sbk_QtTreePropertyBrowser_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QWidget *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtTreePropertyBrowser(QWidget*)
            void *addr = PySide::nextQObjectMemoryAddr();
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            if (addr) {
                cptr = new (addr) ::QtTreePropertyBrowserWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(0);
            } else {
                cptr = new ::QtTreePropertyBrowserWrapper(cppArg0);
            }

            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtTreePropertyBrowser >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtTreePropertyBrowser_Init_TypeError;

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

    Sbk_QtTreePropertyBrowser_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtTreePropertyBrowser");
        return -1;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_alternatingRowColors(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // alternatingRowColors()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->alternatingRowColors();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_attribute1(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attribute1()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->attribute1());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_attribute2(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attribute2()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->attribute2());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_attribute3(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attribute3()const
            BrowserCol cppResult = BrowserCol(const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->attribute3());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_attributes(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // attributes()const
            QList<BrowserCol > cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->attributes();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_backgroundColor(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::backgroundColor(QtBrowserItem*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // backgroundColor(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_backgroundColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // backgroundColor(QtBrowserItem*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QColor cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->backgroundColor(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCOLOR_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_backgroundColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.backgroundColor");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::calculatedBackgroundColor(QtBrowserItem*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // calculatedBackgroundColor(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // calculatedBackgroundColor(QtBrowserItem*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QColor cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->calculatedBackgroundColor(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCOLOR_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.calculatedBackgroundColor");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_editItem(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::editItem(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // editItem(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_editItem_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // editItem(QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->editItem(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_editItem_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.editItem");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_indentation(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // indentation()const
            int cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->indentation();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_isExpanded(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::isExpanded(QtBrowserItem*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // isExpanded(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_isExpanded_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isExpanded(QtBrowserItem*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->isExpanded(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_isExpanded_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.isExpanded");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_isHeaderVisible(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isHeaderVisible()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->isHeaderVisible();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_isItemVisible(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::isItemVisible(QtBrowserItem*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // isItemVisible(QtBrowserItem*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_isItemVisible_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // isItemVisible(QtBrowserItem*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->isItemVisible(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_isItemVisible_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.isItemVisible");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_itemChanged(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemChanged(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // itemChanged(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_itemChanged_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemChanged(QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtTreePropertyBrowserWrapper *>(cppSelf)->QtTreePropertyBrowserWrapper::itemChanged_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_itemChanged_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.itemChanged");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_itemInserted(PyObject *self, PyObject *args)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
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
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_itemInserted_TypeError;

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
            static_cast<::QtTreePropertyBrowserWrapper *>(cppSelf)->QtTreePropertyBrowserWrapper::itemInserted_protected(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_itemInserted_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtTreePropertyBrowser.itemInserted");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_itemRemoved(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemRemoved(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // itemRemoved(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_itemRemoved_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemRemoved(QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtTreePropertyBrowserWrapper *>(cppSelf)->QtTreePropertyBrowserWrapper::itemRemoved_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_itemRemoved_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.itemRemoved");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_propertiesWithoutValueMarked(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertiesWithoutValueMarked()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->propertiesWithoutValueMarked();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_resizeMode(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // resizeMode()const
            QtTreePropertyBrowser::ResizeMode cppResult = QtTreePropertyBrowser::ResizeMode(const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->resizeMode());
            pyResult = Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX])->converter, &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_resizeSection(PyObject *self, PyObject *args)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "resizeSection", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::resizeSection(int,int)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[1])))) {
        overloadId = 0; // resizeSection(int,int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_resizeSection_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        int cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // resizeSection(int,int)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->resizeSection(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_resizeSection_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtTreePropertyBrowser.resizeSection");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_rootIsDecorated(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // rootIsDecorated()const
            bool cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->rootIsDecorated();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_sectionSize(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::sectionSize(int)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // sectionSize(int)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_sectionSize_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // sectionSize(int)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            int cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->sectionSize(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtTreePropertyBrowserFunc_sectionSize_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.sectionSize");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAlternatingRowColors(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setAlternatingRowColors(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setAlternatingRowColors(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setAlternatingRowColors(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setAlternatingRowColors");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAttribute1(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAttribute1(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setAttribute1(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAttribute1_TypeError;

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

    Sbk_QtTreePropertyBrowserFunc_setAttribute1_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setAttribute1");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAttribute2(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAttribute2(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setAttribute2(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAttribute2_TypeError;

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

    Sbk_QtTreePropertyBrowserFunc_setAttribute2_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setAttribute2");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAttribute3(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAttribute3(BrowserCol)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setAttribute3(BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAttribute3_TypeError;

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

    Sbk_QtTreePropertyBrowserFunc_setAttribute3_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setAttribute3");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setAttributes(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setAttributes(QList<BrowserCol>)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX], (pyArg)))) {
        overloadId = 0; // setAttributes(QList<BrowserCol>)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setAttributes_TypeError;

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

    Sbk_QtTreePropertyBrowserFunc_setAttributes_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setAttributes");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setBackgroundColor(PyObject *self, PyObject *args)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setBackgroundColor", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setBackgroundColor(QtBrowserItem*,QColor)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppReferenceConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCOLOR_IDX]), (pyArgs[1])))) {
        overloadId = 0; // setBackgroundColor(QtBrowserItem*,QColor)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setBackgroundColor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QColor cppArg1_local;
        ::QColor *cppArg1 = &cppArg1_local;
        if (Shiboken::Conversions::isImplicitConversion(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCOLOR_IDX]), pythonToCpp[1]))
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setBackgroundColor(QtBrowserItem*,QColor)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setBackgroundColor(cppArg0, *cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setBackgroundColor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtTreePropertyBrowser.setBackgroundColor");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setExpanded(PyObject *self, PyObject *args)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
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
    // 0: QtTreePropertyBrowser::setExpanded(QtBrowserItem*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setExpanded(QtBrowserItem*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setExpanded_TypeError;

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

    Sbk_QtTreePropertyBrowserFunc_setExpanded_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtTreePropertyBrowser.setExpanded");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setHeaderLabels(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setHeaderLabels(QStringList&)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRINGLIST_IDX], (pyArg)))) {
        overloadId = 0; // setHeaderLabels(QStringList&)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setHeaderLabels_TypeError;

    // Call function/method
    {
        ::QStringList cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setHeaderLabels(QStringList&)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setHeaderLabels(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setHeaderLabels_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setHeaderLabels");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setHeaderVisible(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setHeaderVisible(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setHeaderVisible(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setHeaderVisible_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setHeaderVisible(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setHeaderVisible(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setHeaderVisible_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setHeaderVisible");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setIndentation(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setIndentation(int)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setIndentation(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setIndentation_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setIndentation(int)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setIndentation(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setIndentation_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setIndentation");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setItemVisible(PyObject *self, PyObject *args)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setItemVisible", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setItemVisible(QtBrowserItem*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setItemVisible(QtBrowserItem*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setItemVisible_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setItemVisible(QtBrowserItem*,bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setItemVisible(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setItemVisible_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtTreePropertyBrowser.setItemVisible");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setPropertiesWithoutValueMarked(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setPropertiesWithoutValueMarked(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setPropertiesWithoutValueMarked(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setPropertiesWithoutValueMarked(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setPropertiesWithoutValueMarked");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setResizeMode(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setResizeMode(QtTreePropertyBrowser::ResizeMode)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX])->converter, (pyArg)))) {
        overloadId = 0; // setResizeMode(QtTreePropertyBrowser::ResizeMode)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setResizeMode_TypeError;

    // Call function/method
    {
        ::QtTreePropertyBrowser::ResizeMode cppArg0{QtTreePropertyBrowser::Interactive};
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setResizeMode(QtTreePropertyBrowser::ResizeMode)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setResizeMode(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setResizeMode_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setResizeMode");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setRootIsDecorated(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setRootIsDecorated(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setRootIsDecorated(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setRootIsDecorated(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setRootIsDecorated");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_setSplitterPosition(PyObject *self, PyObject *pyArg)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtTreePropertyBrowser::setSplitterPosition(int)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArg)))) {
        overloadId = 0; // setSplitterPosition(int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtTreePropertyBrowserFunc_setSplitterPosition_TypeError;

    // Call function/method
    {
        int cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setSplitterPosition(int)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setSplitterPosition(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtTreePropertyBrowserFunc_setSplitterPosition_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtTreePropertyBrowser.setSplitterPosition");
        return {};
}

static PyObject *Sbk_QtTreePropertyBrowserFunc_splitterPosition(PyObject *self)
{
    QtTreePropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtTreePropertyBrowserWrapper *>(reinterpret_cast< ::QtTreePropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // splitterPosition()const
            int cppResult = const_cast<const ::QtTreePropertyBrowserWrapper *>(cppSelf)->splitterPosition();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyMethodDef Sbk_QtTreePropertyBrowser_methods[] = {
    {"alternatingRowColors", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_alternatingRowColors), METH_NOARGS},
    {"attribute1", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_attribute1), METH_NOARGS},
    {"attribute2", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_attribute2), METH_NOARGS},
    {"attribute3", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_attribute3), METH_NOARGS},
    {"attributes", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_attributes), METH_NOARGS},
    {"backgroundColor", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_backgroundColor), METH_O},
    {"calculatedBackgroundColor", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_calculatedBackgroundColor), METH_O},
    {"editItem", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_editItem), METH_O},
    {"indentation", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_indentation), METH_NOARGS},
    {"isExpanded", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_isExpanded), METH_O},
    {"isHeaderVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_isHeaderVisible), METH_NOARGS},
    {"isItemVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_isItemVisible), METH_O},
    {"itemChanged", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_itemChanged), METH_O},
    {"itemInserted", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_itemInserted), METH_VARARGS},
    {"itemRemoved", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_itemRemoved), METH_O},
    {"propertiesWithoutValueMarked", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_propertiesWithoutValueMarked), METH_NOARGS},
    {"resizeMode", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_resizeMode), METH_NOARGS},
    {"resizeSection", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_resizeSection), METH_VARARGS},
    {"rootIsDecorated", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_rootIsDecorated), METH_NOARGS},
    {"sectionSize", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_sectionSize), METH_O},
    {"setAlternatingRowColors", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAlternatingRowColors), METH_O},
    {"setAttribute1", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAttribute1), METH_O},
    {"setAttribute2", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAttribute2), METH_O},
    {"setAttribute3", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAttribute3), METH_O},
    {"setAttributes", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setAttributes), METH_O},
    {"setBackgroundColor", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setBackgroundColor), METH_VARARGS},
    {"setExpanded", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setExpanded), METH_VARARGS},
    {"setHeaderLabels", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setHeaderLabels), METH_O},
    {"setHeaderVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setHeaderVisible), METH_O},
    {"setIndentation", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setIndentation), METH_O},
    {"setItemVisible", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setItemVisible), METH_VARARGS},
    {"setPropertiesWithoutValueMarked", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setPropertiesWithoutValueMarked), METH_O},
    {"setResizeMode", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setResizeMode), METH_O},
    {"setRootIsDecorated", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setRootIsDecorated), METH_O},
    {"setSplitterPosition", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_setSplitterPosition), METH_O},
    {"splitterPosition", reinterpret_cast<PyCFunction>(Sbk_QtTreePropertyBrowserFunc_splitterPosition), METH_NOARGS},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtTreePropertyBrowser_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtTreePropertyBrowser_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QtTreePropertyBrowserSpecialCastFunction(void *obj, SbkObjectType *desiredType)
{
    auto me = reinterpret_cast< ::QtTreePropertyBrowser *>(obj);
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
static SbkObjectType *_Sbk_QtTreePropertyBrowser_Type = nullptr;
static SbkObjectType *Sbk_QtTreePropertyBrowser_TypeF(void)
{
    return _Sbk_QtTreePropertyBrowser_Type;
}

static PyType_Slot Sbk_QtTreePropertyBrowser_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtTreePropertyBrowser_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtTreePropertyBrowser_spec = {
    "qtpropertybrowser.QtTreePropertyBrowser",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtTreePropertyBrowser_slots
};

} //extern "C"

static void *Sbk_QtTreePropertyBrowser_typeDiscovery(void *cptr, SbkObjectType *instanceType)
{
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QObject >()))
        return dynamic_cast< ::QtTreePropertyBrowser *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QPaintDevice >()))
        return dynamic_cast< ::QtTreePropertyBrowser *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ enum conversion.
static void QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::QtTreePropertyBrowser::ResizeMode *>(cppOut) =
        static_cast<::QtTreePropertyBrowser::ResizeMode>(Shiboken::Enum::getValue(pyIn));

}
static PythonToCppFunc is_QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX]))
        return QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode;
    return {};
}
static PyObject *QtTreePropertyBrowser_ResizeMode_CppToPython_QtTreePropertyBrowser_ResizeMode(const void *cppIn) {
    const int castCppIn = int(*reinterpret_cast<const ::QtTreePropertyBrowser::ResizeMode *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX], castCppIn);

}

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtTreePropertyBrowser_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtTreePropertyBrowser_TypeF())))
        return QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtTreePropertyBrowser_PTR_CppToPython_QtTreePropertyBrowser(const void *cppIn) {
    return PySide::getWrapperForQObject(reinterpret_cast<::QtTreePropertyBrowser *>(const_cast<void *>(cppIn)), Sbk_QtTreePropertyBrowser_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtTreePropertyBrowser_SignatureStrings[] = {
    "qtpropertybrowser.QtTreePropertyBrowser(parent:PySide2.QtWidgets.QWidget=nullptr)",
    "qtpropertybrowser.QtTreePropertyBrowser.alternatingRowColors()->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.attribute1()->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtTreePropertyBrowser.attribute2()->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtTreePropertyBrowser.attribute3()->qtpropertybrowser.BrowserCol",
    "qtpropertybrowser.QtTreePropertyBrowser.attributes()->QList[qtpropertybrowser.BrowserCol]",
    "qtpropertybrowser.QtTreePropertyBrowser.backgroundColor(item:qtpropertybrowser.QtBrowserItem)->PySide2.QtGui.QColor",
    "qtpropertybrowser.QtTreePropertyBrowser.calculatedBackgroundColor(item:qtpropertybrowser.QtBrowserItem)->PySide2.QtGui.QColor",
    "qtpropertybrowser.QtTreePropertyBrowser.editItem(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.indentation()->int",
    "qtpropertybrowser.QtTreePropertyBrowser.isExpanded(item:qtpropertybrowser.QtBrowserItem)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.isHeaderVisible()->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.isItemVisible(item:qtpropertybrowser.QtBrowserItem)->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.itemChanged(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.itemInserted(item:qtpropertybrowser.QtBrowserItem,afterItem:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.itemRemoved(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtTreePropertyBrowser.propertiesWithoutValueMarked()->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.resizeMode()->qtpropertybrowser.QtTreePropertyBrowser.ResizeMode",
    "qtpropertybrowser.QtTreePropertyBrowser.resizeSection(logicalIndex:int,size:int)",
    "qtpropertybrowser.QtTreePropertyBrowser.rootIsDecorated()->bool",
    "qtpropertybrowser.QtTreePropertyBrowser.sectionSize(logicalIndex:int)->int",
    "qtpropertybrowser.QtTreePropertyBrowser.setAlternatingRowColors(enable:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setAttribute1(attribute:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtTreePropertyBrowser.setAttribute2(attribute:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtTreePropertyBrowser.setAttribute3(attribute:qtpropertybrowser.BrowserCol)",
    "qtpropertybrowser.QtTreePropertyBrowser.setAttributes(attributeList:QList[qtpropertybrowser.BrowserCol])",
    "qtpropertybrowser.QtTreePropertyBrowser.setBackgroundColor(item:qtpropertybrowser.QtBrowserItem,color:PySide2.QtGui.QColor)",
    "qtpropertybrowser.QtTreePropertyBrowser.setExpanded(item:qtpropertybrowser.QtBrowserItem,expanded:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setHeaderLabels(labels:PySide2.QtCore.QStringList)",
    "qtpropertybrowser.QtTreePropertyBrowser.setHeaderVisible(visible:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setIndentation(i:int)",
    "qtpropertybrowser.QtTreePropertyBrowser.setItemVisible(item:qtpropertybrowser.QtBrowserItem,visible:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setPropertiesWithoutValueMarked(mark:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setResizeMode(mode:qtpropertybrowser.QtTreePropertyBrowser.ResizeMode)",
    "qtpropertybrowser.QtTreePropertyBrowser.setRootIsDecorated(show:bool)",
    "qtpropertybrowser.QtTreePropertyBrowser.setSplitterPosition(position:int)",
    "qtpropertybrowser.QtTreePropertyBrowser.splitterPosition()->int",
    nullptr}; // Sentinel

void init_QtTreePropertyBrowser(PyObject *module)
{
    _Sbk_QtTreePropertyBrowser_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtTreePropertyBrowser",
        "QtTreePropertyBrowser*",
        &Sbk_QtTreePropertyBrowser_spec,
        QtTreePropertyBrowser_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtTreePropertyBrowser >,
        reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX]),
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread    );
    
    SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtTreePropertyBrowser_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtTreePropertyBrowser_TypeF(),
        QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR,
        is_QtTreePropertyBrowser_PythonToCpp_QtTreePropertyBrowser_PTR_Convertible,
        QtTreePropertyBrowser_PTR_CppToPython_QtTreePropertyBrowser);

    Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser");
    Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser*");
    Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtTreePropertyBrowser).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtTreePropertyBrowserWrapper).name());


    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]));
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QtTreePropertyBrowser_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QtTreePropertyBrowser_TypeF(), &Sbk_QtTreePropertyBrowserSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtTreePropertyBrowser_TypeF(), &Sbk_QtTreePropertyBrowser_typeDiscovery);

    // Initialization of enums.

    // Initialization of enum 'ResizeMode'.
    SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX] = Shiboken::Enum::createScopedEnum(Sbk_QtTreePropertyBrowser_TypeF(),
        "ResizeMode",
        "qtpropertybrowser.QtTreePropertyBrowser.ResizeMode",
        "QtTreePropertyBrowser::ResizeMode");
    if (!SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX])
        return;

    if (!Shiboken::Enum::createScopedEnumItem(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX],
        Sbk_QtTreePropertyBrowser_TypeF(), "Interactive", (long) QtTreePropertyBrowser::ResizeMode::Interactive))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX],
        Sbk_QtTreePropertyBrowser_TypeF(), "Stretch", (long) QtTreePropertyBrowser::ResizeMode::Stretch))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX],
        Sbk_QtTreePropertyBrowser_TypeF(), "Fixed", (long) QtTreePropertyBrowser::ResizeMode::Fixed))
        return;
    if (!Shiboken::Enum::createScopedEnumItem(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX],
        Sbk_QtTreePropertyBrowser_TypeF(), "ResizeToContents", (long) QtTreePropertyBrowser::ResizeMode::ResizeToContents))
        return;
    // Register converter for enum 'QtTreePropertyBrowser::ResizeMode'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX],
            QtTreePropertyBrowser_ResizeMode_CppToPython_QtTreePropertyBrowser_ResizeMode);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode,
            is_QtTreePropertyBrowser_ResizeMode_PythonToCpp_QtTreePropertyBrowser_ResizeMode_Convertible);
        Shiboken::Enum::setTypeConverter(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX], converter);
        Shiboken::Conversions::registerConverterName(converter, "QtTreePropertyBrowser::ResizeMode");
        Shiboken::Conversions::registerConverterName(converter, "ResizeMode");
    }
    // End of 'ResizeMode' enum.

    PySide::Signal::registerSignals(Sbk_QtTreePropertyBrowser_TypeF(), &::QtTreePropertyBrowser::staticMetaObject);

    QtTreePropertyBrowserWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(Sbk_QtTreePropertyBrowser_TypeF(), &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(Sbk_QtTreePropertyBrowser_TypeF(), &::QtTreePropertyBrowser::staticMetaObject, sizeof(::QtTreePropertyBrowser));
}
