
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

// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qtrectfpropertymanager_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <QSet>
#include <qbrush.h>
#include <qbytearray.h>
#include <qicon.h>
#include <qobject.h>
#include <qobjectdefs.h>
#include <qrect.h>
#include <qtpropertybrowser.h>
#include <qtpropertymanager.h>


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

void QtRectFPropertyManagerWrapper::pysideInitQtMetaTypes()
{
}

QtRectFPropertyManagerWrapper::QtRectFPropertyManagerWrapper(QObject * parent) : QtRectFPropertyManager(parent)
{
    // ... middle
}

bool QtRectFPropertyManagerWrapper::check(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "check"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtRectFPropertyManager::check(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.check", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtRectFPropertyManagerWrapper::checkIcon(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "checkIcon"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtRectFPropertyManager::checkIcon(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.checkIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtRectFPropertyManagerWrapper::childEvent(QChildEvent * event)
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

void QtRectFPropertyManagerWrapper::connectNotify(const QMetaMethod & signal)
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

QtProperty * QtRectFPropertyManagerWrapper::createProperty()
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createProperty"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::createProperty();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.createProperty", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QtProperty >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QtProperty *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtRectFPropertyManagerWrapper::customEvent(QEvent * event)
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

void QtRectFPropertyManagerWrapper::disconnectNotify(const QMetaMethod & signal)
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

QString QtRectFPropertyManagerWrapper::displayText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "displayText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::displayText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.displayText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QLineEdit::EchoMode QtRectFPropertyManagerWrapper::echoMode(const QtProperty * arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return QLineEdit::Normal;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "echoMode"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::echoMode(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return QLineEdit::Normal;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkPySide2_QtWidgetsTypes[SBK_QLINEEDIT_ECHOMODE_IDX])->converter, pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.echoMode", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QLineEdit::EchoMode >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return QLineEdit::Normal;
    }
    ::QLineEdit::EchoMode cppResult{QLineEdit::Normal};
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtRectFPropertyManagerWrapper::event(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "event"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QObject::event(event);
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    return cppResult;
}

bool QtRectFPropertyManagerWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    return cppResult;
}

