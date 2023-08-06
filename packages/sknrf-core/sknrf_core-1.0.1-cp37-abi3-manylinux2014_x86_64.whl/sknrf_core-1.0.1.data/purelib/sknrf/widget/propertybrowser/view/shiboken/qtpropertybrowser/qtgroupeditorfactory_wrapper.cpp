
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
#include "qtgroupeditorfactory_wrapper.h"

// inner classes

// Extra includes
#include <qobject.h>
#include <qtpropertybrowser.h>
#include <qtpropertymanager.h>
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

void QtGroupEditorFactoryWrapper::pysideInitQtMetaTypes()
{
}

QtGroupEditorFactoryWrapper::QtGroupEditorFactoryWrapper(QObject * parent) : QtGroupEditorFactory(parent)
{
    // ... middle
}

void QtGroupEditorFactoryWrapper::connectPropertyManager(QtGroupPropertyManager * manager)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "connectPropertyManager"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtGroupEditorFactory::connectPropertyManager(manager);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QWidget * QtGroupEditorFactoryWrapper::createAttributeEditor(QtGroupPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createAttributeEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtGroupEditorFactory::createAttributeEditor(manager, property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNNN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), manager),
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtGroupEditorFactory.createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtGroupEditorFactoryWrapper::createEditor(QtGroupPropertyManager * manager, QtProperty * property, QWidget * parent)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtGroupEditorFactory::createEditor(manager, property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), manager),
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtGroupEditorFactory.createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtGroupEditorFactoryWrapper::disconnectPropertyManager(QtGroupPropertyManager * manager)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "disconnectPropertyManager"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtGroupEditorFactory::disconnectPropertyManager(manager);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QtGroupEditorFactoryWrapper::~QtGroupEditorFactoryWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtGroupEditorFactory_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtGroupEditorFactory >()))
        return -1;

    ::QtGroupEditorFactoryWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numNamedArgs = (kwds ? PyDict_Size(kwds) : 0);
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths
    if (numArgs + numNamedArgs > 1) {
        PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtGroupEditorFactory(): too many arguments");
        return -1;
    }

    if (!PyArg_ParseTuple(args, "|O:QtGroupEditorFactory", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtGroupEditorFactory::QtGroupEditorFactory(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtGroupEditorFactory(QObject*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtGroupEditorFactory(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtGroupEditorFactory_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtGroupEditorFactory(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0]))))
                    goto Sbk_QtGroupEditorFactory_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtGroupEditorFactory(QObject*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cptr = new ::QtGroupEditorFactoryWrapper(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtGroupEditorFactory >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtGroupEditorFactory_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtGroupEditorFactory_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtGroupEditorFactory");
        return -1;
}

static PyObject *Sbk_QtGroupEditorFactoryFunc_connectPropertyManager(PyObject *self, PyObject *pyArg)
{
    QtGroupEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtGroupEditorFactoryWrapper *>(reinterpret_cast< ::QtGroupEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTGROUPEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtGroupEditorFactory::connectPropertyManager(QtGroupPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), (pyArg)))) {
        overloadId = 0; // connectPropertyManager(QtGroupPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtGroupEditorFactoryFunc_connectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtGroupPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // connectPropertyManager(QtGroupPropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtGroupEditorFactoryWrapper *>(cppSelf)->QtGroupEditorFactoryWrapper::connectPropertyManager_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtGroupEditorFactoryFunc_connectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtGroupEditorFactory.connectPropertyManager");
        return {};
}

static PyObject *Sbk_QtGroupEditorFactoryFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    QtGroupEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtGroupEditorFactoryWrapper *>(reinterpret_cast< ::QtGroupEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTGROUPEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr, nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0, 0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "createAttributeEditor", 4, 4, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2]), &(pyArgs[3])))
        return {};


    // Overloaded function decisor
    // 0: QtGroupEditorFactory::createAttributeEditor(QtGroupPropertyManager*,QtProperty*,QWidget*,BrowserCol)
    if (numArgs == 4
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[2])))
        && (pythonToCpp[3] = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArgs[3])))) {
        overloadId = 0; // createAttributeEditor(QtGroupPropertyManager*,QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtGroupEditorFactoryFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtGroupPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        if (!Shiboken::Object::isValid(pyArgs[2]))
            return {};
        ::QWidget *cppArg2;
        pythonToCpp[2](pyArgs[2], &cppArg2);
        ::BrowserCol cppArg3{NONE};
        pythonToCpp[3](pyArgs[3], &cppArg3);

        if (!PyErr_Occurred()) {
            // createAttributeEditor(QtGroupPropertyManager*,QtProperty*,QWidget*,BrowserCol)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = static_cast<::QtGroupEditorFactoryWrapper *>(cppSelf)->QtGroupEditorFactoryWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2, cppArg3);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtGroupEditorFactoryFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtGroupEditorFactory.createAttributeEditor");
        return {};
}

static PyObject *Sbk_QtGroupEditorFactoryFunc_createEditor(PyObject *self, PyObject *args)
{
    QtGroupEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtGroupEditorFactoryWrapper *>(reinterpret_cast< ::QtGroupEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTGROUPEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "createEditor", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtGroupEditorFactory::createEditor(QtGroupPropertyManager*,QtProperty*,QWidget*)
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[2])))) {
        overloadId = 0; // createEditor(QtGroupPropertyManager*,QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtGroupEditorFactoryFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtGroupPropertyManager *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        if (!Shiboken::Object::isValid(pyArgs[2]))
            return {};
        ::QWidget *cppArg2;
        pythonToCpp[2](pyArgs[2], &cppArg2);

        if (!PyErr_Occurred()) {
            // createEditor(QtGroupPropertyManager*,QtProperty*,QWidget*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = static_cast<::QtGroupEditorFactoryWrapper *>(cppSelf)->QtGroupEditorFactoryWrapper::createEditor_protected(cppArg0, cppArg1, cppArg2);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtGroupEditorFactoryFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtGroupEditorFactory.createEditor");
        return {};
}

static PyObject *Sbk_QtGroupEditorFactoryFunc_disconnectPropertyManager(PyObject *self, PyObject *pyArg)
{
    QtGroupEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtGroupEditorFactoryWrapper *>(reinterpret_cast< ::QtGroupEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTGROUPEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtGroupEditorFactory::disconnectPropertyManager(QtGroupPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]), (pyArg)))) {
        overloadId = 0; // disconnectPropertyManager(QtGroupPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtGroupEditorFactoryFunc_disconnectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtGroupPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // disconnectPropertyManager(QtGroupPropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtGroupEditorFactoryWrapper *>(cppSelf)->QtGroupEditorFactoryWrapper::disconnectPropertyManager_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtGroupEditorFactoryFunc_disconnectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtGroupEditorFactory.disconnectPropertyManager");
        return {};
}

