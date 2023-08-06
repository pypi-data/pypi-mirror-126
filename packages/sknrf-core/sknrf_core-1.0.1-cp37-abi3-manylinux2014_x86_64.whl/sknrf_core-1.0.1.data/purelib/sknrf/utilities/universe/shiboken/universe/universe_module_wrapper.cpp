
#include <sbkpython.h>
#include <shiboken.h>
#include <algorithm>
#include <signature.h>
#include "universe_python.h"



// Extra includes

// Current module's type array.
PyTypeObject **SbkuniverseTypes = nullptr;
// Current module's PyObject pointer.
PyObject *SbkuniverseModuleObject = nullptr;
// Current module's converter array.
SbkConverter **SbkuniverseTypeConverters = nullptr;
// Global functions ------------------------------------------------------------

static PyMethodDef universe_methods[] = {
    {0} // Sentinel
};

// Classes initialization functions ------------------------------------------------------------
void init_Truck(PyObject *module);
void init_Icecream(PyObject *module);


// Module initialization ------------------------------------------------------------
#if defined _WIN32 || defined __CYGWIN__
    #define SBK_EXPORT_MODULE __declspec(dllexport)
#elif __GNUC__ >= 4
    #define SBK_EXPORT_MODULE __attribute__ ((visibility("default")))
#else
    #define SBK_EXPORT_MODULE
#endif

#ifdef IS_PY3K
static struct PyModuleDef moduledef = {
    /* m_base     */ PyModuleDef_HEAD_INIT,
    /* m_name     */ "universe",
    /* m_doc      */ nullptr,
    /* m_size     */ -1,
    /* m_methods  */ universe_methods,
    /* m_reload   */ nullptr,
    /* m_traverse */ nullptr,
    /* m_clear    */ nullptr,
    /* m_free     */ nullptr
};

#endif

// The signatures string for the global functions.
// Multiple signatures have their index "n:" in front.
static const char *universe_SignatureStrings[] = {
    nullptr}; // Sentinel

SBK_MODULE_INIT_FUNCTION_BEGIN(universe)
    // Create an array of wrapper types for the current module.
    static PyTypeObject *cppApi[SBK_universe_IDX_COUNT];
    SbkuniverseTypes = cppApi;

    // Create an array of primitive type converters for the current module.
    static SbkConverter *sbkConverters[SBK_universe_CONVERTERS_IDX_COUNT];
    SbkuniverseTypeConverters = sbkConverters;

#ifdef IS_PY3K
    PyObject *module = Shiboken::Module::create("universe", &moduledef);
#else
    PyObject *module = Shiboken::Module::create("universe", universe_methods);
#endif

    // Make module available from global scope
    SbkuniverseModuleObject = module;

    // Initialize classes in the type system
    init_Truck(module);
    init_Icecream(module);
    // Register primitive types converters.

    Shiboken::Module::registerTypes(module, SbkuniverseTypes);
    Shiboken::Module::registerTypeConverters(module, SbkuniverseTypeConverters);

    if (PyErr_Occurred()) {
        PyErr_Print();
        Py_FatalError("can't initialize module universe");
    }
    FinishSignatureInitialization(module, universe_SignatureStrings);

SBK_MODULE_INIT_FUNCTION_END
