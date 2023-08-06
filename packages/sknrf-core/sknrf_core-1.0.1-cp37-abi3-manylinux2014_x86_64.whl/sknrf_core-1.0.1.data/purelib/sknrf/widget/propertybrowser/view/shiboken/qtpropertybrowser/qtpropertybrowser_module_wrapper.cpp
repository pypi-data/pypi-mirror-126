
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
#include "qtpropertybrowser_python.h"



// Extra includes

// Current module's type array.
PyTypeObject **SbkqtpropertybrowserTypes = nullptr;
// Current module's PyObject pointer.
PyObject *SbkqtpropertybrowserModuleObject = nullptr;
// Current module's converter array.
SbkConverter **SbkqtpropertybrowserTypeConverters = nullptr;
void cleanTypesAttributes(void) {
    if (PY_VERSION_HEX >= 0x03000000 && PY_VERSION_HEX < 0x03060000)
        return; // PYSIDE-953: testbinding crashes in Python 3.5 when hasattr touches types!
    for (int i = 0, imax = SBK_qtpropertybrowser_IDX_COUNT; i < imax; i++) {
        PyObject *pyType = reinterpret_cast<PyObject *>(SbkqtpropertybrowserTypes[i]);
        if (pyType && PyObject_HasAttrString(pyType, "staticMetaObject"))
            PyObject_SetAttrString(pyType, "staticMetaObject", Py_None);
    }
}
// Global functions ------------------------------------------------------------

static PyMethodDef qtpropertybrowser_methods[] = {
    {0} // Sentinel
};

// Classes initialization functions ------------------------------------------------------------
void init_QtVariantEditorFactory(PyObject *module);
void init_QtTimeEditFactory(PyObject *module);
void init_QtTFTensorEditFactory(PyObject *module);
void init_QtSpinBoxFactory(PyObject *module);
void init_QtSliderFactory(PyObject *module);
void init_QtSizePolicyEditorFactory(PyObject *module);
void init_QtSizeFEditorFactory(PyObject *module);
void init_QtSizeEditorFactory(PyObject *module);
void init_QtScrollBarFactory(PyObject *module);
void init_QtRectFEditorFactory(PyObject *module);
void init_QtRectEditorFactory(PyObject *module);
void init_QtProperty(PyObject *module);
void init_QtVariantProperty(PyObject *module);
void init_QtPointFEditorFactory(PyObject *module);
void init_QtPointEditorFactory(PyObject *module);
void init_QtLocaleEditorFactory(PyObject *module);
void init_QtLineEditFactory(PyObject *module);
void init_QtKeySequenceEditorFactory(PyObject *module);
void init_QtIntEditFactory(PyObject *module);
void init_QtGroupEditorFactory(PyObject *module);
void init_QtFontEditorFactory(PyObject *module);
void init_QtFlagEditorFactory(PyObject *module);
void init_QtFileEditorFactory(PyObject *module);
void init_QtEnumEditorFactory(PyObject *module);
void init_QtDoubleSpinBoxFactory(PyObject *module);
void init_QtDoubleEditFactory(PyObject *module);
void init_QtDateTimeEditFactory(PyObject *module);
void init_QtDateEditFactory(PyObject *module);
void init_QtCursorEditorFactory(PyObject *module);
void init_QtComplexEditFactory(PyObject *module);
void init_QtColorEditorFactory(PyObject *module);
void init_QtCheckBoxFactory(PyObject *module);
void init_QtCharEditorFactory(PyObject *module);
void init_QtBrowserItem(PyObject *module);
void init_QtAbstractPropertyBrowser(PyObject *module);
void init_QtGroupBoxPropertyBrowser(PyObject *module);
void init_QtTreePropertyBrowser(PyObject *module);
void init_QtButtonPropertyBrowser(PyObject *module);
void init_QtAbstractPropertyManager(PyObject *module);
void init_QtTimePropertyManager(PyObject *module);
void init_QtFilePropertyManager(PyObject *module);
void init_QtTFTensorPropertyManager(PyObject *module);
void init_QtEnumPropertyManager(PyObject *module);
void init_QtStringPropertyManager(PyObject *module);
void init_QtDoublePropertyManager(PyObject *module);
void init_QtSizePropertyManager(PyObject *module);
void init_QtDateTimePropertyManager(PyObject *module);
void init_QtSizePolicyPropertyManager(PyObject *module);
void init_QtDatePropertyManager(PyObject *module);
void init_QtSizeFPropertyManager(PyObject *module);
void init_QtCursorPropertyManager(PyObject *module);
void init_QtComplexPropertyManager(PyObject *module);
void init_QtRectPropertyManager(PyObject *module);
void init_QtRectFPropertyManager(PyObject *module);
void init_QtColorPropertyManager(PyObject *module);
void init_QtCharPropertyManager(PyObject *module);
void init_QtPointPropertyManager(PyObject *module);
void init_QtPointFPropertyManager(PyObject *module);
void init_QtBoolPropertyManager(PyObject *module);
void init_QtLocalePropertyManager(PyObject *module);
void init_QtKeySequencePropertyManager(PyObject *module);
void init_QtIntPropertyManager(PyObject *module);
void init_QtGroupPropertyManager(PyObject *module);
void init_QtVariantPropertyManager(PyObject *module);
void init_QtFontPropertyManager(PyObject *module);
void init_QtFlagPropertyManager(PyObject *module);
void init_QtAbstractEditorFactoryBase(PyObject *module);