static PyMethodDef Sbk_QtGroupEditorFactory_methods[] = {
    {"connectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtGroupEditorFactoryFunc_connectPropertyManager), METH_O},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtGroupEditorFactoryFunc_createAttributeEditor), METH_VARARGS},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtGroupEditorFactoryFunc_createEditor), METH_VARARGS},
    {"disconnectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtGroupEditorFactoryFunc_disconnectPropertyManager), METH_O},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtGroupEditorFactory_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtGroupEditorFactory_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtGroupEditorFactory_Type = nullptr;
static SbkObjectType *Sbk_QtGroupEditorFactory_TypeF(void)
{
    return _Sbk_QtGroupEditorFactory_Type;
}

static PyType_Slot Sbk_QtGroupEditorFactory_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtGroupEditorFactory_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtGroupEditorFactory_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtGroupEditorFactory_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtGroupEditorFactory_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtGroupEditorFactory_spec = {
    "qtpropertybrowser.QtGroupEditorFactory",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtGroupEditorFactory_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtGroupEditorFactory_PythonToCpp_QtGroupEditorFactory_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtGroupEditorFactory_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtGroupEditorFactory_PythonToCpp_QtGroupEditorFactory_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtGroupEditorFactory_TypeF())))
        return QtGroupEditorFactory_PythonToCpp_QtGroupEditorFactory_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtGroupEditorFactory_PTR_CppToPython_QtGroupEditorFactory(const void *cppIn) {
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtGroupEditorFactory *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
     }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtGroupEditorFactory_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtGroupEditorFactory_SignatureStrings[] = {
    "qtpropertybrowser.QtGroupEditorFactory(parent:PySide2.QtCore.QObject=nullptr)",
    "qtpropertybrowser.QtGroupEditorFactory.connectPropertyManager(manager:qtpropertybrowser.QtGroupPropertyManager)",
    "qtpropertybrowser.QtGroupEditorFactory.createAttributeEditor(manager:qtpropertybrowser.QtGroupPropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtGroupEditorFactory.createEditor(manager:qtpropertybrowser.QtGroupPropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtGroupEditorFactory.disconnectPropertyManager(manager:qtpropertybrowser.QtGroupPropertyManager)",
    nullptr}; // Sentinel

void init_QtGroupEditorFactory(PyObject *module)
{
    _Sbk_QtGroupEditorFactory_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtGroupEditorFactory",
        "QtGroupEditorFactory*",
        &Sbk_QtGroupEditorFactory_spec,
        QtGroupEditorFactory_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtGroupEditorFactory >,
        0,
        0,
        0    );
    
    SbkqtpropertybrowserTypes[SBK_QTGROUPEDITORFACTORY_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtGroupEditorFactory_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtGroupEditorFactory_TypeF(),
        QtGroupEditorFactory_PythonToCpp_QtGroupEditorFactory_PTR,
        is_QtGroupEditorFactory_PythonToCpp_QtGroupEditorFactory_PTR_Convertible,
        QtGroupEditorFactory_PTR_CppToPython_QtGroupEditorFactory);

    Shiboken::Conversions::registerConverterName(converter, "QtGroupEditorFactory");
    Shiboken::Conversions::registerConverterName(converter, "QtGroupEditorFactory*");
    Shiboken::Conversions::registerConverterName(converter, "QtGroupEditorFactory&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtGroupEditorFactory).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtGroupEditorFactoryWrapper).name());



    QtGroupEditorFactoryWrapper::pysideInitQtMetaTypes();
}
