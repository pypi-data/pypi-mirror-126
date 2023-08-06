
// default includes
#include <shiboken.h>
#include <typeinfo>

// module include
#include "universe_python.h"

// main header
#include "truck_wrapper.h"

// inner classes

// Extra includes
#include <icecream.h>
#include <truck.h>


#include <cctype>
#include <cstring>



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


// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_Truck_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::Truck >()))
        return -1;

    ::Truck *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numNamedArgs = (kwds ? PyDict_Size(kwds) : 0);
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths
    if (numArgs + numNamedArgs > 1) {
        PyErr_SetString(PyExc_TypeError, "universe.Truck(): too many arguments");
        return -1;
    }

    if (!PyArg_ParseTuple(args, "|O:Truck", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: Truck::Truck(bool)
    // 1: Truck::Truck(Truck)
    if (numArgs == 0) {
        overloadId = 0; // Truck(bool)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[0])))) {
        overloadId = 0; // Truck(bool)
    } else if (numArgs == 1
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppReferenceConvertible(reinterpret_cast<SbkObjectType *>(SbkuniverseTypes[SBK_TRUCK_IDX]), (pyArgs[0])))) {
        overloadId = 1; // Truck(Truck)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_Truck_Init_TypeError;

    // Call function/method
    switch (overloadId) {
        case 0: // Truck(bool leaveOnDestruction)
        {
            if (kwds) {
                PyObject *keyName = nullptr;
                PyObject *value = nullptr;
                keyName = Py_BuildValue("s","leaveOnDestruction");
                if (PyDict_Contains(kwds, keyName)) {
                value = PyDict_GetItemString(kwds, "leaveOnDestruction");
                if (value && pyArgs[0]) {
                    PyErr_SetString(PyExc_TypeError, "universe.Truck(): got multiple values for keyword argument 'leaveOnDestruction'.");
                    return -1;
                                } else if (value) {
                    pyArgs[0] = value;
                    if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArgs[0]))))
                        goto Sbk_Truck_Init_TypeError;
                }
}
            }
            bool cppArg0 = false;
            if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

            if (!PyErr_Occurred()) {
                // Truck(bool)
                PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
                cptr = new ::Truck(cppArg0);
                PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            }
            break;
        }
        case 1: // Truck(const Truck & other)
        {
            if (!Shiboken::Object::isValid(pyArgs[0]))
                return -1;
            ::Truck cppArg0_local;
            ::Truck *cppArg0 = &cppArg0_local;
            if (Shiboken::Conversions::isImplicitConversion(reinterpret_cast<SbkObjectType *>(SbkuniverseTypes[SBK_TRUCK_IDX]), pythonToCpp[0]))
                pythonToCpp[0](pyArgs[0], &cppArg0_local);
            else
                pythonToCpp[0](pyArgs[0], &cppArg0);


            if (!PyErr_Occurred()) {
                // Truck(Truck)
                PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
                cptr = new ::Truck(*cppArg0);
                PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            }
            break;
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::Truck >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_Truck_Init_TypeError;

    Shiboken::Object::setValidCpp(sbkSelf, true);
    if (Shiboken::BindingManager::instance().hasWrapper(cptr)) {
        Shiboken::BindingManager::instance().releaseWrapper(Shiboken::BindingManager::instance().retrieveWrapper(cptr));
    }
    Shiboken::BindingManager::instance().registerWrapper(sbkSelf, cptr);


    return 1;

    Sbk_Truck_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "universe.Truck");
        return -1;
}

static PyObject *Sbk_TruckFunc_addIcecreamFlavor(PyObject *self, PyObject *pyArg)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: Truck::addIcecreamFlavor(Icecream*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkuniverseTypes[SBK_ICECREAM_IDX]), (pyArg)))) {
        overloadId = 0; // addIcecreamFlavor(Icecream*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_TruckFunc_addIcecreamFlavor_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::Icecream *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // addIcecreamFlavor(Icecream*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->addIcecreamFlavor(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS

            // Ownership transferences.
            Shiboken::Object::releaseOwnership(pyArg);
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_TruckFunc_addIcecreamFlavor_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "universe.Truck.addIcecreamFlavor");
        return {};
}

