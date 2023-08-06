
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

// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qtproperty_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <qbrush.h>
#include <qicon.h>
#include <qtpropertybrowser.h>


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

void QtPropertyWrapper::pysideInitQtMetaTypes()
{
}

QtPropertyWrapper::QtPropertyWrapper(QtAbstractPropertyManager * manager) : QtProperty(manager)
{
    // ... middle
}

QtPropertyWrapper::~QtPropertyWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtProperty_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtProperty >()))
        return -1;

    ::QtPropertyWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "QtProperty", 1, 1, &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtProperty::QtProperty(QtAbstractPropertyManager*)
    if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtProperty(QtAbstractPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtProperty_Init_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QtAbstractPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtProperty(QtAbstractPropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cptr = new ::QtPropertyWrapper(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtProperty >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtProperty_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtProperty_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtProperty");
        return -1;
}

static PyObject *Sbk_QtPropertyFunc_addSubProperty(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::addSubProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // addSubProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_addSubProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // addSubProperty(QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->addSubProperty(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_addSubProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.addSubProperty");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_check(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // check()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->check();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_checkIcon(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // checkIcon()const
            QIcon cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->checkIcon();
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_displayText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // displayText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->displayText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_foreground(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // foreground()const
            QBrush cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->foreground();
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QBRUSH_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_formatText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // formatText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->formatText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_hasValue(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // hasValue()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->hasValue();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_insertSubProperty(PyObject *self, PyObject *args)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "insertSubProperty", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtProperty::insertSubProperty(QtProperty*,QtProperty*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[1])))) {
        overloadId = 0; // insertSubProperty(QtProperty*,QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_insertSubProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // insertSubProperty(QtProperty*,QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->insertSubProperty(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_insertSubProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtProperty.insertSubProperty");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_isEnabled(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isEnabled()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->isEnabled();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_isModified(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // isModified()const
            bool cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->isModified();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_label(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // label()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->label();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_maximumText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // maximumText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->maximumText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_minimumText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // minimumText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->minimumText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_pkAvgText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // pkAvgText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->pkAvgText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_propertyChanged(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyChanged()
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtPropertyWrapper *>(cppSelf)->QtPropertyWrapper::propertyChanged_protected();
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_QtPropertyFunc_propertyManager(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyManager()const
            QtAbstractPropertyManager * cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->propertyManager();
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_propertyName(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyName()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->propertyName();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_removeSubProperty(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::removeSubProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // removeSubProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_removeSubProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // removeSubProperty(QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->removeSubProperty(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_removeSubProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.removeSubProperty");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setEnabled(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setEnabled(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setEnabled(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setEnabled_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setEnabled(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setEnabled(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setEnabled_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setEnabled");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setLabel(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setLabel(QString)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setLabel(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setLabel_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setLabel(QString)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setLabel(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setLabel_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setLabel");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setModified(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setModified(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setModified(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setModified_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setModified(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setModified(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setModified_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setModified");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setPropertyName(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setPropertyName(QString)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setPropertyName(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setPropertyName_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setPropertyName(QString)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setPropertyName(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setPropertyName_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setPropertyName");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setStatusTip(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setStatusTip(QString)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setStatusTip(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setStatusTip_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setStatusTip(QString)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setStatusTip(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setStatusTip_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setStatusTip");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setToolTip(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setToolTip(QString)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setToolTip(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setToolTip_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setToolTip(QString)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setToolTip(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setToolTip_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setToolTip");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_setWhatsThis(PyObject *self, PyObject *pyArg)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtProperty::setWhatsThis(QString)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // setWhatsThis(QString)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtPropertyFunc_setWhatsThis_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setWhatsThis(QString)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setWhatsThis(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtPropertyFunc_setWhatsThis_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtProperty.setWhatsThis");
        return {};
}

static PyObject *Sbk_QtPropertyFunc_statusTip(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // statusTip()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->statusTip();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_subProperties(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // subProperties()const
            QList<QtProperty* > cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->subProperties();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_toolTip(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // toolTip()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->toolTip();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_unitText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // unitText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->unitText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_valueIcon(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueIcon()const
            QIcon cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->valueIcon();
            pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_valueText(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueText()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->valueText();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtPropertyFunc_whatsThis(PyObject *self)
{
    QtPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtPropertyWrapper *>(reinterpret_cast< ::QtProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // whatsThis()const
            QString cppResult = const_cast<const ::QtPropertyWrapper *>(cppSelf)->whatsThis();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyMethodDef Sbk_QtProperty_methods[] = {
    {"addSubProperty", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_addSubProperty), METH_O},
    {"check", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_check), METH_NOARGS},
    {"checkIcon", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_checkIcon), METH_NOARGS},
    {"displayText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_displayText), METH_NOARGS},
    {"foreground", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_foreground), METH_NOARGS},
    {"formatText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_formatText), METH_NOARGS},
    {"hasValue", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_hasValue), METH_NOARGS},
    {"insertSubProperty", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_insertSubProperty), METH_VARARGS},
    {"isEnabled", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_isEnabled), METH_NOARGS},
    {"isModified", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_isModified), METH_NOARGS},
    {"label", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_label), METH_NOARGS},
    {"maximumText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_maximumText), METH_NOARGS},
    {"minimumText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_minimumText), METH_NOARGS},
    {"pkAvgText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_pkAvgText), METH_NOARGS},
    {"propertyChanged", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_propertyChanged), METH_NOARGS},
    {"propertyManager", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_propertyManager), METH_NOARGS},
    {"propertyName", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_propertyName), METH_NOARGS},
    {"removeSubProperty", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_removeSubProperty), METH_O},
    {"setEnabled", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setEnabled), METH_O},
    {"setLabel", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setLabel), METH_O},
    {"setModified", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setModified), METH_O},
    {"setPropertyName", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setPropertyName), METH_O},
    {"setStatusTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setStatusTip), METH_O},
    {"setToolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setToolTip), METH_O},
    {"setWhatsThis", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_setWhatsThis), METH_O},
    {"statusTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_statusTip), METH_NOARGS},
    {"subProperties", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_subProperties), METH_NOARGS},
    {"toolTip", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_toolTip), METH_NOARGS},
    {"unitText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_unitText), METH_NOARGS},
    {"valueIcon", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_valueIcon), METH_NOARGS},
    {"valueText", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_valueText), METH_NOARGS},
    {"whatsThis", reinterpret_cast<PyCFunction>(Sbk_QtPropertyFunc_whatsThis), METH_NOARGS},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtProperty_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtProperty_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtProperty_Type = nullptr;
