

#ifndef SBK_QPROGRESSINDICATOR_PYTHON_H
#define SBK_QPROGRESSINDICATOR_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside2_qtcore_python.h>
#include <pyside2_qtgui_python.h>
#include <pyside2_qtwidgets_python.h>

// Binded library includes
#include <qprogressindicator.h>
// Conversion Includes - Primitive Types
#include <qabstractitemmodel.h>
#include <QString>
#include <QStringList>
#include <signalmanager.h>

// Conversion Includes - Container Types
#include <pysideqflags.h>
#include <QLinkedList>
#include <QList>
#include <QMap>
#include <QMultiMap>
#include <QPair>
#include <QQueue>
#include <QSet>
#include <QStack>
#include <QVector>

// Type indices
enum : int {
    SBK_QPROGRESSINDICATOR_IDX                               = 0,
    SBK_qprogressindicator_IDX_COUNT                         = 1
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkqprogressindicatorTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkqprogressindicatorModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkqprogressindicatorTypeConverters;

// Converter indices
enum : int {
    SBK_QPROGRESSINDICATOR_QLIST_QACTIONPTR_IDX              = 0, // QList<QAction* >
    SBK_QPROGRESSINDICATOR_QLIST_QVARIANT_IDX                = 1, // QList<QVariant >
    SBK_QPROGRESSINDICATOR_QLIST_QSTRING_IDX                 = 2, // QList<QString >
    SBK_QPROGRESSINDICATOR_QMAP_QSTRING_QVARIANT_IDX         = 3, // QMap<QString,QVariant >
    SBK_qprogressindicator_CONVERTERS_IDX_COUNT              = 4
};
// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::QProgressIndicator >() { return reinterpret_cast<PyTypeObject *>(SbkqprogressindicatorTypes[SBK_QPROGRESSINDICATOR_IDX]); }

} // namespace Shiboken

#endif // SBK_QPROGRESSINDICATOR_PYTHON_H