// Enum definitions ------------------------------------------------------------
static void BrowserCol_PythonToCpp_BrowserCol(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::BrowserCol *>(cppOut) =
        static_cast<::BrowserCol>(Shiboken::Enum::getValue(pyIn));

}
static PythonToCppFunc is_BrowserCol_PythonToCpp_BrowserCol_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]))
        return BrowserCol_PythonToCpp_BrowserCol;
    return {};
}
static PyObject *BrowserCol_CppToPython_BrowserCol(const void *cppIn) {
    const int castCppIn = int(*reinterpret_cast<const ::BrowserCol *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX], castCppIn);

}


static void Domain_PythonToCpp_Domain(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::Domain *>(cppOut) =
        static_cast<::Domain>(Shiboken::Enum::getValue(pyIn));

}
static PythonToCppFunc is_Domain_PythonToCpp_Domain_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX]))
        return Domain_PythonToCpp_Domain;
    return {};
}
static PyObject *Domain_CppToPython_Domain(const void *cppIn) {
    const int castCppIn = int(*reinterpret_cast<const ::Domain *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX], castCppIn);

}


static void Format_PythonToCpp_Format(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::Format *>(cppOut) =
        static_cast<::Format>(Shiboken::Enum::getValue(pyIn));

}
static PythonToCppFunc is_Format_PythonToCpp_Format_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_FORMAT_IDX]))
        return Format_PythonToCpp_Format;
    return {};
}
static PyObject *Format_CppToPython_Format(const void *cppIn) {
    const int castCppIn = int(*reinterpret_cast<const ::Format *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX], castCppIn);

}


static void PkAvg_PythonToCpp_PkAvg(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::PkAvg *>(cppOut) =
        static_cast<::PkAvg>(Shiboken::Enum::getValue(pyIn));

}
static PythonToCppFunc is_PkAvg_PythonToCpp_PkAvg_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_PKAVG_IDX]))
        return PkAvg_PythonToCpp_PkAvg;
    return {};
}
static PyObject *PkAvg_CppToPython_PkAvg(const void *cppIn) {
    const int castCppIn = int(*reinterpret_cast<const ::PkAvg *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_PKAVG_IDX], castCppIn);

}


static void Scale_PythonToCpp_Scale(PyObject *pyIn, void *cppOut) {
    *reinterpret_cast<::Scale *>(cppOut) =
        static_cast<::Scale>(Shiboken::Enum::getValue(pyIn));

}
static PythonToCppFunc is_Scale_PythonToCpp_Scale_Convertible(PyObject *pyIn) {
    if (PyObject_TypeCheck(pyIn, SbkqtpropertybrowserTypes[SBK_SCALE_IDX]))
        return Scale_PythonToCpp_Scale;
    return {};
}
static PyObject *Scale_CppToPython_Scale(const void *cppIn) {
    const int castCppIn = int(*reinterpret_cast<const ::Scale *>(cppIn));
    return Shiboken::Enum::newItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX], castCppIn);

}


// Required modules' type and converter arrays.
PyTypeObject **SbkPySide2_QtCoreTypes;
SbkConverter **SbkPySide2_QtCoreTypeConverters;
PyTypeObject **SbkPySide2_QtGuiTypes;
SbkConverter **SbkPySide2_QtGuiTypeConverters;
PyTypeObject **SbkPySide2_QtWidgetsTypes;
SbkConverter **SbkPySide2_QtWidgetsTypeConverters;

// Module initialization ------------------------------------------------------------

// Primitive Type converters.