static SbkObjectType *Sbk_QtProperty_TypeF(void)
{
    return _Sbk_QtProperty_Type;
}

static PyType_Slot Sbk_QtProperty_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtProperty_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtProperty_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtProperty_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtProperty_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtProperty_spec = {
    "qtpropertybrowser.QtProperty",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtProperty_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtProperty_PythonToCpp_QtProperty_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtProperty_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtProperty_PythonToCpp_QtProperty_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtProperty_TypeF())))
        return QtProperty_PythonToCpp_QtProperty_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtProperty_PTR_CppToPython_QtProperty(const void *cppIn) {
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtProperty *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
     }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtProperty_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtProperty_SignatureStrings[] = {
    "qtpropertybrowser.QtProperty(manager:qtpropertybrowser.QtAbstractPropertyManager)",
    "qtpropertybrowser.QtProperty.addSubProperty(property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtProperty.check()->bool",
    "qtpropertybrowser.QtProperty.checkIcon()->PySide2.QtGui.QIcon",
    "qtpropertybrowser.QtProperty.displayText()->QString",
    "qtpropertybrowser.QtProperty.foreground()->PySide2.QtGui.QBrush",
    "qtpropertybrowser.QtProperty.formatText()->QString",
    "qtpropertybrowser.QtProperty.hasValue()->bool",
    "qtpropertybrowser.QtProperty.insertSubProperty(property:qtpropertybrowser.QtProperty,afterProperty:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtProperty.isEnabled()->bool",
    "qtpropertybrowser.QtProperty.isModified()->bool",
    "qtpropertybrowser.QtProperty.label()->QString",
    "qtpropertybrowser.QtProperty.maximumText()->QString",
    "qtpropertybrowser.QtProperty.minimumText()->QString",
    "qtpropertybrowser.QtProperty.pkAvgText()->QString",
    "qtpropertybrowser.QtProperty.propertyChanged()",
    "qtpropertybrowser.QtProperty.propertyManager()->qtpropertybrowser.QtAbstractPropertyManager",
    "qtpropertybrowser.QtProperty.propertyName()->QString",
    "qtpropertybrowser.QtProperty.removeSubProperty(property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtProperty.setEnabled(enable:bool)",
    "qtpropertybrowser.QtProperty.setLabel(text:QString)",
    "qtpropertybrowser.QtProperty.setModified(modified:bool)",
    "qtpropertybrowser.QtProperty.setPropertyName(text:QString)",
    "qtpropertybrowser.QtProperty.setStatusTip(text:QString)",
    "qtpropertybrowser.QtProperty.setToolTip(text:QString)",
    "qtpropertybrowser.QtProperty.setWhatsThis(text:QString)",
    "qtpropertybrowser.QtProperty.statusTip()->QString",
    "qtpropertybrowser.QtProperty.subProperties()->QList[qtpropertybrowser.QtProperty]",
    "qtpropertybrowser.QtProperty.toolTip()->QString",
    "qtpropertybrowser.QtProperty.unitText()->QString",
    "qtpropertybrowser.QtProperty.valueIcon()->PySide2.QtGui.QIcon",
    "qtpropertybrowser.QtProperty.valueText()->QString",
    "qtpropertybrowser.QtProperty.whatsThis()->QString",
    nullptr}; // Sentinel

void init_QtProperty(PyObject *module)
{
    _Sbk_QtProperty_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtProperty",
        "QtProperty*",
        &Sbk_QtProperty_spec,
        QtProperty_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtProperty >,
        0,
        0,
        0    );
    
    SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtProperty_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtProperty_TypeF(),
        QtProperty_PythonToCpp_QtProperty_PTR,
        is_QtProperty_PythonToCpp_QtProperty_PTR_Convertible,
        QtProperty_PTR_CppToPython_QtProperty);

    Shiboken::Conversions::registerConverterName(converter, "QtProperty");
    Shiboken::Conversions::registerConverterName(converter, "QtProperty*");
    Shiboken::Conversions::registerConverterName(converter, "QtProperty&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtProperty).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtPropertyWrapper).name());



    QtPropertyWrapper::pysideInitQtMetaTypes();
}
