
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
#include "qtkeysequenceeditorfactory_wrapper.h"

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

void QtKeySequenceEditorFactoryWrapper::pysideInitQtMetaTypes()
{
}

QtKeySequenceEditorFactoryWrapper::QtKeySequenceEditorFactoryWrapper(QObject * parent) : QtKeySequenceEditorFactory(parent)
{
    // ... middle
}

void QtKeySequenceEditorFactoryWrapper::connectPropertyManager(QtKeySequencePropertyManager * manager)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "connectPropertyManager"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtKeySequenceEditorFactory::connectPropertyManager(manager);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QWidget * QtKeySequenceEditorFactoryWrapper::createAttributeEditor(QtKeySequencePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createAttributeEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtKeySequenceEditorFactory::createAttributeEditor(manager, property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNNN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), manager),
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtKeySequenceEditorFactory.createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtKeySequenceEditorFactoryWrapper::createEditor(QtKeySequencePropertyManager * manager, QtProperty * property, QWidget * parent)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtKeySequenceEditorFactory::createEditor(manager, property, parent);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), manager),
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtKeySequenceEditorFactory.createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtKeySequenceEditorFactoryWrapper::disconnectPropertyManager(QtKeySequencePropertyManager * manager)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "disconnectPropertyManager"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QtKeySequenceEditorFactory::disconnectPropertyManager(manager);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QtKeySequenceEditorFactoryWrapper::~QtKeySequenceEditorFactoryWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtKeySequenceEditorFactory_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtKeySequenceEditorFactory >()))
        return -1;

    ::QtKeySequenceEditorFactoryWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numNamedArgs = (kwds ? PyDict_Size(kwds) : 0);
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths
    if (numArgs + numNamedArgs > 1) {
        PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtKeySequenceEditorFactory(): too many arguments");
        return -1;
    }

    if (!PyArg_ParseTuple(args, "|O:QtKeySequenceEditorFactory", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtKeySequenceEditorFactory::QtKeySequenceEditorFactory(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtKeySequenceEditorFactory(QObject*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtKeySequenceEditorFactory(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtKeySequenceEditorFactory_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtKeySequenceEditorFactory(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0]))))
                    goto Sbk_QtKeySequenceEditorFactory_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtKeySequenceEditorFactory(QObject*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cptr = new ::QtKeySequenceEditorFactoryWrapper(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtKeySequenceEditorFactory >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtKeySequenceEditorFactory_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    Shiboken::Object::setHasCppWrapper(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_QtKeySequenceEditorFactory_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtKeySequenceEditorFactory");
        return -1;
}

static PyObject *Sbk_QtKeySequenceEditorFactoryFunc_connectPropertyManager(PyObject *self, PyObject *pyArg)
{
    QtKeySequenceEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtKeySequenceEditorFactoryWrapper *>(reinterpret_cast< ::QtKeySequenceEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtKeySequenceEditorFactory::connectPropertyManager(QtKeySequencePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), (pyArg)))) {
        overloadId = 0; // connectPropertyManager(QtKeySequencePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtKeySequenceEditorFactoryFunc_connectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtKeySequencePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // connectPropertyManager(QtKeySequencePropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtKeySequenceEditorFactoryWrapper *>(cppSelf)->QtKeySequenceEditorFactoryWrapper::connectPropertyManager_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtKeySequenceEditorFactoryFunc_connectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtKeySequenceEditorFactory.connectPropertyManager");
        return {};
}

static PyObject *Sbk_QtKeySequenceEditorFactoryFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    QtKeySequenceEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtKeySequenceEditorFactoryWrapper *>(reinterpret_cast< ::QtKeySequenceEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
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
    // 0: QtKeySequenceEditorFactory::createAttributeEditor(QtKeySequencePropertyManager*,QtProperty*,QWidget*,BrowserCol)
    if (numArgs == 4
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[2])))
        && (pythonToCpp[3] = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArgs[3])))) {
        overloadId = 0; // createAttributeEditor(QtKeySequencePropertyManager*,QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtKeySequenceEditorFactoryFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtKeySequencePropertyManager *cppArg0;
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
            // createAttributeEditor(QtKeySequencePropertyManager*,QtProperty*,QWidget*,BrowserCol)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = static_cast<::QtKeySequenceEditorFactoryWrapper *>(cppSelf)->QtKeySequenceEditorFactoryWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2, cppArg3);
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

    Sbk_QtKeySequenceEditorFactoryFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtKeySequenceEditorFactory.createAttributeEditor");
        return {};
}

static PyObject *Sbk_QtKeySequenceEditorFactoryFunc_createEditor(PyObject *self, PyObject *args)
{
    QtKeySequenceEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtKeySequenceEditorFactoryWrapper *>(reinterpret_cast< ::QtKeySequenceEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
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
    // 0: QtKeySequenceEditorFactory::createEditor(QtKeySequencePropertyManager*,QtProperty*,QWidget*)
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[2])))) {
        overloadId = 0; // createEditor(QtKeySequencePropertyManager*,QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtKeySequenceEditorFactoryFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtKeySequencePropertyManager *cppArg0;
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
            // createEditor(QtKeySequencePropertyManager*,QtProperty*,QWidget*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = static_cast<::QtKeySequenceEditorFactoryWrapper *>(cppSelf)->QtKeySequenceEditorFactoryWrapper::createEditor_protected(cppArg0, cppArg1, cppArg2);
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

    Sbk_QtKeySequenceEditorFactoryFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtKeySequenceEditorFactory.createEditor");
        return {};
}