// C++ to Python conversion for type 'QComplex'.
static PyObject *QComplex_CppToPython_QComplex(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QComplex *>(const_cast<void *>(cppIn));

                    return PyComplex_FromDoubles(cppInRef.real(), cppInRef.imag());

}
// Python to C++ conversions for type 'QComplex'.
static void PyComplex_PythonToCpp_QComplex(PyObject *pyIn, void *cppOut) {

    double real = PyComplex_RealAsDouble(pyIn);
    double imag = PyComplex_ImagAsDouble(pyIn);
    *reinterpret_cast<::QComplex *>(cppOut) = QComplex(real, imag);

}
static PythonToCppFunc is_PyComplex_PythonToCpp_QComplex_Convertible(PyObject *pyIn) {
    if (PyComplex_Check(pyIn))
        return PyComplex_PythonToCpp_QComplex;
    return {};
}


// Container Type converters.

// C++ to Python conversion for type 'const QList<QObject* > &'.
static PyObject *_constQList_QObjectPTR_REF_CppToPython__constQList_QObjectPTR_REF(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QObject* > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QObject* >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QObject* cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _constQList_QObjectPTR_REF_PythonToCpp__constQList_QObjectPTR_REF(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QObject* > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QObject* cppItem{nullptr};
        Shiboken::Conversions::pythonToCppPointer(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]), pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__constQList_QObjectPTR_REF_PythonToCpp__constQList_QObjectPTR_REF_Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::checkSequenceTypes(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX], pyIn))
        return _constQList_QObjectPTR_REF_PythonToCpp__constQList_QObjectPTR_REF;
    return {};
}

// C++ to Python conversion for type 'QList<QByteArray >'.
static PyObject *_QList_QByteArray__CppToPython__QList_QByteArray_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QByteArray > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QByteArray >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QByteArray cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QBYTEARRAY_IDX]), &cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_QByteArray__PythonToCpp__QList_QByteArray_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QByteArray > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QByteArray cppItem;
        Shiboken::Conversions::pythonToCppCopy(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QBYTEARRAY_IDX]), pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_QByteArray__PythonToCpp__QList_QByteArray__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleSequenceTypes(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QBYTEARRAY_IDX]), pyIn))
        return _QList_QByteArray__PythonToCpp__QList_QByteArray_;
    return {};
}

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

// C++ to Python conversion for type 'QList<QtBrowserItem* >'.
static PyObject *_QList_QtBrowserItemPTR__CppToPython__QList_QtBrowserItemPTR_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QtBrowserItem* > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QtBrowserItem* >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QtBrowserItem* cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QtBrowserItem* > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QtBrowserItem* cppItem{nullptr};
        Shiboken::Conversions::pythonToCppPointer(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::checkSequenceTypes(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX], pyIn))
        return _QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR_;
    return {};
}

// C++ to Python conversion for type 'QList<QtProperty* >'.
static PyObject *_QList_QtPropertyPTR__CppToPython__QList_QtPropertyPTR_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<QtProperty* > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<QtProperty* >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QtProperty* cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<QtProperty* > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QtProperty* cppItem{nullptr};
        Shiboken::Conversions::pythonToCppPointer(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::checkSequenceTypes(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyIn))
        return _QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR_;
    return {};
}

// C++ to Python conversion for type 'QSet<QtProperty* >'.
static PyObject *_QSet_QtPropertyPTR__CppToPython__QSet_QtPropertyPTR_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QSet<QtProperty* > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QSet<QtProperty* >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::QtProperty* cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QSet<QtProperty* > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::QtProperty* cppItem{nullptr};
        Shiboken::Conversions::pythonToCppPointer(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::checkSequenceTypes(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX], pyIn))
        return _QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR_;
    return {};
}

// C++ to Python conversion for type 'QList<BrowserCol >'.
static PyObject *_QList_BrowserCol__CppToPython__QList_BrowserCol_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QList<BrowserCol > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cpplist_to_pylist_conversion - START
        PyObject* pyOut = PyList_New((int) cppInRef.size());
        ::QList<BrowserCol >::const_iterator it = cppInRef.begin();
        for (int idx = 0; it != cppInRef.end(); ++it, ++idx) {
            ::BrowserCol cppItem(*it);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, &cppItem));
        }
        return pyOut;
    // TEMPLATE - cpplist_to_pylist_conversion - END

}
static void _QList_BrowserCol__PythonToCpp__QList_BrowserCol_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QList<BrowserCol > *>(cppOut);

                // TEMPLATE - pyseq_to_cpplist_conversion - START
    for (int i = 0, size = PySequence_Size(pyIn); i < size; i++) {

        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, i));
        ::BrowserCol cppItem{NONE};
        Shiboken::Conversions::pythonToCppCopy(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, pyItem, &(cppItem));
        cppOutRef << cppItem;
    }
    // TEMPLATE - pyseq_to_cpplist_conversion - END

}
static PythonToCppFunc is__QList_BrowserCol__PythonToCpp__QList_BrowserCol__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleSequenceTypes(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, pyIn))
        return _QList_BrowserCol__PythonToCpp__QList_BrowserCol_;
    return {};
}