QBrush QtRectFPropertyManagerWrapper::foreground(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "foreground"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::foreground(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QBRUSH_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.foreground", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QBrush >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QBrush cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtRectFPropertyManagerWrapper::formatText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "formatText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::formatText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.formatText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

bool QtRectFPropertyManagerWrapper::hasValue(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "hasValue"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::hasValue(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.hasValue", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtRectFPropertyManagerWrapper::initializeProperty(QtProperty * property)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "initializeProperty"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtRectFPropertyManager::initializeProperty(property);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

bool QtRectFPropertyManagerWrapper::isReadOnly(const QtProperty * arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "isReadOnly"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::isReadOnly(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), arg__1)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.isReadOnly", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtRectFPropertyManagerWrapper::maximumText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "maximumText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::maximumText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.maximumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtRectFPropertyManagerWrapper::minimumText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "minimumText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::minimumText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.minimumText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtRectFPropertyManagerWrapper::pkAvgText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "pkAvgText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::pkAvgText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.pkAvgText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtRectFPropertyManagerWrapper::timerEvent(QTimerEvent * event)
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

void QtRectFPropertyManagerWrapper::uninitializeProperty(QtProperty * property)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "uninitializeProperty"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtRectFPropertyManager::uninitializeProperty(property);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QString QtRectFPropertyManagerWrapper::unitText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "unitText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::unitText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.unitText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QIcon QtRectFPropertyManagerWrapper::valueIcon(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "valueIcon"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyManager::valueIcon(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.valueIcon", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QIcon >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QIcon cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QString QtRectFPropertyManagerWrapper::valueText(const QtProperty * property) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QString();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "valueText"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtRectFPropertyManager::valueText(property);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QString();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtRectFPropertyManager.valueText", "QString", Py_TYPE(pyResult)->tp_name);
        return ::QString();
    }
    ::QString cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

const QMetaObject *QtRectFPropertyManagerWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtRectFPropertyManager::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtRectFPropertyManagerWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtRectFPropertyManager::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtRectFPropertyManagerWrapper::qt_metacast(const char *_clname)
{
        if (!_clname) return {};
        SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
        if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
                return static_cast<void *>(const_cast< QtRectFPropertyManagerWrapper *>(this));
        return QtRectFPropertyManager::qt_metacast(_clname);
}

QtRectFPropertyManagerWrapper::~QtRectFPropertyManagerWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtRectFPropertyManager_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    const char *argNames[] = {"parent"};
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtRectFPropertyManager >()))
        return -1;

    ::QtRectFPropertyManagerWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_ParseTuple(args, "|O:QtRectFPropertyManager", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtRectFPropertyManager::QtRectFPropertyManager(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtRectFPropertyManager(QObject*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtRectFPropertyManager(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManager_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtRectFPropertyManager(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0]))))
                    goto Sbk_QtRectFPropertyManager_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtRectFPropertyManager(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            if (addr) {
                cptr = new (addr) ::QtRectFPropertyManagerWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(0);
            } else {
                cptr = new ::QtRectFPropertyManagerWrapper(cppArg0);
            }

            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtRectFPropertyManager >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtRectFPropertyManager_Init_TypeError;

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

    Sbk_QtRectFPropertyManager_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtRectFPropertyManager");
        return -1;
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_check(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::check(const QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // check(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_check_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // check(const QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            bool cppResult = Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self)) ? const_cast<const ::QtRectFPropertyManagerWrapper *>(cppSelf)->::QtRectFPropertyManager::check(cppArg0) : const_cast<const ::QtRectFPropertyManagerWrapper *>(cppSelf)->check(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtRectFPropertyManagerFunc_check_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.check");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_checkIcon(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::checkIcon(const QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // checkIcon(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_checkIcon_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // checkIcon(const QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QIcon cppResult = static_cast<::QtRectFPropertyManagerWrapper *>(cppSelf)->QtRectFPropertyManagerWrapper::checkIcon_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtRectFPropertyManagerFunc_checkIcon_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.checkIcon");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_constraint(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtRectFPropertyManager::constraint(const QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // constraint(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_constraint_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // constraint(const QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QRectF cppResult = const_cast<const ::QtRectFPropertyManagerWrapper *>(cppSelf)->constraint(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QRECTF_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtRectFPropertyManagerFunc_constraint_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.constraint");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_initializeProperty(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::initializeProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // initializeProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_initializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // initializeProperty(QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtRectFPropertyManagerWrapper *>(cppSelf)->QtRectFPropertyManagerWrapper::initializeProperty_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtRectFPropertyManagerFunc_initializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.initializeProperty");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_precision(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtRectFPropertyManager::precision(const QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // precision(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_precision_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // precision(const QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            int cppResult = const_cast<const ::QtRectFPropertyManagerWrapper *>(cppSelf)->precision(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtRectFPropertyManagerFunc_precision_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.precision");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_setCheck(PyObject *self, PyObject *args)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setCheck", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtRectFPropertyManager::setCheck(QtProperty*,bool)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[1])))) {
        overloadId = 0; // setCheck(QtProperty*,bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_setCheck_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        bool cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setCheck(QtProperty*,bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setCheck(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtRectFPropertyManagerFunc_setCheck_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtRectFPropertyManager.setCheck");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_setConstraint(PyObject *self, PyObject *args)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setConstraint", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtRectFPropertyManager::setConstraint(QtProperty*,QRectF)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppReferenceConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QRECTF_IDX]), (pyArgs[1])))) {
        overloadId = 0; // setConstraint(QtProperty*,QRectF)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_setConstraint_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QRectF cppArg1_local;
        ::QRectF *cppArg1 = &cppArg1_local;
        if (Shiboken::Conversions::isImplicitConversion(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QRECTF_IDX]), pythonToCpp[1]))
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setConstraint(QtProperty*,QRectF)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setConstraint(cppArg0, *cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtRectFPropertyManagerFunc_setConstraint_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtRectFPropertyManager.setConstraint");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_setPrecision(PyObject *self, PyObject *args)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setPrecision", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtRectFPropertyManager::setPrecision(QtProperty*,int)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), (pyArgs[1])))) {
        overloadId = 0; // setPrecision(QtProperty*,int)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_setPrecision_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        int cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setPrecision(QtProperty*,int)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setPrecision(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtRectFPropertyManagerFunc_setPrecision_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtRectFPropertyManager.setPrecision");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_setValue(PyObject *self, PyObject *args)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setValue", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtRectFPropertyManager::setValue(QtProperty*,QRectF)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppReferenceConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QRECTF_IDX]), (pyArgs[1])))) {
        overloadId = 0; // setValue(QtProperty*,QRectF)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_setValue_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QRectF cppArg1_local;
        ::QRectF *cppArg1 = &cppArg1_local;
        if (Shiboken::Conversions::isImplicitConversion(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QRECTF_IDX]), pythonToCpp[1]))
            pythonToCpp[1](pyArgs[1], &cppArg1_local);
        else
            pythonToCpp[1](pyArgs[1], &cppArg1);


        if (!PyErr_Occurred()) {
            // setValue(QtProperty*,QRectF)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setValue(cppArg0, *cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtRectFPropertyManagerFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtRectFPropertyManager.setValue");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_subDoublePropertyManager(PyObject *self)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subDoublePropertyManager()const
            QtDoublePropertyManager * cppResult = const_cast<const ::QtRectFPropertyManagerWrapper *>(cppSelf)->subDoublePropertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_uninitializeProperty(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::uninitializeProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // uninitializeProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_uninitializeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // uninitializeProperty(QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtRectFPropertyManagerWrapper *>(cppSelf)->QtRectFPropertyManagerWrapper::uninitializeProperty_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtRectFPropertyManagerFunc_uninitializeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.uninitializeProperty");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_value(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtRectFPropertyManager::value(const QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // value(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_value_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // value(const QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QRectF cppResult = const_cast<const ::QtRectFPropertyManagerWrapper *>(cppSelf)->value(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QRECTF_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtRectFPropertyManagerFunc_value_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.value");
        return {};
}

static PyObject *Sbk_QtRectFPropertyManagerFunc_valueText(PyObject *self, PyObject *pyArg)
{
    QtRectFPropertyManagerWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtRectFPropertyManagerWrapper *>(reinterpret_cast< ::QtRectFPropertyManager *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyManager::valueText(const QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // valueText(const QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtRectFPropertyManagerFunc_valueText_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // valueText(const QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QString cppResult = static_cast<::QtRectFPropertyManagerWrapper *>(cppSelf)->QtRectFPropertyManagerWrapper::valueText_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtRectFPropertyManagerFunc_valueText_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtRectFPropertyManager.valueText");
        return {};
}

static PyMethodDef Sbk_QtRectFPropertyManager_methods[] = {
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_check), METH_O},
    {"checkIcon", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_checkIcon), METH_O},
    {"constraint", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_constraint), METH_O},
    {"initializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_initializeProperty), METH_O},
    {"precision", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_precision), METH_O},
    {"setCheck", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_setCheck), METH_VARARGS},
    {"setConstraint", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_setConstraint), METH_VARARGS},
    {"setPrecision", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_setPrecision), METH_VARARGS},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_setValue), METH_VARARGS},
    {"subDoublePropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_subDoublePropertyManager), METH_NOARGS},
    {"uninitializeProperty", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_uninitializeProperty), METH_O},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_value), METH_O},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtRectFPropertyManagerFunc_valueText), METH_O},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtRectFPropertyManager_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtRectFPropertyManager_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtRectFPropertyManager_Type = nullptr;
