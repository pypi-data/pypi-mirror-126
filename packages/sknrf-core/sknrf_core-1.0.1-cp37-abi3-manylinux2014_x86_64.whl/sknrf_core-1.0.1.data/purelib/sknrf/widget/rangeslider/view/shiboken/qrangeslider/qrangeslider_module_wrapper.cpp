
#include <sbkpython.h>
#include <shiboken.h>
#include <algorithm>
#include <signature.h>
#ifndef QT_NO_VERSION_TAGGING
#  define QT_NO_VERSION_TAGGING
#endif
#include <QDebug>
#include <pyside.h>
#include <qapp_macro.h>
#include "qrangeslider_python.h"



// Extra includes

// Current module's type array.
PyTypeObject **SbkqrangesliderTypes = nullptr;
// Current module's PyObject pointer.
PyObject *SbkqrangesliderModuleObject = nullptr;
// Current module's converter array.
SbkConverter **SbkqrangesliderTypeConverters = nullptr;
void cleanTypesAttributes(void) {
    if (PY_VERSION_HEX >= 0x03000000 && PY_VERSION_HEX < 0x03060000)
        return; // PYSIDE-953: testbinding crashes in Python 3.5 when hasattr touches types!
    for (int i = 0, imax = SBK_qrangeslider_IDX_COUNT; i < imax; i++) {
        PyObject *pyType = reinterpret_cast<PyObject *>(SbkqrangesliderTypes[i]);
        if (pyType && PyObject_HasAttrString(pyType, "staticMetaObject"))
            PyObject_SetAttrString(pyType, "staticMetaObject", Py_None);
    }
}
// Global functions ------------------------------------------------------------

static PyMethodDef qrangeslider_methods[] = {
    {0} // Sentinel
};

// Classes initialization functions ------------------------------------------------------------
void init_QRangeSlider(PyObject *module);

// Required modules' type and converter arrays.
PyTypeObject **SbkPySide2_QtCoreTypes;
SbkConverter **SbkPySide2_QtCoreTypeConverters;
PyTypeObject **SbkPySide2_QtGuiTypes;
SbkConverter **SbkPySide2_QtGuiTypeConverters;
PyTypeObject **SbkPySide2_QtWidgetsTypes;
SbkConverter **SbkPySide2_QtWidgetsTypeConverters;

// Module initialization ------------------------------------------------------------
// Container Type converters.

// C++ to Python conversion for type 'QList<QAction* >'.
static PyObject *_QList_QActionPTR__CppToPython__QList_QActionPTR_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QAction* > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QAction* >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QAction* cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QACTION_IDX]), cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_QActionPTR__PythonToCpp__QList_QActionPTR_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QAction* > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QAction* cppItem{nullptr};
        Shiboken::Conversions::pythonToCppPointer(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QACTION_IDX]), pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_QActionPTR__PythonToCpp__QList_QActionPTR__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::checkSequenceTypes(SbkPySide2_QtWidgetsTypes[SBK_QACTION_IDX], pyIn))
        return _QList_QActionPTR__PythonToCpp__QList_QActionPTR_;
    return {};
}

// C++ to Python conversion for type 'QList<QVariant >'.
static PyObject *_QList_QVariant__CppToPython__QList_QVariant_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QVariant > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QVariant >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QVariant cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], &cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_QVariant__PythonToCpp__QList_QVariant_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QVariant > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QVariant cppItem;
        Shiboken::Conversions::pythonToCppCopy(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_QVariant__PythonToCpp__QList_QVariant__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyIn))
        return _QList_QVariant__PythonToCpp__QList_QVariant_;
    return {};
}

// C++ to Python conversion for type 'QList<QString >'.
static PyObject *_QList_QString__CppToPython__QList_QString_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QString > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QString >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QString cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_QString__PythonToCpp__QList_QString_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QString > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QString cppItem;
        Shiboken::Conversions::pythonToCppCopy(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_QString__PythonToCpp__QList_QString__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], pyIn))
        return _QList_QString__PythonToCpp__QList_QString_;
    return {};
}

// C++ to Python conversion for type 'QMap<QString,QVariant >'.
static PyObject *_QMap_QString_QVariant__CppToPython__QMap_QString_QVariant_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QMap<QString,QVariant > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cppmap_to_pymap_conversion - START
          PyObject *pyOut = PyDict_New();
          for (::QMap<QString,QVariant >::const_iterator it = cppInRef.begin(), end = cppInRef.end(); it != end; ++it) {
              ::QString key = it.key();
              ::QVariant value = it.value();
              PyObject *pyKey = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], &key);
              PyObject *pyValue = Shiboken::Conversions::copyToPython(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], &value);
              PyDict_SetItem(pyOut, pyKey, pyValue);
              Py_DECREF(pyKey);
              Py_DECREF(pyValue);
          }
          return pyOut;
    // TEMPLATE - cppmap_to_pymap_conversion - END

}
static void _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QMap<QString,QVariant > *>(cppOut);

                // TEMPLATE - pydict_to_cppmap_conversion - START
      PyObject *key;
      PyObject *value;
      Py_ssize_t pos = 0;
      while (PyDict_Next(pyIn, &pos, &key, &value)) {
          ::QString cppKey;
        Shiboken::Conversions::pythonToCppCopy(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], key, &(cppKey));
          ::QVariant cppValue;
        Shiboken::Conversions::pythonToCppCopy(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], value, &(cppValue));
          cppOutRef.insert(cppKey, cppValue);
      }
    // TEMPLATE - pydict_to_cppmap_conversion - END

}
static PythonToCppFunc is__QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleDictTypes(SbkPySide2_QtCoreTypeConverters[SBK_QSTRING_IDX], false, SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], false, pyIn))
        return _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_;
    return {};
}


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
    /* m_name     */ "qrangeslider",
    /* m_doc      */ nullptr,
    /* m_size     */ -1,
    /* m_methods  */ qrangeslider_methods,
    /* m_reload   */ nullptr,
    /* m_traverse */ nullptr,
    /* m_clear    */ nullptr,
    /* m_free     */ nullptr
};