// C++ to Python conversion for type 'QMap<int,QIcon >'.
static PyObject *_QMap_int_QIcon__CppToPython__QMap_int_QIcon_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QMap<int,QIcon > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cppmap_to_pymap_conversion - START
          PyObject *pyOut = PyDict_New();
          for (::QMap<int,QIcon >::const_iterator it = cppInRef.begin(), end = cppInRef.end(); it != end; ++it) {
              int key = it.key();
              ::QIcon value = it.value();
              PyObject *pyKey = Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<int>(), &key);
              PyObject *pyValue = Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), &value);
              PyDict_SetItem(pyOut, pyKey, pyValue);
              Py_DECREF(pyKey);
              Py_DECREF(pyValue);
          }
          return pyOut;
    // TEMPLATE - cppmap_to_pymap_conversion - END

}
static void _QMap_int_QIcon__PythonToCpp__QMap_int_QIcon_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QMap<int,QIcon > *>(cppOut);

                // TEMPLATE - pydict_to_cppmap_conversion - START
      PyObject *key;
      PyObject *value;
      Py_ssize_t pos = 0;
      while (PyDict_Next(pyIn, &pos, &key, &value)) {
          int cppKey;
        Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<int>(), key, &(cppKey));
          ::QIcon cppValue;
        Shiboken::Conversions::pythonToCppCopy(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QICON_IDX]), value, &(cppValue));
          cppOutRef.insert(cppKey, cppValue);
      }
    // TEMPLATE - pydict_to_cppmap_conversion - END

}
static PythonToCppFunc is__QMap_int_QIcon__PythonToCpp__QMap_int_QIcon__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleDictTypes(Shiboken::Conversions::PrimitiveTypeConverter<int>(), false, *PepType_SGTP(SbkPySide2_QtGuiTypes[SBK_QICON_IDX])->converter, false, pyIn))
        return _QMap_int_QIcon__PythonToCpp__QMap_int_QIcon_;
    return {};
}

// C++ to Python conversion for type 'QVector<double >'.
static PyObject *_QVector_double__CppToPython__QVector_double_(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QVector<double > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cppvector_to_pylist_conversion - START
        ::QVector<double >::size_type vectorSize = cppInRef.size();
        PyObject* pyOut = PyList_New((int) vectorSize);
        for (::QVector<double >::size_type idx = 0; idx < vectorSize; ++idx) {
            double cppItem(cppInRef[idx]);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<double>(), &cppItem));
        }
        return pyOut;
    // TEMPLATE - cppvector_to_pylist_conversion - END

}
static void _QVector_double__PythonToCpp__QVector_double_(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QVector<double > *>(cppOut);

                // TEMPLATE - pyseq_to_cppvector_conversion - START
    int vectorSize = PySequence_Size(pyIn);
    cppOutRef.reserve(vectorSize);
    for (int idx = 0; idx < vectorSize; ++idx) {
        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, idx));
        double cppItem;
        Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<double>(), pyItem, &(cppItem));
        cppOutRef.push_back(cppItem);
    }
    // TEMPLATE - pyseq_to_cppvector_conversion - END

}
static PythonToCppFunc is__QVector_double__PythonToCpp__QVector_double__Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleSequenceTypes(Shiboken::Conversions::PrimitiveTypeConverter<double>(), pyIn))
        return _QVector_double__PythonToCpp__QVector_double_;
    return {};
}