static PyObject *Sbk_TruckFunc_arrive(PyObject *self)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // arrive()const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            const_cast<const ::Truck *>(cppSelf)->arrive();
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_TruckFunc_deliver(PyObject *self)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // deliver()const
            bool cppResult = const_cast<const ::Truck *>(cppSelf)->deliver();
            pyResult = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_TruckFunc_leave(PyObject *self)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // leave()const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            const_cast<const ::Truck *>(cppSelf)->leave();
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_TruckFunc_printAvailableFlavors(PyObject *self)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // printAvailableFlavors()const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            const_cast<const ::Truck *>(cppSelf)->printAvailableFlavors();
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_TruckFunc_setArrivalMessage(PyObject *self, PyObject *pyArg)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: Truck::setArrivalMessage(std::string)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<std::string>(), (pyArg)))) {
        overloadId = 0; // setArrivalMessage(std::string)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_TruckFunc_setArrivalMessage_TypeError;

    // Call function/method
    {
        ::std::string cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setArrivalMessage(std::string)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setArrivalMessage(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_TruckFunc_setArrivalMessage_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "universe.Truck.setArrivalMessage");
        return {};
}

static PyObject *Sbk_TruckFunc_setLeaveOnDestruction(PyObject *self, PyObject *pyArg)
{
    ::Truck *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: Truck::setLeaveOnDestruction(bool)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), (pyArg)))) {
        overloadId = 0; // setLeaveOnDestruction(bool)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_TruckFunc_setLeaveOnDestruction_TypeError;

    // Call function/method
    {
        bool cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setLeaveOnDestruction(bool)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setLeaveOnDestruction(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_TruckFunc_setLeaveOnDestruction_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "universe.Truck.setLeaveOnDestruction");
        return {};
}

static PyObject *Sbk_Truck___copy__(PyObject *self)
{
    if (!Shiboken::Object::isValid(self))
        return {};
    ::Truck &cppSelf =  *reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(self)));
    PyObject *pyResult = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkuniverseTypes[SBK_TRUCK_IDX]), &cppSelf);
    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyMethodDef Sbk_Truck_methods[] = {
    {"addIcecreamFlavor", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_addIcecreamFlavor), METH_O},
    {"arrive", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_arrive), METH_NOARGS},
    {"deliver", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_deliver), METH_NOARGS},
    {"leave", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_leave), METH_NOARGS},
    {"printAvailableFlavors", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_printAvailableFlavors), METH_NOARGS},
    {"setArrivalMessage", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_setArrivalMessage), METH_O},
    {"setLeaveOnDestruction", reinterpret_cast<PyCFunction>(Sbk_TruckFunc_setLeaveOnDestruction), METH_O},

    {"__copy__", reinterpret_cast<PyCFunction>(Sbk_Truck___copy__), METH_NOARGS},
    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_Truck_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_Truck_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_Truck_Type = nullptr;
static SbkObjectType *Sbk_Truck_TypeF(void)
{
    return _Sbk_Truck_Type;
}

static PyType_Slot Sbk_Truck_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_Truck_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_Truck_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_Truck_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_Truck_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_Truck_spec = {
    "universe.Truck",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_Truck_slots
};

} //extern "C"


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void Truck_PythonToCpp_Truck_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_Truck_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_Truck_PythonToCpp_Truck_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_Truck_TypeF())))
        return Truck_PythonToCpp_Truck_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *Truck_PTR_CppToPython_Truck(const void *cppIn) {
    auto pyOut = reinterpret_cast<PyObject *>(Shiboken::BindingManager::instance().retrieveWrapper(cppIn));
    if (pyOut) {
        Py_INCREF(pyOut);
        return pyOut;
    }
    bool changedTypeName = false;
    auto tCppIn = reinterpret_cast<const ::Truck *>(cppIn);
    const char *typeName = typeid(*tCppIn).name();
    auto sbkType = Shiboken::ObjectType::typeForTypeName(typeName);
    if (sbkType && Shiboken::ObjectType::hasSpecialCastFunction(sbkType)) {
        typeName = typeNameOf(tCppIn);
        changedTypeName = true;
     }
    PyObject *result = Shiboken::Object::newObject(Sbk_Truck_TypeF(), const_cast<void *>(cppIn), false, /* exactType */ changedTypeName, typeName);
    if (changedTypeName)
        delete [] typeName;
    return result;
}