#endif

// The signatures string for the global functions.
// Multiple signatures have their index "n:" in front.
static const char *qrangeslider_SignatureStrings[] = {
    nullptr}; // Sentinel

SBK_MODULE_INIT_FUNCTION_BEGIN(qrangeslider)
    {
        Shiboken::AutoDecRef requiredModule(Shiboken::Module::import("PySide2.QtCore"));
        if (requiredModule.isNull())
            return SBK_MODULE_INIT_ERROR;
        SbkPySide2_QtCoreTypes = Shiboken::Module::getTypes(requiredModule);
        SbkPySide2_QtCoreTypeConverters = Shiboken::Module::getTypeConverters(requiredModule);
    }

    {
        Shiboken::AutoDecRef requiredModule(Shiboken::Module::import("PySide2.QtGui"));
        if (requiredModule.isNull())
            return SBK_MODULE_INIT_ERROR;
        SbkPySide2_QtGuiTypes = Shiboken::Module::getTypes(requiredModule);
        SbkPySide2_QtGuiTypeConverters = Shiboken::Module::getTypeConverters(requiredModule);
    }

    {
        Shiboken::AutoDecRef requiredModule(Shiboken::Module::import("PySide2.QtWidgets"));
        if (requiredModule.isNull())
            return SBK_MODULE_INIT_ERROR;
        SbkPySide2_QtWidgetsTypes = Shiboken::Module::getTypes(requiredModule);
        SbkPySide2_QtWidgetsTypeConverters = Shiboken::Module::getTypeConverters(requiredModule);
    }

    // Create an array of wrapper types for the current module.
    static PyTypeObject *cppApi[SBK_qrangeslider_IDX_COUNT];
    SbkqrangesliderTypes = cppApi;

    // Create an array of primitive type converters for the current module.
    static SbkConverter *sbkConverters[SBK_qrangeslider_CONVERTERS_IDX_COUNT];
    SbkqrangesliderTypeConverters = sbkConverters;

#ifdef IS_PY3K
    PyObject *module = Shiboken::Module::create("qrangeslider", &moduledef);
#else
    PyObject *module = Shiboken::Module::create("qrangeslider", qrangeslider_methods);
#endif

    // Make module available from global scope
    SbkqrangesliderModuleObject = module;

    // Initialize classes in the type system
    init_QRangeSlider(module);

    // Register converter for type 'QList<QAction*>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QACTIONPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QActionPTR__CppToPython__QList_QActionPTR_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QACTIONPTR_IDX], "QList<QAction*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QACTIONPTR_IDX],
        _QList_QActionPTR__PythonToCpp__QList_QActionPTR_,
        is__QList_QActionPTR__PythonToCpp__QList_QActionPTR__Convertible);

    // Register converter for type 'QList<QVariant>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QVariant__CppToPython__QList_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QVARIANT_IDX], "QList<QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QVARIANT_IDX],
        _QList_QVariant__PythonToCpp__QList_QVariant_,
        is__QList_QVariant__PythonToCpp__QList_QVariant__Convertible);

    // Register converter for type 'QList<QString>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QSTRING_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QString__CppToPython__QList_QString_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QSTRING_IDX], "QList<QString>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QLIST_QSTRING_IDX],
        _QList_QString__PythonToCpp__QList_QString_,
        is__QList_QString__PythonToCpp__QList_QString__Convertible);

    // Register converter for type 'QMap<QString,QVariant>'.
    SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyDict_Type, _QMap_QString_QVariant__CppToPython__QMap_QString_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX], "QMap<QString,QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqrangesliderTypeConverters[SBK_QRANGESLIDER_QMAP_QSTRING_QVARIANT_IDX],
        _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_,
        is__QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant__Convertible);

    // Register primitive types converters.

    Shiboken::Module::registerTypes(module, SbkqrangesliderTypes);
    Shiboken::Module::registerTypeConverters(module, SbkqrangesliderTypeConverters);

    if (PyErr_Occurred()) {
        PyErr_Print();
        Py_FatalError("can't initialize module qrangeslider");
    }
    PySide::registerCleanupFunction(cleanTypesAttributes);

    FinishSignatureInitialization(module, qrangeslider_SignatureStrings);
    NotifyModuleForQApp(module, qApp);

SBK_MODULE_INIT_FUNCTION_END