// C++ to Python conversion for type 'const QVector<QComplex > &'.
static PyObject *_constQVector_QComplex_REF_CppToPython__constQVector_QComplex_REF(const void *cppIn) {
    auto &cppInRef = *reinterpret_cast<::QVector<QComplex > *>(const_cast<void *>(cppIn));

                // TEMPLATE - cppvector_to_pylist_conversion - START
        ::QVector<QComplex >::size_type vectorSize = cppInRef.size();
        PyObject* pyOut = PyList_New((int) vectorSize);
        for (::QVector<QComplex >::size_type idx = 0; idx < vectorSize; ++idx) {
            ::QComplex cppItem(cppInRef[idx]);
            PyList_SET_ITEM(pyOut, idx, Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QCOMPLEX_IDX], &cppItem));
        }
        return pyOut;
    // TEMPLATE - cppvector_to_pylist_conversion - END

}
static void _constQVector_QComplex_REF_PythonToCpp__constQVector_QComplex_REF(PyObject *pyIn, void *cppOut) {
    auto &cppOutRef = *reinterpret_cast<::QVector<QComplex > *>(cppOut);

                // TEMPLATE - pyseq_to_cppvector_conversion - START
    int vectorSize = PySequence_Size(pyIn);
    cppOutRef.reserve(vectorSize);
    for (int idx = 0; idx < vectorSize; ++idx) {
        Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyIn, idx));
        ::QComplex cppItem;
        Shiboken::Conversions::pythonToCppCopy(SbkqtpropertybrowserTypeConverters[SBK_QCOMPLEX_IDX], pyItem, &(cppItem));
        cppOutRef.push_back(cppItem);
    }
    // TEMPLATE - pyseq_to_cppvector_conversion - END

}
static PythonToCppFunc is__constQVector_QComplex_REF_PythonToCpp__constQVector_QComplex_REF_Convertible(PyObject *pyIn) {
    if (Shiboken::Conversions::convertibleSequenceTypes(SbkqtpropertybrowserTypeConverters[SBK_QCOMPLEX_IDX], pyIn))
        return _constQVector_QComplex_REF_PythonToCpp__constQVector_QComplex_REF;
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
    /* m_name     */ "qtpropertybrowser",
    /* m_doc      */ nullptr,
    /* m_size     */ -1,
    /* m_methods  */ qtpropertybrowser_methods,
    /* m_reload   */ nullptr,
    /* m_traverse */ nullptr,
    /* m_clear    */ nullptr,
    /* m_free     */ nullptr
};

#endif

// The signatures string for the global functions.
// Multiple signatures have their index "n:" in front.
static const char *qtpropertybrowser_SignatureStrings[] = {
    nullptr}; // Sentinel

SBK_MODULE_INIT_FUNCTION_BEGIN(qtpropertybrowser)
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
    static PyTypeObject *cppApi[SBK_qtpropertybrowser_IDX_COUNT];
    SbkqtpropertybrowserTypes = cppApi;

    // Create an array of primitive type converters for the current module.
    static SbkConverter *sbkConverters[SBK_qtpropertybrowser_CONVERTERS_IDX_COUNT];
    SbkqtpropertybrowserTypeConverters = sbkConverters;

#ifdef IS_PY3K
    PyObject *module = Shiboken::Module::create("qtpropertybrowser", &moduledef);
#else
    PyObject *module = Shiboken::Module::create("qtpropertybrowser", qtpropertybrowser_methods);
