

#ifndef SBK_QTPROPERTYBROWSER_PYTHON_H
#define SBK_QTPROPERTYBROWSER_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside2_qtcore_python.h>
#include <pyside2_qtgui_python.h>
#include <pyside2_qtwidgets_python.h>

// Binded library includes
#include <qtbuttonpropertybrowser.h>
#include <qtpropertybrowserutils_p.h>
#include <qtvariantproperty.h>
#include <qtgroupboxpropertybrowser.h>
#include <qtpropertymanager.h>
#include <qttreepropertybrowser.h>
#include <qteditorfactory.h>
#include <qtpropertybrowser.h>
// Conversion Includes - Primitive Types
#include <complex>
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
    SBK_QTABSTRACTEDITORFACTORYBASE_IDX                      = 4,
    SBK_QTABSTRACTPROPERTYBROWSER_IDX                        = 5,
    SBK_QTABSTRACTPROPERTYMANAGER_IDX                        = 6,
    SBK_QTBOOLPROPERTYMANAGER_IDX                            = 7,
    SBK_QTBROWSERITEM_IDX                                    = 8,
    SBK_QTBUTTONPROPERTYBROWSER_IDX                          = 9,
    SBK_QTCHAREDITORFACTORY_IDX                              = 10,
    SBK_QTCHARPROPERTYMANAGER_IDX                            = 11,
    SBK_QTCHECKBOXFACTORY_IDX                                = 12,
    SBK_QTCOLOREDITORFACTORY_IDX                             = 13,
    SBK_QTCOLORPROPERTYMANAGER_IDX                           = 14,
    SBK_QTCOMPLEXEDITFACTORY_IDX                             = 15,
    SBK_QTCOMPLEXPROPERTYMANAGER_IDX                         = 16,
    SBK_QTCURSOREDITORFACTORY_IDX                            = 17,
    SBK_QTCURSORPROPERTYMANAGER_IDX                          = 18,
    SBK_QTDATEEDITFACTORY_IDX                                = 19,
    SBK_QTDATEPROPERTYMANAGER_IDX                            = 20,
    SBK_QTDATETIMEEDITFACTORY_IDX                            = 21,
    SBK_QTDATETIMEPROPERTYMANAGER_IDX                        = 22,
    SBK_QTDOUBLEEDITFACTORY_IDX                              = 23,
    SBK_QTDOUBLEPROPERTYMANAGER_IDX                          = 24,
    SBK_QTDOUBLESPINBOXFACTORY_IDX                           = 25,
    SBK_QTENUMEDITORFACTORY_IDX                              = 26,
    SBK_QTENUMPROPERTYMANAGER_IDX                            = 27,
    SBK_QTFILEEDITORFACTORY_IDX                              = 28,
    SBK_QTFILEPROPERTYMANAGER_IDX                            = 29,
    SBK_QTFLAGEDITORFACTORY_IDX                              = 30,
    SBK_QTFLAGPROPERTYMANAGER_IDX                            = 31,
    SBK_QTFONTEDITORFACTORY_IDX                              = 32,
    SBK_QTFONTPROPERTYMANAGER_IDX                            = 33,
    SBK_QTGROUPBOXPROPERTYBROWSER_IDX                        = 34,
    SBK_QTGROUPEDITORFACTORY_IDX                             = 35,
    SBK_QTGROUPPROPERTYMANAGER_IDX                           = 36,
    SBK_QTINTEDITFACTORY_IDX                                 = 37,
    SBK_QTINTPROPERTYMANAGER_IDX                             = 38,
    SBK_QTKEYSEQUENCEEDITORFACTORY_IDX                       = 39,
    SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX                     = 40,
    SBK_QTLINEEDITFACTORY_IDX                                = 41,
    SBK_QTLOCALEEDITORFACTORY_IDX                            = 42,
    SBK_QTLOCALEPROPERTYMANAGER_IDX                          = 43,
    SBK_QTPOINTEDITORFACTORY_IDX                             = 44,
    SBK_QTPOINTFEDITORFACTORY_IDX                            = 45,
    SBK_QTPOINTFPROPERTYMANAGER_IDX                          = 46,
    SBK_QTPOINTPROPERTYMANAGER_IDX                           = 47,
    SBK_QTPROPERTY_IDX                                       = 48,
    SBK_QTRECTEDITORFACTORY_IDX                              = 49,
    SBK_QTRECTFEDITORFACTORY_IDX                             = 50,
    SBK_QTRECTFPROPERTYMANAGER_IDX                           = 51,
    SBK_QTRECTPROPERTYMANAGER_IDX                            = 52,
    SBK_QTSCROLLBARFACTORY_IDX                               = 53,
    SBK_QTSIZEEDITORFACTORY_IDX                              = 54,
    SBK_QTSIZEFEDITORFACTORY_IDX                             = 55,
    SBK_QTSIZEFPROPERTYMANAGER_IDX                           = 56,
    SBK_QTSIZEPOLICYEDITORFACTORY_IDX                        = 57,
    SBK_QTSIZEPOLICYPROPERTYMANAGER_IDX                      = 58,
    SBK_QTSIZEPROPERTYMANAGER_IDX                            = 59,
    SBK_QTSLIDERFACTORY_IDX                                  = 60,
    SBK_QTSPINBOXFACTORY_IDX                                 = 61,
    SBK_QTSTRINGPROPERTYMANAGER_IDX                          = 62,
    SBK_QTTFTENSOREDITFACTORY_IDX                            = 63,
    SBK_QTTFTENSORPROPERTYMANAGER_IDX                        = 64,
    SBK_QTTIMEEDITFACTORY_IDX                                = 65,
    SBK_QTTIMEPROPERTYMANAGER_IDX                            = 66,
    SBK_QTTREEPROPERTYBROWSER_IDX                            = 67,
    SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX                 = 68,
    SBK_QTVARIANTEDITORFACTORY_IDX                           = 69,
    SBK_QTVARIANTPROPERTY_IDX                                = 70,
    SBK_QTVARIANTPROPERTYMANAGER_IDX                         = 71,
    SBK_BROWSERCOL_IDX                                       = 0,
    SBK_DOMAIN_IDX                                           = 1,
    SBK_FORMAT_IDX                                           = 2,
    SBK_PKAVG_IDX                                            = 3,
    SBK_SCALE_IDX                                            = 72,
    SBK_qtpropertybrowser_IDX_COUNT                          = 73
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkqtpropertybrowserTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkqtpropertybrowserModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkqtpropertybrowserTypeConverters;

