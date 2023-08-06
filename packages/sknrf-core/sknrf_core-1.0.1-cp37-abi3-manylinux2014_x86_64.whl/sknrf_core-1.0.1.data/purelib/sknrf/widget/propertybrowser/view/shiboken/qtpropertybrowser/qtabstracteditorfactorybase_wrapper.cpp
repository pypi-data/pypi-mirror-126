
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
#include "qtabstracteditorfactorybase_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <qbytearray.h>
#include <qobject.h>
#include <qobjectdefs.h>
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

void QtAbstractEditorFactoryBaseWrapper::pysideInitQtMetaTypes()
{
}

QtAbstractEditorFactoryBaseWrapper::QtAbstractEditorFactoryBaseWrapper(QObject * parent) : QtAbstractEditorFactoryBase(parent)
{
    // ... middle
}

void QtAbstractEditorFactoryBaseWrapper::breakConnection(QtAbstractPropertyManager * manager)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "breakConnection"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.breakConnection()' not implemented.");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]), manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtAbstractEditorFactoryBaseWrapper::childEvent(QChildEvent * event)
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

void QtAbstractEditorFactoryBaseWrapper::connectNotify(const QMetaMethod & signal)
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

QWidget * QtAbstractEditorFactoryBaseWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol atttribute)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createAttributeEditor"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.createAttributeEditor()' not implemented.");
        return nullptr;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), property),
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), parent),
        Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &atttribute)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractEditorFactoryBase.createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtAbstractEditorFactoryBaseWrapper::createEditor(QtProperty * property, QWidget * parent)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createEditor"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.createEditor()' not implemented.");
        return nullptr;
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractEditorFactoryBase.createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractEditorFactoryBaseWrapper::customEvent(QEvent * event)
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

void QtAbstractEditorFactoryBaseWrapper::disconnectNotify(const QMetaMethod & signal)
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

bool QtAbstractEditorFactoryBaseWrapper::event(QEvent * event)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractEditorFactoryBase.event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    return cppResult;
}

bool QtAbstractEditorFactoryBaseWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractEditorFactoryBase.eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    return cppResult;
}

void QtAbstractEditorFactoryBaseWrapper::managerDestroyed(QObject * manager)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "managerDestroyed"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.managerDestroyed()' not implemented.");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), manager)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtAbstractEditorFactoryBaseWrapper::timerEvent(QTimerEvent * event)
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

const QMetaObject *QtAbstractEditorFactoryBaseWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtAbstractEditorFactoryBase::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtAbstractEditorFactoryBaseWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtAbstractEditorFactoryBase::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtAbstractEditorFactoryBaseWrapper::qt_metacast(const char *_clname)
{
        if (!_clname) return {};
        SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
        if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
                return static_cast<void *>(const_cast< QtAbstractEditorFactoryBaseWrapper *>(this));
        return QtAbstractEditorFactoryBase::qt_metacast(_clname);
}

QtAbstractEditorFactoryBaseWrapper::~QtAbstractEditorFactoryBaseWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtAbstractEditorFactoryBase_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    const char *argNames[] = {"parent"};
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    SbkObjectType *type = reinterpret_cast<SbkObjectType *>(self->ob_type);
    SbkObjectType *myType = reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX]);
    if (type == myType) {
        PyErr_SetString(PyExc_NotImplementedError,
            "'QtAbstractEditorFactoryBase' represents a C++ abstract class and cannot be instantiated");
        return -1;
    }

    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtAbstractEditorFactoryBase >()))
        return -1;

    ::QtAbstractEditorFactoryBaseWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_ParseTuple(args, "|O:QtAbstractEditorFactoryBase", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::QtAbstractEditorFactoryBase(QObject*)
    if (numArgs == 0) {
        overloadId = 0; // QtAbstractEditorFactoryBase(QObject*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtAbstractEditorFactoryBase(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtAbstractEditorFactoryBase(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArgs[0]))))
                    goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QObject *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtAbstractEditorFactoryBase(QObject*)
            void *addr = PySide::nextQObjectMemoryAddr();
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            if (addr) {
                cptr = new (addr) ::QtAbstractEditorFactoryBaseWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(0);
            } else {
                cptr = new ::QtAbstractEditorFactoryBaseWrapper(cppArg0);
            }

            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtAbstractEditorFactoryBase >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtAbstractEditorFactoryBase_Init_TypeError;

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

    Sbk_QtAbstractEditorFactoryBase_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractEditorFactoryBase");
        return -1;
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection(PyObject *self, PyObject *pyArg)
{
    QtAbstractEditorFactoryBaseWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::breakConnection(QtAbstractPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]), (pyArg)))) {
        overloadId = 0; // breakConnection(QtAbstractPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtAbstractPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // breakConnection(QtAbstractPropertyManager*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.breakConnection()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtAbstractEditorFactoryBaseWrapper *>(cppSelf)->breakConnection_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractEditorFactoryBase.breakConnection");
        return {};
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    QtAbstractEditorFactoryBaseWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "createAttributeEditor", 3, 3, &(pyArgs[0]), &(pyArgs[1]), &(pyArgs[2])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArgs[2])))) {
        overloadId = 0; // createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QWidget *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);
        ::BrowserCol cppArg2{NONE};
        pythonToCpp[2](pyArgs[2], &cppArg2);

        if (!PyErr_Occurred()) {
            // createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.createAttributeEditor()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = cppSelf->createAttributeEditor(cppArg0, cppArg1, cppArg2);
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

    Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractEditorFactoryBase.createAttributeEditor");
        return {};
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_createEditor(PyObject *self, PyObject *args)
{
    QtAbstractEditorFactoryBaseWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "createEditor", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::createEditor(QtProperty*,QWidget*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[1])))) {
        overloadId = 0; // createEditor(QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_createEditor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QWidget *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // createEditor(QtProperty*,QWidget*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.createEditor()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = cppSelf->createEditor(cppArg0, cppArg1);
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

    Sbk_QtAbstractEditorFactoryBaseFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractEditorFactoryBase.createEditor");
        return {};
}