#endif

    // Make module available from global scope
    SbkqtpropertybrowserModuleObject = module;

    // Initialize classes in the type system
    init_QtVariantEditorFactory(module);
    init_QtTimeEditFactory(module);
    init_QtTFTensorEditFactory(module);
    init_QtSpinBoxFactory(module);
    init_QtSliderFactory(module);
    init_QtSizePolicyEditorFactory(module);
    init_QtSizeFEditorFactory(module);
    init_QtSizeEditorFactory(module);
    init_QtScrollBarFactory(module);
    init_QtRectFEditorFactory(module);
    init_QtRectEditorFactory(module);
    init_QtProperty(module);
    init_QtVariantProperty(module);
    init_QtPointFEditorFactory(module);
    init_QtPointEditorFactory(module);
    init_QtLocaleEditorFactory(module);
    init_QtLineEditFactory(module);
    init_QtKeySequenceEditorFactory(module);
    init_QtIntEditFactory(module);
    init_QtGroupEditorFactory(module);
    init_QtFontEditorFactory(module);
    init_QtFlagEditorFactory(module);
    init_QtFileEditorFactory(module);
    init_QtEnumEditorFactory(module);
    init_QtDoubleSpinBoxFactory(module);
    init_QtDoubleEditFactory(module);
    init_QtDateTimeEditFactory(module);
    init_QtDateEditFactory(module);
    init_QtCursorEditorFactory(module);
    init_QtComplexEditFactory(module);
    init_QtColorEditorFactory(module);
    init_QtCheckBoxFactory(module);
    init_QtCharEditorFactory(module);
    init_QtBrowserItem(module);
    init_QtAbstractPropertyBrowser(module);
    init_QtGroupBoxPropertyBrowser(module);
    init_QtTreePropertyBrowser(module);
    init_QtButtonPropertyBrowser(module);
    init_QtAbstractPropertyManager(module);
    init_QtTimePropertyManager(module);
    init_QtFilePropertyManager(module);
    init_QtTFTensorPropertyManager(module);
    init_QtEnumPropertyManager(module);
    init_QtStringPropertyManager(module);
    init_QtDoublePropertyManager(module);
    init_QtSizePropertyManager(module);
    init_QtDateTimePropertyManager(module);
    init_QtSizePolicyPropertyManager(module);
    init_QtDatePropertyManager(module);
    init_QtSizeFPropertyManager(module);
    init_QtCursorPropertyManager(module);
    init_QtComplexPropertyManager(module);
    init_QtRectPropertyManager(module);
    init_QtRectFPropertyManager(module);
    init_QtColorPropertyManager(module);
    init_QtCharPropertyManager(module);
    init_QtPointPropertyManager(module);
    init_QtPointFPropertyManager(module);
    init_QtBoolPropertyManager(module);
    init_QtLocalePropertyManager(module);
    init_QtKeySequencePropertyManager(module);
    init_QtIntPropertyManager(module);
    init_QtGroupPropertyManager(module);
    init_QtVariantPropertyManager(module);
    init_QtFontPropertyManager(module);
    init_QtFlagPropertyManager(module);
    init_QtAbstractEditorFactoryBase(module);

    // Register converter for type 'qtpropertybrowser.QComplex'.
    SbkqtpropertybrowserTypeConverters[SBK_QCOMPLEX_IDX] = Shiboken::Conversions::createConverter(&PyComplex_Type, QComplex_CppToPython_QComplex);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QCOMPLEX_IDX], "QComplex");
    // Add user defined implicit conversions to type converter.
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QCOMPLEX_IDX],
        PyComplex_PythonToCpp_QComplex,
        is_PyComplex_PythonToCpp_QComplex_Convertible);


    // Register converter for type 'const QList<QObject*>&'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _constQList_QObjectPTR_REF_CppToPython__constQList_QObjectPTR_REF);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX], "const QList<QObject*>&");
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX], "QList<QObject*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX],
        _constQList_QObjectPTR_REF_PythonToCpp__constQList_QObjectPTR_REF,
        is__constQList_QObjectPTR_REF_PythonToCpp__constQList_QObjectPTR_REF_Convertible);

    // Register converter for type 'QList<QByteArray>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QByteArray__CppToPython__QList_QByteArray_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX], "QList<QByteArray>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX],
        _QList_QByteArray__PythonToCpp__QList_QByteArray_,
        is__QList_QByteArray__PythonToCpp__QList_QByteArray__Convertible);

    // Register converter for type 'QList<QAction*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QActionPTR__CppToPython__QList_QActionPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX], "QList<QAction*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX],
        _QList_QActionPTR__PythonToCpp__QList_QActionPTR_,
        is__QList_QActionPTR__PythonToCpp__QList_QActionPTR__Convertible);

    // Register converter for type 'QList<QtBrowserItem*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QtBrowserItemPTR__CppToPython__QList_QtBrowserItemPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX], "QList<QtBrowserItem*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX],
        _QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR_,
        is__QList_QtBrowserItemPTR__PythonToCpp__QList_QtBrowserItemPTR__Convertible);

    // Register converter for type 'QList<QtProperty*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QtPropertyPTR__CppToPython__QList_QtPropertyPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX], "QList<QtProperty*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX],
        _QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR_,
        is__QList_QtPropertyPTR__PythonToCpp__QList_QtPropertyPTR__Convertible);

    // Register converter for type 'QSet<QtProperty*>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX] = Shiboken::Conversions::createConverter(&PySet_Type, _QSet_QtPropertyPTR__CppToPython__QSet_QtPropertyPTR_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX], "QSet<QtProperty*>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX],
        _QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR_,
        is__QSet_QtPropertyPTR__PythonToCpp__QSet_QtPropertyPTR__Convertible);

    // Register converter for type 'QList<BrowserCol>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_BrowserCol__CppToPython__QList_BrowserCol_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX], "QList<BrowserCol>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX],
        _QList_BrowserCol__PythonToCpp__QList_BrowserCol_,
        is__QList_BrowserCol__PythonToCpp__QList_BrowserCol__Convertible);

    // Register converter for type 'QMap<int,QIcon>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX] = Shiboken::Conversions::createConverter(&PyDict_Type, _QMap_int_QIcon__CppToPython__QMap_int_QIcon_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX], "QMap<int,QIcon>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX],
        _QMap_int_QIcon__PythonToCpp__QMap_int_QIcon_,
        is__QMap_int_QIcon__PythonToCpp__QMap_int_QIcon__Convertible);

    // Register converter for type 'QVector<double>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_DOUBLE_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QVector_double__CppToPython__QVector_double_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_DOUBLE_IDX], "QVector<double>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_DOUBLE_IDX],
        _QVector_double__PythonToCpp__QVector_double_,
        is__QVector_double__PythonToCpp__QVector_double__Convertible);

    // Register converter for type 'const QVector<QComplex>&'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_QCOMPLEX_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _constQVector_QComplex_REF_CppToPython__constQVector_QComplex_REF);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_QCOMPLEX_IDX], "const QVector<QComplex>&");
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_QCOMPLEX_IDX], "QVector<QComplex>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QVECTOR_QCOMPLEX_IDX],
        _constQVector_QComplex_REF_PythonToCpp__constQVector_QComplex_REF,
        is__constQVector_QComplex_REF_PythonToCpp__constQVector_QComplex_REF_Convertible);

    // Register converter for type 'QList<QVariant>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QVariant__CppToPython__QList_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX], "QList<QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX],
        _QList_QVariant__PythonToCpp__QList_QVariant_,
        is__QList_QVariant__PythonToCpp__QList_QVariant__Convertible);

    // Register converter for type 'QList<QString>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX] = Shiboken::Conversions::createConverter(&PyList_Type, _QList_QString__CppToPython__QList_QString_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX], "QList<QString>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX],
        _QList_QString__PythonToCpp__QList_QString_,
        is__QList_QString__PythonToCpp__QList_QString__Convertible);

    // Register converter for type 'QMap<QString,QVariant>'.
    SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX] = Shiboken::Conversions::createConverter(&PyDict_Type, _QMap_QString_QVariant__CppToPython__QMap_QString_QVariant_);
    Shiboken::Conversions::registerConverterName(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX], "QMap<QString,QVariant>");
    Shiboken::Conversions::addPythonToCppValueConversion(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX],
        _QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant_,
        is__QMap_QString_QVariant__PythonToCpp__QMap_QString_QVariant__Convertible);

    // Initialization of enums.

    // Initialization of enum 'BrowserCol'.
    SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX] = Shiboken::Enum::createGlobalEnum(module,
        "BrowserCol",
        "qtpropertybrowser.BrowserCol",
        "BrowserCol");
    if (!SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])
        return SBK_MODULE_INIT_ERROR;

    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "NONE", (long) BrowserCol::NONE))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "UNIT", (long) BrowserCol::UNIT))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "PKAVG", (long) BrowserCol::PKAVG))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "FORMAT", (long) BrowserCol::FORMAT))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "MINIMUM", (long) BrowserCol::MINIMUM))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "MAXIMUM", (long) BrowserCol::MAXIMUM))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
        module, "CHECK", (long) BrowserCol::CHECK))
        return SBK_MODULE_INIT_ERROR;
    // Register converter for enum 'BrowserCol'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX],
            BrowserCol_CppToPython_BrowserCol);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            BrowserCol_PythonToCpp_BrowserCol,
            is_BrowserCol_PythonToCpp_BrowserCol_Convertible);
        Shiboken::Enum::setTypeConverter(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX], converter);
        Shiboken::Conversions::registerConverterName(converter, "BrowserCol");
    }
    // End of 'BrowserCol' enum.

    // Initialization of enum 'Domain'.
    SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX] = Shiboken::Enum::createGlobalEnum(module,
        "Domain",
        "qtpropertybrowser.Domain",
        "Domain");
    if (!SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX])
        return SBK_MODULE_INIT_ERROR;

    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX],
        module, "TF", (long) Domain::TF))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX],
        module, "FF", (long) Domain::FF))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX],
        module, "FT", (long) Domain::FT))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX],
        module, "TT", (long) Domain::TT))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX],
        module, "TH", (long) Domain::TH))
        return SBK_MODULE_INIT_ERROR;
    // Register converter for enum 'Domain'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX],
            Domain_CppToPython_Domain);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            Domain_PythonToCpp_Domain,
            is_Domain_PythonToCpp_Domain_Convertible);
        Shiboken::Enum::setTypeConverter(SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX], converter);
        Shiboken::Conversions::registerConverterName(converter, "Domain");
    }
    // End of 'Domain' enum.

    // Initialization of enum 'Format'.
    SbkqtpropertybrowserTypes[SBK_FORMAT_IDX] = Shiboken::Enum::createGlobalEnum(module,
        "Format",
        "qtpropertybrowser.Format",
        "Format");
    if (!SbkqtpropertybrowserTypes[SBK_FORMAT_IDX])
        return SBK_MODULE_INIT_ERROR;

    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX],
        module, "RE", (long) Format::RE))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX],
        module, "RE_IM", (long) Format::RE_IM))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX],
        module, "LIN_DEG", (long) Format::LIN_DEG))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX],
        module, "LOG_DEG", (long) Format::LOG_DEG))
        return SBK_MODULE_INIT_ERROR;
    // Register converter for enum 'Format'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX],
            Format_CppToPython_Format);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            Format_PythonToCpp_Format,
            is_Format_PythonToCpp_Format_Convertible);
        Shiboken::Enum::setTypeConverter(SbkqtpropertybrowserTypes[SBK_FORMAT_IDX], converter);
        Shiboken::Conversions::registerConverterName(converter, "Format");
    }
    // End of 'Format' enum.

    // Initialization of enum 'PkAvg'.
    SbkqtpropertybrowserTypes[SBK_PKAVG_IDX] = Shiboken::Enum::createGlobalEnum(module,
        "PkAvg",
        "qtpropertybrowser.PkAvg",
        "PkAvg");
    if (!SbkqtpropertybrowserTypes[SBK_PKAVG_IDX])
        return SBK_MODULE_INIT_ERROR;

    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_PKAVG_IDX],
        module, "PK", (long) PkAvg::PK))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_PKAVG_IDX],
        module, "AVG", (long) PkAvg::AVG))
        return SBK_MODULE_INIT_ERROR;
    // Register converter for enum 'PkAvg'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(SbkqtpropertybrowserTypes[SBK_PKAVG_IDX],
            PkAvg_CppToPython_PkAvg);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            PkAvg_PythonToCpp_PkAvg,
            is_PkAvg_PythonToCpp_PkAvg_Convertible);
        Shiboken::Enum::setTypeConverter(SbkqtpropertybrowserTypes[SBK_PKAVG_IDX], converter);
        Shiboken::Conversions::registerConverterName(converter, "PkAvg");
    }
    // End of 'PkAvg' enum.

    // Initialization of enum 'Scale'.
    SbkqtpropertybrowserTypes[SBK_SCALE_IDX] = Shiboken::Enum::createGlobalEnum(module,
        "Scale",
        "qtpropertybrowser.Scale",
        "Scale");
    if (!SbkqtpropertybrowserTypes[SBK_SCALE_IDX])
        return SBK_MODULE_INIT_ERROR;

    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "T", (long) Scale::T))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "G", (long) Scale::G))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "M", (long) Scale::M))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "K", (long) Scale::K))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "_", (long) Scale::_))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "m", (long) Scale::m))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "u", (long) Scale::u))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "n", (long) Scale::n))
        return SBK_MODULE_INIT_ERROR;
    if (!Shiboken::Enum::createGlobalEnumItem(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
        module, "p", (long) Scale::p))
        return SBK_MODULE_INIT_ERROR;
    // Register converter for enum 'Scale'.
    {
        SbkConverter *converter = Shiboken::Conversions::createConverter(SbkqtpropertybrowserTypes[SBK_SCALE_IDX],
            Scale_CppToPython_Scale);
        Shiboken::Conversions::addPythonToCppValueConversion(converter,
            Scale_PythonToCpp_Scale,
            is_Scale_PythonToCpp_Scale_Convertible);
        Shiboken::Enum::setTypeConverter(SbkqtpropertybrowserTypes[SBK_SCALE_IDX], converter);
        Shiboken::Conversions::registerConverterName(converter, "Scale");
    }
    // End of 'Scale' enum.

    // Register primitive types converters.

    Shiboken::Module::registerTypes(module, SbkqtpropertybrowserTypes);
    Shiboken::Module::registerTypeConverters(module, SbkqtpropertybrowserTypeConverters);

    if (PyErr_Occurred()) {
        PyErr_Print();
        Py_FatalError("can't initialize module qtpropertybrowser");
    }
    qRegisterMetaType< ::BrowserCol >("BrowserCol");
    qRegisterMetaType< ::Domain >("Domain");
    qRegisterMetaType< ::Format >("Format");
    qRegisterMetaType< ::PkAvg >("PkAvg");
    qRegisterMetaType< ::Scale >("Scale");
    PySide::registerCleanupFunction(cleanTypesAttributes);

    FinishSignatureInitialization(module, qtpropertybrowser_SignatureStrings);
    NotifyModuleForQApp(module, qApp);

SBK_MODULE_INIT_FUNCTION_END