// Converter indices
enum : int {
    SBK_QCOMPLEX_IDX                                         = 0,
    SBK_QTPROPERTYBROWSER_QLIST_QOBJECTPTR_IDX               = 1, // const QList<QObject* > &
    SBK_QTPROPERTYBROWSER_QLIST_QBYTEARRAY_IDX               = 2, // QList<QByteArray >
    SBK_QTPROPERTYBROWSER_QLIST_QACTIONPTR_IDX               = 3, // QList<QAction* >
    SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX         = 4, // QList<QtBrowserItem* >
    SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX            = 5, // QList<QtProperty* >
    SBK_QTPROPERTYBROWSER_QSET_QTPROPERTYPTR_IDX             = 6, // QSet<QtProperty* >
    SBK_QTPROPERTYBROWSER_QLIST_BROWSERCOL_IDX               = 7, // QList<BrowserCol >
    SBK_QTPROPERTYBROWSER_QMAP_INT_QICON_IDX                 = 8, // QMap<int,QIcon >
    SBK_QTPROPERTYBROWSER_QVECTOR_DOUBLE_IDX                 = 9, // QVector<double >
    SBK_QTPROPERTYBROWSER_QVECTOR_QCOMPLEX_IDX               = 10, // const QVector<QComplex > &
    SBK_QTPROPERTYBROWSER_QLIST_QVARIANT_IDX                 = 11, // QList<QVariant >
    SBK_QTPROPERTYBROWSER_QLIST_QSTRING_IDX                  = 12, // QList<QString >
    SBK_QTPROPERTYBROWSER_QMAP_QSTRING_QVARIANT_IDX          = 13, // QMap<QString,QVariant >
    SBK_qtpropertybrowser_CONVERTERS_IDX_COUNT               = 14
};
// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject *SbkType< ::BrowserCol >() { return SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX]; }
template<> inline PyTypeObject *SbkType< ::Domain >() { return SbkqtpropertybrowserTypes[SBK_DOMAIN_IDX]; }
template<> inline PyTypeObject *SbkType< ::Format >() { return SbkqtpropertybrowserTypes[SBK_FORMAT_IDX]; }
template<> inline PyTypeObject *SbkType< ::PkAvg >() { return SbkqtpropertybrowserTypes[SBK_PKAVG_IDX]; }
template<> inline PyTypeObject *SbkType< ::Scale >() { return SbkqtpropertybrowserTypes[SBK_SCALE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QtAbstractEditorFactoryBase >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTEDITORFACTORYBASE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtAbstractPropertyBrowser >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtAbstractPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtBoolPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTBOOLPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtBrowserItem >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtButtonPropertyBrowser >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTBUTTONPROPERTYBROWSER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtCharEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCHAREDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtCharPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCHARPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtCheckBoxFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCHECKBOXFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtColorEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCOLOREDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtColorPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCOLORPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtComplexEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCOMPLEXEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtComplexPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCOMPLEXPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtCursorEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCURSOREDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtCursorPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTCURSORPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDateEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDATEEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDatePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDATEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDateTimeEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDATETIMEEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDateTimePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDATETIMEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDoubleEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDOUBLEEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDoublePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDOUBLEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtDoubleSpinBoxFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTDOUBLESPINBOXFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtEnumEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTENUMEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtEnumPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTENUMPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtFileEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTFILEEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtFilePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTFILEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtFlagEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTFLAGEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtFlagPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTFLAGPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtFontEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTFONTEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtFontPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTFONTPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtGroupBoxPropertyBrowser >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTGROUPBOXPROPERTYBROWSER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtGroupEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTGROUPEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtGroupPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTGROUPPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtIntEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTINTEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtIntPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTINTPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtKeySequenceEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtKeySequencePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtLineEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTLINEEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtLocaleEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTLOCALEEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtLocalePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTLOCALEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtPointEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTPOINTEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtPointFEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTPOINTFEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtPointFPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTPOINTFPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtPointPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTPOINTPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtProperty >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtRectEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTRECTEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtRectFEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTRECTFEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtRectFPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTRECTFPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtRectPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTRECTPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtScrollBarFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSCROLLBARFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSizeEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSIZEEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSizeFEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSIZEFEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSizeFPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSIZEFPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSizePolicyEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSIZEPOLICYEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSizePolicyPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSIZEPOLICYPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSizePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSIZEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSliderFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSLIDERFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtSpinBoxFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSPINBOXFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtStringPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTSTRINGPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtTFTensorEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTTFTENSOREDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtTFTensorPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTTFTENSORPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtTimeEditFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTTIMEEDITFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtTimePropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTTIMEPROPERTYMANAGER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtTreePropertyBrowser::ResizeMode >() { return SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_RESIZEMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QtTreePropertyBrowser >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTTREEPROPERTYBROWSER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtVariantEditorFactory >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTVARIANTEDITORFACTORY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtVariantProperty >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTY_IDX]); }
template<> inline PyTypeObject *SbkType< ::QtVariantPropertyManager >() { return reinterpret_cast<PyTypeObject *>(SbkqtpropertybrowserTypes[SBK_QTVARIANTPROPERTYMANAGER_IDX]); }

} // namespace Shiboken

#endif // SBK_QTPROPERTYBROWSER_PYTHON_H

