
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
#include "qtvariantproperty_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <qbrush.h>
#include <qicon.h>
#include <qtpropertybrowser.h>
#include <qtvariantproperty.h>


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

void QtVariantPropertyWrapper::pysideInitQtMetaTypes()
{
}

QtVariantPropertyWrapper::QtVariantPropertyWrapper(QtVariantPropertyManager * manager) : QtVariantProperty(manager)
{
    // ... middle
}

QtVariantPropertyWrapper::~QtVariantPropertyWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtVariantProperty_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtVariantProperty >()))
        return -1;

    ::QtVariantPropertyWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "QtVariantProperty", 1, 1, &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtVariantProperty::QtVariantProperty(QtVariantPropertyManager*)
    if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtVariantProperty(QtVariantPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantProperty_Init_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QtVariantPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtVariantProperty(QtVariantPropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cptr = new ::QtVariantPropertyWrapper(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtVariantProperty >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtVariantProperty_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtVariantProperty_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtVariantProperty");
        return -1;
}

static PyObject *Sbk_QtVariantPropertyFunc_attributeValue(PyObject *self, PyObject *pyArg)
{
    QtVariantPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantProperty::attributeValue(QString)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArg)))) {
        overloadId = 0; // attributeValue(QString)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyFunc_attributeValue_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // attributeValue(QString)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QVariant cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->attributeValue(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtVariantPropertyFunc_attributeValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtVariantProperty.attributeValue");
        return {};
}

static PyObject *Sbk_QtVariantPropertyFunc_propertyType(PyObject *self)
{
    QtVariantPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // propertyType()const
            int cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->propertyType();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyFunc_setAttribute(PyObject *self, PyObject *args)
{
    QtVariantPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setAttribute", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtVariantProperty::setAttribute(QString,QVariant)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], (pyArgs[1])))) {
        overloadId = 0; // setAttribute(QString,QVariant)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyFunc_setAttribute_TypeError;

    // Call function/method
    {
        ::QString cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        ::QVariant cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // setAttribute(QString,QVariant)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setAttribute(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyFunc_setAttribute_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtVariantProperty.setAttribute");
        return {};
}

static PyObject *Sbk_QtVariantPropertyFunc_setValue(PyObject *self, PyObject *pyArg)
{
    QtVariantPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtVariantProperty::setValue(QVariant)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], (pyArg)))) {
        overloadId = 0; // setValue(QVariant)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtVariantPropertyFunc_setValue_TypeError;

    // Call function/method
    {
        ::QVariant cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setValue(QVariant)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setValue(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtVariantPropertyFunc_setValue_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtVariantProperty.setValue");
        return {};
}

static PyObject *Sbk_QtVariantPropertyFunc_value(PyObject *self)
{
    QtVariantPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // value()const
            QVariant cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->value();
            pyResult = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtVariantPropertyFunc_valueType(PyObject *self)
{
    QtVariantPropertyWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtVariantPropertyWrapper *>(reinterpret_cast< ::QtVariantProperty *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // valueType()const
            int cppResult = const_cast<const ::QtVariantPropertyWrapper *>(cppSelf)->valueType();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyMethodDef Sbk_QtVariantProperty_methods[] = {
    {"attributeValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_attributeValue), METH_O},
    {"propertyType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_propertyType), METH_NOARGS},
    {"setAttribute", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_setAttribute), METH_VARARGS},
    {"setValue", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_setValue), METH_O},
    {"value", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_value), METH_NOARGS},
    {"valueType", reinterpret_cast<PyCFunction>(Sbk_QtVariantPropertyFunc_valueType), METH_NOARGS},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtVariantProperty_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtVariantProperty_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtVariantProperty_Type = nullptr;
static SbkObjectType *Sbk_QtVariantProperty_TypeF(void)
{
    return _Sbk_QtVariantProperty_Type;
}

static PyType_Slot Sbk_QtVariantProperty_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtVariantProperty_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtVariantProperty_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtVariantProperty_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtVariantProperty_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtVariantProperty_spec = {
    "qtpropertybrowser.QtVariantProperty",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtVariantProperty_slots
};

} //extern "C"

static void *Sbk_QtVariantProperty_typeDiscovery(void *cptr, SbkObjectType *instanceType)
{
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QtProperty >()))
        return dynamic_cast< ::QtVariantProperty *>(reinterpret_cast< ::QtProperty *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtVariantProperty_PythonToCpp_QtVariantProperty_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtVariantProperty_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtVariantProperty_PythonToCpp_QtVariantProperty_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtVariantProperty_TypeF())))
        return QtVariantProperty_PythonToCpp_QtVariantProperty_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtVariantProperty_PTR_CppToPython_QtVariantProperty(const void *cppIn) {
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtVariantProperty *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
     }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtVariantProperty_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtVariantProperty_SignatureStrings[] = {
    "qtpropertybrowser.QtVariantProperty(manager:qtpropertybrowser.QtVariantPropertyManager)",
    "qtpropertybrowser.QtVariantProperty.attributeValue(attribute:QString)->QVariant",
    "qtpropertybrowser.QtVariantProperty.propertyType()->int",
    "qtpropertybrowser.QtVariantProperty.setAttribute(attribute:QString,value:QVariant)",
    "qtpropertybrowser.QtVariantProperty.setValue(value:QVariant)",
    "qtpropertybrowser.QtVariantProperty.value()->QVariant",
    "qtpropertybrowser.QtVariantProperty.valueType()->int",
    nullptr}; // Sentinel

void init_QtVariantProperty(PyObject *module)
{
    _Sbk_QtVariantProperty_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtVariantProperty",
        "QtVariantProperty*",
        &Sbk_QtVariantProperty_spec,
        QtVariantProperty_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtVariantProperty >,
        reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]),
        0,
        0    );
    
    SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtVariantProperty_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtVariantProperty_TypeF(),
        QtVariantProperty_PythonToCpp_QtVariantProperty_PTR,
        is_QtVariantProperty_PythonToCpp_QtVariantProperty_PTR_Convertible,
        QtVariantProperty_PTR_CppToPython_QtVariantProperty);

    Shiboken::Conversions::registerConverterName(converter, "QtVariantProperty");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantProperty*");
    Shiboken::Conversions::registerConverterName(converter, "QtVariantProperty&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantProperty).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtVariantPropertyWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtVariantProperty_TypeF(), &Sbk_QtVariantProperty_typeDiscovery);


    QtVariantPropertyWrapper::pysideInitQtMetaTypes();
}