static PyObject *Sbk_QtKeySequenceEditorFactoryFunc_disconnectPropertyManager(PyObject *self, PyObject *pyArg)
{
    QtKeySequenceEditorFactoryWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtKeySequenceEditorFactoryWrapper *>(reinterpret_cast< ::QtKeySequenceEditorFactory *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEEDITORFACTORY_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtKeySequenceEditorFactory::disconnectPropertyManager(QtKeySequencePropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]), (pyArg)))) {
        overloadId = 0; // disconnectPropertyManager(QtKeySequencePropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtKeySequenceEditorFactoryFunc_disconnectPropertyManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtKeySequencePropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // disconnectPropertyManager(QtKeySequencePropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtKeySequenceEditorFactoryWrapper *>(cppSelf)->QtKeySequenceEditorFactoryWrapper::disconnectPropertyManager_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtKeySequenceEditorFactoryFunc_disconnectPropertyManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtKeySequenceEditorFactory.disconnectPropertyManager");
        return {};
}

static PyMethodDef Sbk_QtKeySequenceEditorFactory_methods[] = {
    {"connectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtKeySequenceEditorFactoryFunc_connectPropertyManager), METH_O},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtKeySequenceEditorFactoryFunc_createAttributeEditor), METH_VARARGS},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtKeySequenceEditorFactoryFunc_createEditor), METH_VARARGS},
    {"disconnectPropertyManager", reinterpret_cast<PyCFunction>(Sbk_QtKeySequenceEditorFactoryFunc_disconnectPropertyManager), METH_O},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtKeySequenceEditorFactory_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtKeySequenceEditorFactory_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtKeySequenceEditorFactory_Type = nullptr;
static SbkObjectType *Sbk_QtKeySequenceEditorFactory_TypeF(void)
{
    return _Sbk_QtKeySequenceEditorFactory_Type;
}

static PyType_Slot Sbk_QtKeySequenceEditorFactory_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtKeySequenceEditorFactory_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtKeySequenceEditorFactory_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtKeySequenceEditorFactory_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtKeySequenceEditorFactory_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtKeySequenceEditorFactory_spec = {
    "qtpropertybrowser.QtKeySequenceEditorFactory",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtKeySequenceEditorFactory_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtKeySequenceEditorFactory_PythonToCpp_QtKeySequenceEditorFactory_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtKeySequenceEditorFactory_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtKeySequenceEditorFactory_PythonToCpp_QtKeySequenceEditorFactory_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtKeySequenceEditorFactory_TypeF())))
        return QtKeySequenceEditorFactory_PythonToCpp_QtKeySequenceEditorFactory_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtKeySequenceEditorFactory_PTR_CppToPython_QtKeySequenceEditorFactory(const void *cppIn) {
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::QtKeySequenceEditorFactory *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
     }
    PyObject *result = Shiboken::Object::newObject(Sbk_QtKeySequenceEditorFactory_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtKeySequenceEditorFactory_SignatureStrings[] = {
    "qtpropertybrowser.QtKeySequenceEditorFactory(parent:PySide2.QtCore.QObject=nullptr)",
    "qtpropertybrowser.QtKeySequenceEditorFactory.connectPropertyManager(manager:qtpropertybrowser.QtKeySequencePropertyManager)",
    "qtpropertybrowser.QtKeySequenceEditorFactory.createAttributeEditor(manager:qtpropertybrowser.QtKeySequencePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtKeySequenceEditorFactory.createEditor(manager:qtpropertybrowser.QtKeySequencePropertyManager,property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtKeySequenceEditorFactory.disconnectPropertyManager(manager:qtpropertybrowser.QtKeySequencePropertyManager)",
    nullptr}; // Sentinel

void init_QtKeySequenceEditorFactory(PyObject *module)
{
    _Sbk_QtKeySequenceEditorFactory_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtKeySequenceEditorFactory",
        "QtKeySequenceEditorFactory*",
        &Sbk_QtKeySequenceEditorFactory_spec,
        QtKeySequenceEditorFactory_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtKeySequenceEditorFactory >,
        0,
        0,
        0    );
    
    SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEEDITORFACTORY_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtKeySequenceEditorFactory_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtKeySequenceEditorFactory_TypeF(),
        QtKeySequenceEditorFactory_PythonToCpp_QtKeySequenceEditorFactory_PTR,
        is_QtKeySequenceEditorFactory_PythonToCpp_QtKeySequenceEditorFactory_PTR_Convertible,
        QtKeySequenceEditorFactory_PTR_CppToPython_QtKeySequenceEditorFactory);

    Shiboken::Conversions::registerConverterName(converter, "QtKeySequenceEditorFactory");
    Shiboken::Conversions::registerConverterName(converter, "QtKeySequenceEditorFactory*");
    Shiboken::Conversions::registerConverterName(converter, "QtKeySequenceEditorFactory&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtKeySequenceEditorFactory).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtKeySequenceEditorFactoryWrapper).name());



    QtKeySequenceEditorFactoryWrapper::pysideInitQtMetaTypes();
}