// C++ to Python copy conversion.
static PyObject *Truck_COPY_CppToPython_Truck(const void *cppIn) {
    return Shiboken::Object::newObject(Sbk_Truck_TypeF(), new ::Truck(*reinterpret_cast<const ::Truck *>(cppIn)), true, true);
}

// Python to C++ copy conversion.
static void Truck_PythonToCpp_Truck_COPY(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::Truck *>(cppOut) = *reinterpret_cast< ::Truck *>(Shiboken::Conversions::cppPointer(SbkuniverseTypes[SBK_TRUCK_IDX], reinterpret_cast<SbkObject *>(pyIn)));
}
static PythonToCppFunc is_Truck_PythonToCpp_Truck_COPY_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_Truck_TypeF())))
        return Truck_PythonToCpp_Truck_COPY;
    return {};
}

// Implicit conversions.
static void bool_PythonToCpp_Truck(PyObject *pyIn, void *cppOut) {
    bool cppIn;
    Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyIn, &cppIn);
    *reinterpret_cast<::Truck *>(cppOut) = ::Truck(cppIn);
}
static PythonToCppFunc is_bool_PythonToCpp_Truck_Convertible(PyObject *pyIn) {
    if (PyBool_Check(pyIn))
        return bool_PythonToCpp_Truck;
    return {};
}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *Truck_SignatureStrings[] = {
    "1:universe.Truck(leaveOnDestruction:bool=false)",
    "0:universe.Truck(other:universe.Truck)",
    "universe.Truck.addIcecreamFlavor(icecream:universe.Icecream)",
    "universe.Truck.arrive()",
    "universe.Truck.deliver()->bool",
    "universe.Truck.leave()",
    "universe.Truck.printAvailableFlavors()",
    "universe.Truck.setArrivalMessage(message:std.string)",
    "universe.Truck.setLeaveOnDestruction(value:bool)",
    "universe.Truck.__copy__()",
    nullptr}; // Sentinel

void init_Truck(PyObject *module)
{
    _Sbk_Truck_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "Truck",
        "Truck",
        &Sbk_Truck_spec,
        Truck_SignatureStrings,
        &Shiboken::callCppDestructor< ::Truck >,
        0,
        0,
        0    );
    
    SbkuniverseTypes[SBK_TRUCK_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_Truck_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_Truck_TypeF(),
        Truck_PythonToCpp_Truck_PTR,
        is_Truck_PythonToCpp_Truck_PTR_Convertible,
        Truck_PTR_CppToPython_Truck,
        Truck_COPY_CppToPython_Truck);

    Shiboken::Conversions::registerConverterName(converter, "Truck");
    Shiboken::Conversions::registerConverterName(converter, "Truck*");
    Shiboken::Conversions::registerConverterName(converter, "Truck&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::Truck).name());

    // Add Python to C++ copy (value, not pointer neither reference) conversion to type converter.
    Shiboken::Conversions::addPythonToCppValueConversion(converter,
        Truck_PythonToCpp_Truck_COPY,
        is_Truck_PythonToCpp_Truck_COPY_Convertible);
    // Add implicit conversions to type converter.
    Shiboken::Conversions::addPythonToCppValueConversion(converter,
        bool_PythonToCpp_Truck,
        is_bool_PythonToCpp_Truck_Convertible);


}