static PyObject *Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed(PyObject *self, PyObject *pyArg)
{
    QtAbstractEditorFactoryBaseWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractEditorFactoryBaseWrapper *>(reinterpret_cast< ::QtAbstractEditorFactoryBase *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractEditorFactoryBase::managerDestroyed(QObject*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), (pyArg)))) {
        overloadId = 0; // managerDestroyed(QObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QObject *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // managerDestroyed(QObject*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractEditorFactoryBase.managerDestroyed()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtAbstractEditorFactoryBaseWrapper *>(cppSelf)->managerDestroyed_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractEditorFactoryBase.managerDestroyed");
        return {};
}

static PyMethodDef Sbk_QtAbstractEditorFactoryBase_methods[] = {
    {"breakConnection", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_breakConnection), METH_O},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_createAttributeEditor), METH_VARARGS},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_createEditor), METH_VARARGS},
    {"managerDestroyed", reinterpret_cast<PyCFunction>(Sbk_QtAbstractEditorFactoryBaseFunc_managerDestroyed), METH_O},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtAbstractEditorFactoryBase_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtAbstractEditorFactoryBase_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtAbstractEditorFactoryBase_Type = nullptr;
static SbkObjectType *Sbk_QtAbstractEditorFactoryBase_TypeF(void)
{
    return _Sbk_QtAbstractEditorFactoryBase_Type;
}

static PyType_Slot Sbk_QtAbstractEditorFactoryBase_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtAbstractEditorFactoryBase_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtAbstractEditorFactoryBase_spec = {
    "qtpropertybrowser.QtAbstractEditorFactoryBase",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtAbstractEditorFactoryBase_slots
};

} //extern "C"

static void *Sbk_QtAbstractEditorFactoryBase_typeDiscovery(void *cptr, SbkObjectType *instanceType)
{
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QObject >()))
        return dynamic_cast< ::QtAbstractEditorFactoryBase *>(reinterpret_cast< ::QObject *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtAbstractEditorFactoryBase_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtAbstractEditorFactoryBase_TypeF())))
        return QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtAbstractEditorFactoryBase_PTR_CppToPython_QtAbstractEditorFactoryBase(const void *cppIn) {
    return PySide::getWrapperForQObject(reinterpret_cast<::QtAbstractEditorFactoryBase *>(const_cast<void *>(cppIn)), Sbk_QtAbstractEditorFactoryBase_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtAbstractEditorFactoryBase_SignatureStrings[] = {
    "qtpropertybrowser.QtAbstractEditorFactoryBase(parent:PySide2.QtCore.QObject=nullptr)",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.breakConnection(manager:qtpropertybrowser.QtAbstractPropertyManager)",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.createAttributeEditor(property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget,atttribute:qtpropertybrowser.BrowserCol)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.createEditor(property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractEditorFactoryBase.managerDestroyed(manager:PySide2.QtCore.QObject)",
    nullptr}; // Sentinel

void init_QtAbstractEditorFactoryBase(PyObject *module)
{
    _Sbk_QtAbstractEditorFactoryBase_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtAbstractEditorFactoryBase",
        "QtAbstractEditorFactoryBase*",
        &Sbk_QtAbstractEditorFactoryBase_spec,
        QtAbstractEditorFactoryBase_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtAbstractEditorFactoryBase >,
        reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]),
        0,
        0    );
    
    SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtAbstractEditorFactoryBase_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtAbstractEditorFactoryBase_TypeF(),
        QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR,
        is_QtAbstractEditorFactoryBase_PythonToCpp_QtAbstractEditorFactoryBase_PTR_Convertible,
        QtAbstractEditorFactoryBase_PTR_CppToPython_QtAbstractEditorFactoryBase);

    Shiboken::Conversions::registerConverterName(converter, "QtAbstractEditorFactoryBase");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractEditorFactoryBase*");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractEditorFactoryBase&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractEditorFactoryBase).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractEditorFactoryBaseWrapper).name());


    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtAbstractEditorFactoryBase_TypeF(), &Sbk_QtAbstractEditorFactoryBase_typeDiscovery);

    PySide::Signal::registerSignals(Sbk_QtAbstractEditorFactoryBase_TypeF(), &::QtAbstractEditorFactoryBase::staticMetaObject);

    QtAbstractEditorFactoryBaseWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(Sbk_QtAbstractEditorFactoryBase_TypeF(), &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(Sbk_QtAbstractEditorFactoryBase_TypeF(), &::QtAbstractEditorFactoryBase::staticMetaObject, sizeof(::QtAbstractEditorFactoryBase));
}