static SbkObjectType *Sbk_QtRectFPropertyManager_TypeF(void)
{
    return _Sbk_QtRectFPropertyManager_Type;
}

static PyType_Slot Sbk_QtRectFPropertyManager_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtRectFPropertyManager_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtRectFPropertyManager_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtRectFPropertyManager_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtRectFPropertyManager_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtRectFPropertyManager_spec = {
    "qtpropertybrowser.QtRectFPropertyManager",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtRectFPropertyManager_slots
};

} //extern "C"

static void *Sbk_QtRectFPropertyManager_typeDiscovery(void *cptr, SbkObjectType *instanceType)
{
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QObject >()))
        return dynamic_cast< ::QtRectFPropertyManager *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtRectFPropertyManager_PythonToCpp_QtRectFPropertyManager_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtRectFPropertyManager_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtRectFPropertyManager_PythonToCpp_QtRectFPropertyManager_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtRectFPropertyManager_TypeF())))
        return QtRectFPropertyManager_PythonToCpp_QtRectFPropertyManager_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtRectFPropertyManager_PTR_CppToPython_QtRectFPropertyManager(const void *cppIn) {
    return PySide::getWrapperForQObject(reinterpret_cast<::QtRectFPropertyManager *>(const_cast<void *>(cppIn)), Sbk_QtRectFPropertyManager_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtRectFPropertyManager_SignatureStrings[] = {
    "qtpropertybrowser.QtRectFPropertyManager(parent:PySide2.QtCore.QObject=nullptr)",
    "qtpropertybrowser.QtRectFPropertyManager.check(property:qtpropertybrowser.QtProperty)->bool",
    "qtpropertybrowser.QtRectFPropertyManager.checkIcon(property:qtpropertybrowser.QtProperty)->PySide2.QtGui.QIcon",
    "qtpropertybrowser.QtRectFPropertyManager.constraint(property:qtpropertybrowser.QtProperty)->PySide2.QtCore.QRectF",
    "qtpropertybrowser.QtRectFPropertyManager.initializeProperty(property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtRectFPropertyManager.precision(property:qtpropertybrowser.QtProperty)->int",
    "qtpropertybrowser.QtRectFPropertyManager.setCheck(property:qtpropertybrowser.QtProperty,check:bool)",
    "qtpropertybrowser.QtRectFPropertyManager.setConstraint(property:qtpropertybrowser.QtProperty,constraint:PySide2.QtCore.QRectF)",
    "qtpropertybrowser.QtRectFPropertyManager.setPrecision(property:qtpropertybrowser.QtProperty,prec:int)",
    "qtpropertybrowser.QtRectFPropertyManager.setValue(property:qtpropertybrowser.QtProperty,val:PySide2.QtCore.QRectF)",
    "qtpropertybrowser.QtRectFPropertyManager.subDoublePropertyManager()->qtpropertybrowser.QtDoublePropertyManager",
    "qtpropertybrowser.QtRectFPropertyManager.uninitializeProperty(property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtRectFPropertyManager.value(property:qtpropertybrowser.QtProperty)->PySide2.QtCore.QRectF",
    "qtpropertybrowser.QtRectFPropertyManager.valueText(property:qtpropertybrowser.QtProperty)->QString",
    nullptr}; // Sentinel

void init_QtRectFPropertyManager(PyObject *module)
{
    _Sbk_QtRectFPropertyManager_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtRectFPropertyManager",
        "QtRectFPropertyManager*",
        &Sbk_QtRectFPropertyManager_spec,
        QtRectFPropertyManager_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtRectFPropertyManager >,
        reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]),
        0,
        0    );
    
    SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtRectFPropertyManager_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtRectFPropertyManager_TypeF(),
        QtRectFPropertyManager_PythonToCpp_QtRectFPropertyManager_PTR,
        is_QtRectFPropertyManager_PythonToCpp_QtRectFPropertyManager_PTR_Convertible,
        QtRectFPropertyManager_PTR_CppToPython_QtRectFPropertyManager);

    Shiboken::Conversions::registerConverterName(converter, "QtRectFPropertyManager");
    Shiboken::Conversions::registerConverterName(converter, "QtRectFPropertyManager*");
    Shiboken::Conversions::registerConverterName(converter, "QtRectFPropertyManager&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtRectFPropertyManager).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtRectFPropertyManagerWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtRectFPropertyManager_TypeF(), &Sbk_QtRectFPropertyManager_typeDiscovery);

    PySide::Signal::registerSignals(Sbk_QtRectFPropertyManager_TypeF(), &::QtRectFPropertyManager::staticMetaObject);

    QtRectFPropertyManagerWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(Sbk_QtRectFPropertyManager_TypeF(), &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(Sbk_QtRectFPropertyManager_TypeF(), &::QtRectFPropertyManager::staticMetaObject, sizeof(::QtRectFPropertyManager));
}
