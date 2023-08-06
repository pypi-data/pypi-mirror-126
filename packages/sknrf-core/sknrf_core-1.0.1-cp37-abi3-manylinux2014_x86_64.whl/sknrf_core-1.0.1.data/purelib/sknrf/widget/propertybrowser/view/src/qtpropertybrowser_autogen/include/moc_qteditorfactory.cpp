/****************************************************************************
** Meta object code from reading C++ file 'qteditorfactory.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.13.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../../../../../../../../sknrf/widget/propertybrowser/view/src/qteditorfactory.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#include <QtCore/QVector>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qteditorfactory.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.13.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_QtGroupEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[69];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtGroupEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtGroupEditorFactory_t qt_meta_stringdata_QtGroupEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 20), // "QtGroupEditorFactory"
QT_MOC_LITERAL(1, 21, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 34, 0), // ""
QT_MOC_LITERAL(3, 35, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtGroupEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtGroupEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtGroupEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtGroupEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtGroupEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtGroupPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtGroupEditorFactory.data,
    qt_meta_data_QtGroupEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtGroupEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtGroupEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtGroupEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtGroupPropertyManager>::qt_metacast(_clname);
}

int QtGroupEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtGroupPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtSpinBoxFactory_t {
    QByteArrayData data[15];
    char stringdata0[291];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtSpinBoxFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtSpinBoxFactory_t qt_meta_stringdata_QtSpinBoxFactory = {
    {
QT_MOC_LITERAL(0, 0, 16), // "QtSpinBoxFactory"
QT_MOC_LITERAL(1, 17, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 37, 0), // ""
QT_MOC_LITERAL(3, 38, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 50, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 67, 21), // "slotSingleStepChanged"
QT_MOC_LITERAL(6, 89, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(7, 109, 12), // "slotSetValue"
QT_MOC_LITERAL(8, 122, 14), // "slotSetMinimum"
QT_MOC_LITERAL(9, 137, 14), // "slotSetMaximum"
QT_MOC_LITERAL(10, 152, 12), // "slotSetCheck"
QT_MOC_LITERAL(11, 165, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(12, 185, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(13, 221, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(14, 257, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtSpinBoxFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotSingleStepChanged\0slotReadOnlyChanged\0"
    "slotSetValue\0slotSetMinimum\0slotSetMaximum\0"
    "slotSetCheck\0slotEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtSpinBoxFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      14,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   84,    2, 0x08 /* Private */,
       4,    3,   89,    2, 0x08 /* Private */,
       5,    2,   96,    2, 0x08 /* Private */,
       6,    2,  101,    2, 0x08 /* Private */,
       7,    1,  106,    2, 0x08 /* Private */,
       8,    1,  109,    2, 0x08 /* Private */,
       9,    1,  112,    2, 0x08 /* Private */,
       8,    1,  115,    2, 0x08 /* Private */,
       9,    1,  118,    2, 0x08 /* Private */,
      10,    1,  121,    2, 0x08 /* Private */,
      11,    1,  124,    2, 0x08 /* Private */,
      12,    1,  127,    2, 0x08 /* Private */,
      13,    1,  130,    2, 0x08 /* Private */,
      14,    1,  133,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int, QMetaType::Int,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtSpinBoxFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtSpinBoxFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotSingleStepChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 4: _t->d_func()->slotSetValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotSetMinimum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetMaximum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 13: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtSpinBoxFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtIntPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtSpinBoxFactory.data,
    qt_meta_data_QtSpinBoxFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtSpinBoxFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtSpinBoxFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtSpinBoxFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacast(_clname);
}

int QtSpinBoxFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 14)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 14;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 14)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 14;
    }
    return _id;
}
struct qt_meta_stringdata_QtIntEditFactory_t {
    QByteArrayData data[15];
    char stringdata0[290];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtIntEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtIntEditFactory_t qt_meta_stringdata_QtIntEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 16), // "QtIntEditFactory"
QT_MOC_LITERAL(1, 17, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 37, 0), // ""
QT_MOC_LITERAL(3, 38, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 50, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 67, 20), // "slotPrecisionChanged"
QT_MOC_LITERAL(6, 88, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(7, 108, 12), // "slotSetValue"
QT_MOC_LITERAL(8, 121, 14), // "slotSetMinimum"
QT_MOC_LITERAL(9, 136, 14), // "slotSetMaximum"
QT_MOC_LITERAL(10, 151, 12), // "slotSetCheck"
QT_MOC_LITERAL(11, 164, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(12, 184, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(13, 220, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(14, 256, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtIntEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotPrecisionChanged\0slotReadOnlyChanged\0"
    "slotSetValue\0slotSetMinimum\0slotSetMaximum\0"
    "slotSetCheck\0slotEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtIntEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      15,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   89,    2, 0x08 /* Private */,
       4,    3,   94,    2, 0x08 /* Private */,
       4,    3,  101,    2, 0x08 /* Private */,
       5,    2,  108,    2, 0x08 /* Private */,
       6,    2,  113,    2, 0x08 /* Private */,
       7,    1,  118,    2, 0x08 /* Private */,
       8,    1,  121,    2, 0x08 /* Private */,
       9,    1,  124,    2, 0x08 /* Private */,
       8,    1,  127,    2, 0x08 /* Private */,
       9,    1,  130,    2, 0x08 /* Private */,
      10,    1,  133,    2, 0x08 /* Private */,
      11,    1,  136,    2, 0x08 /* Private */,
      12,    1,  139,    2, 0x08 /* Private */,
      13,    1,  142,    2, 0x08 /* Private */,
      14,    1,  145,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double, QMetaType::Double,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int, QMetaType::Int,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtIntEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtIntEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2])),(*reinterpret_cast< double(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3]))); break;
        case 3: _t->d_func()->slotPrecisionChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 4: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 5: _t->d_func()->slotSetValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetMinimum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetMaximum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 13: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 14: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtIntEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtIntPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtIntEditFactory.data,
    qt_meta_data_QtIntEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtIntEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtIntEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtIntEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacast(_clname);
}

int QtIntEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 15)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 15;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 15)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 15;
    }
    return _id;
}
struct qt_meta_stringdata_QtSliderFactory_t {
    QByteArrayData data[14];
    char stringdata0[270];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtSliderFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtSliderFactory_t qt_meta_stringdata_QtSliderFactory = {
    {
QT_MOC_LITERAL(0, 0, 15), // "QtSliderFactory"
QT_MOC_LITERAL(1, 16, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 36, 0), // ""
QT_MOC_LITERAL(3, 37, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 49, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 66, 21), // "slotSingleStepChanged"
QT_MOC_LITERAL(6, 88, 12), // "slotSetValue"
QT_MOC_LITERAL(7, 101, 14), // "slotSetMinimum"
QT_MOC_LITERAL(8, 116, 14), // "slotSetMaximum"
QT_MOC_LITERAL(9, 131, 12), // "slotSetCheck"
QT_MOC_LITERAL(10, 144, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(11, 164, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(12, 200, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(13, 236, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtSliderFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotSingleStepChanged\0slotSetValue\0"
    "slotSetMinimum\0slotSetMaximum\0"
    "slotSetCheck\0slotEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtSliderFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   79,    2, 0x08 /* Private */,
       4,    3,   84,    2, 0x08 /* Private */,
       5,    2,   91,    2, 0x08 /* Private */,
       6,    1,   96,    2, 0x08 /* Private */,
       7,    1,   99,    2, 0x08 /* Private */,
       8,    1,  102,    2, 0x08 /* Private */,
       7,    1,  105,    2, 0x08 /* Private */,
       8,    1,  108,    2, 0x08 /* Private */,
       9,    1,  111,    2, 0x08 /* Private */,
      10,    1,  114,    2, 0x08 /* Private */,
      11,    1,  117,    2, 0x08 /* Private */,
      12,    1,  120,    2, 0x08 /* Private */,
      13,    1,  123,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int, QMetaType::Int,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtSliderFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtSliderFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotSingleStepChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotSetValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotSetMinimum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotSetMaximum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtSliderFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtIntPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtSliderFactory.data,
    qt_meta_data_QtSliderFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtSliderFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtSliderFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtSliderFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacast(_clname);
}

int QtSliderFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 13;
    }
    return _id;
}
struct qt_meta_stringdata_QtScrollBarFactory_t {
    QByteArrayData data[14];
    char stringdata0[273];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtScrollBarFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtScrollBarFactory_t qt_meta_stringdata_QtScrollBarFactory = {
    {
QT_MOC_LITERAL(0, 0, 18), // "QtScrollBarFactory"
QT_MOC_LITERAL(1, 19, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 39, 0), // ""
QT_MOC_LITERAL(3, 40, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 52, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 69, 21), // "slotSingleStepChanged"
QT_MOC_LITERAL(6, 91, 12), // "slotSetValue"
QT_MOC_LITERAL(7, 104, 14), // "slotSetMinimum"
QT_MOC_LITERAL(8, 119, 14), // "slotSetMaximum"
QT_MOC_LITERAL(9, 134, 12), // "slotSetCheck"
QT_MOC_LITERAL(10, 147, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(11, 167, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(12, 203, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(13, 239, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtScrollBarFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotSingleStepChanged\0slotSetValue\0"
    "slotSetMinimum\0slotSetMaximum\0"
    "slotSetCheck\0slotEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtScrollBarFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   79,    2, 0x08 /* Private */,
       4,    3,   84,    2, 0x08 /* Private */,
       5,    2,   91,    2, 0x08 /* Private */,
       6,    1,   96,    2, 0x08 /* Private */,
       7,    1,   99,    2, 0x08 /* Private */,
       8,    1,  102,    2, 0x08 /* Private */,
       7,    1,  105,    2, 0x08 /* Private */,
       8,    1,  108,    2, 0x08 /* Private */,
       9,    1,  111,    2, 0x08 /* Private */,
      10,    1,  114,    2, 0x08 /* Private */,
      11,    1,  117,    2, 0x08 /* Private */,
      12,    1,  120,    2, 0x08 /* Private */,
      13,    1,  123,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int, QMetaType::Int,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtScrollBarFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtScrollBarFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2])),(*reinterpret_cast< int(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotSingleStepChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotSetValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotSetMinimum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotSetMaximum((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtScrollBarFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtIntPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtScrollBarFactory.data,
    qt_meta_data_QtScrollBarFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtScrollBarFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtScrollBarFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtScrollBarFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacast(_clname);
}

int QtScrollBarFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtIntPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 13;
    }
    return _id;
}
struct qt_meta_stringdata_QtCheckBoxFactory_t {
    QByteArrayData data[9];
    char stringdata0[154];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtCheckBoxFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtCheckBoxFactory_t qt_meta_stringdata_QtCheckBoxFactory = {
    {
QT_MOC_LITERAL(0, 0, 17), // "QtCheckBoxFactory"
QT_MOC_LITERAL(1, 18, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 38, 0), // ""
QT_MOC_LITERAL(3, 39, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 51, 22), // "slotTextVisibleChanged"
QT_MOC_LITERAL(5, 74, 12), // "slotSetValue"
QT_MOC_LITERAL(6, 87, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(7, 107, 12), // "slotSetCheck"
QT_MOC_LITERAL(8, 120, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtCheckBoxFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotTextVisibleChanged\0"
    "slotSetValue\0slotEditorDestroyed\0"
    "slotSetCheck\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtCheckBoxFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   44,    2, 0x08 /* Private */,
       4,    2,   49,    2, 0x08 /* Private */,
       5,    1,   54,    2, 0x08 /* Private */,
       6,    1,   57,    2, 0x08 /* Private */,
       7,    1,   60,    2, 0x08 /* Private */,
       8,    1,   63,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtCheckBoxFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtCheckBoxFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotTextVisibleChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 2: _t->d_func()->slotSetValue((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtCheckBoxFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtBoolPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtCheckBoxFactory.data,
    qt_meta_data_QtCheckBoxFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtCheckBoxFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtCheckBoxFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtCheckBoxFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtBoolPropertyManager>::qt_metacast(_clname);
}

int QtCheckBoxFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtBoolPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}
struct qt_meta_stringdata_QtDoubleSpinBoxFactory_t {
    QByteArrayData data[16];
    char stringdata0[318];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtDoubleSpinBoxFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtDoubleSpinBoxFactory_t qt_meta_stringdata_QtDoubleSpinBoxFactory = {
    {
QT_MOC_LITERAL(0, 0, 22), // "QtDoubleSpinBoxFactory"
QT_MOC_LITERAL(1, 23, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 43, 0), // ""
QT_MOC_LITERAL(3, 44, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 56, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 73, 21), // "slotSingleStepChanged"
QT_MOC_LITERAL(6, 95, 20), // "slotPrecisionChanged"
QT_MOC_LITERAL(7, 116, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(8, 136, 12), // "slotSetValue"
QT_MOC_LITERAL(9, 149, 14), // "slotSetMinimum"
QT_MOC_LITERAL(10, 164, 14), // "slotSetMaximum"
QT_MOC_LITERAL(11, 179, 12), // "slotSetCheck"
QT_MOC_LITERAL(12, 192, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(13, 212, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(14, 248, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(15, 284, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtDoubleSpinBoxFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotSingleStepChanged\0slotPrecisionChanged\0"
    "slotReadOnlyChanged\0slotSetValue\0"
    "slotSetMinimum\0slotSetMaximum\0"
    "slotSetCheck\0slotEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtDoubleSpinBoxFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      13,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   79,    2, 0x08 /* Private */,
       4,    3,   84,    2, 0x08 /* Private */,
       5,    2,   91,    2, 0x08 /* Private */,
       6,    2,   96,    2, 0x08 /* Private */,
       7,    2,  101,    2, 0x08 /* Private */,
       8,    1,  106,    2, 0x08 /* Private */,
       9,    1,  109,    2, 0x08 /* Private */,
      10,    1,  112,    2, 0x08 /* Private */,
      11,    1,  115,    2, 0x08 /* Private */,
      12,    1,  118,    2, 0x08 /* Private */,
      13,    1,  121,    2, 0x08 /* Private */,
      14,    1,  124,    2, 0x08 /* Private */,
      15,    1,  127,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double, QMetaType::Double,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtDoubleSpinBoxFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtDoubleSpinBoxFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2])),(*reinterpret_cast< double(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotSingleStepChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotPrecisionChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 4: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 5: _t->d_func()->slotSetValue((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtDoubleSpinBoxFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtDoublePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtDoubleSpinBoxFactory.data,
    qt_meta_data_QtDoubleSpinBoxFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtDoubleSpinBoxFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtDoubleSpinBoxFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtDoubleSpinBoxFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtDoublePropertyManager>::qt_metacast(_clname);
}

int QtDoubleSpinBoxFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtDoublePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 13)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 13;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 13)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 13;
    }
    return _id;
}
struct qt_meta_stringdata_QtDoubleEditFactory_t {
    QByteArrayData data[19];
    char stringdata0[388];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtDoubleEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtDoubleEditFactory_t qt_meta_stringdata_QtDoubleEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtDoubleEditFactory"
QT_MOC_LITERAL(1, 20, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 53, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 70, 20), // "slotPrecisionChanged"
QT_MOC_LITERAL(6, 91, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(7, 111, 12), // "slotSetValue"
QT_MOC_LITERAL(8, 124, 12), // "slotSetScale"
QT_MOC_LITERAL(9, 137, 13), // "slotSetFormat"
QT_MOC_LITERAL(10, 151, 14), // "slotSetMinimum"
QT_MOC_LITERAL(11, 166, 14), // "slotSetMaximum"
QT_MOC_LITERAL(12, 181, 12), // "slotSetCheck"
QT_MOC_LITERAL(13, 194, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(14, 214, 32), // "slotUnitAttributeEditorDestroyed"
QT_MOC_LITERAL(15, 247, 34), // "slotFormatAttributeEditorDest..."
QT_MOC_LITERAL(16, 282, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(17, 318, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(18, 354, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtDoubleEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotPrecisionChanged\0slotReadOnlyChanged\0"
    "slotSetValue\0slotSetScale\0slotSetFormat\0"
    "slotSetMinimum\0slotSetMaximum\0"
    "slotSetCheck\0slotEditorDestroyed\0"
    "slotUnitAttributeEditorDestroyed\0"
    "slotFormatAttributeEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtDoubleEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      16,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   94,    2, 0x08 /* Private */,
       4,    3,   99,    2, 0x08 /* Private */,
       5,    2,  106,    2, 0x08 /* Private */,
       6,    2,  111,    2, 0x08 /* Private */,
       7,    1,  116,    2, 0x08 /* Private */,
       8,    1,  119,    2, 0x08 /* Private */,
       9,    1,  122,    2, 0x08 /* Private */,
      10,    1,  125,    2, 0x08 /* Private */,
      11,    1,  128,    2, 0x08 /* Private */,
      12,    1,  131,    2, 0x08 /* Private */,
      13,    1,  134,    2, 0x08 /* Private */,
      14,    1,  137,    2, 0x08 /* Private */,
      15,    1,  140,    2, 0x08 /* Private */,
      16,    1,  143,    2, 0x08 /* Private */,
      17,    1,  146,    2, 0x08 /* Private */,
      18,    1,  149,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double, QMetaType::Double,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtDoubleEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtDoubleEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2])),(*reinterpret_cast< double(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotPrecisionChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 4: _t->d_func()->slotSetValue((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotSetScale((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetFormat((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotUnitAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotFormatAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 13: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 14: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 15: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtDoubleEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtDoublePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtDoubleEditFactory.data,
    qt_meta_data_QtDoubleEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtDoubleEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtDoubleEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtDoubleEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtDoublePropertyManager>::qt_metacast(_clname);
}

int QtDoubleEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtDoublePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 16)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 16;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 16)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 16;
    }
    return _id;
}
struct qt_meta_stringdata_QtComplexEditFactory_t {
    QByteArrayData data[21];
    char stringdata0[411];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtComplexEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtComplexEditFactory_t qt_meta_stringdata_QtComplexEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 20), // "QtComplexEditFactory"
QT_MOC_LITERAL(1, 21, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 41, 0), // ""
QT_MOC_LITERAL(3, 42, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 54, 8), // "QComplex"
QT_MOC_LITERAL(5, 63, 16), // "slotRangeChanged"
QT_MOC_LITERAL(6, 80, 20), // "slotPrecisionChanged"
QT_MOC_LITERAL(7, 101, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(8, 121, 12), // "slotSetValue"
QT_MOC_LITERAL(9, 134, 12), // "slotSetScale"
QT_MOC_LITERAL(10, 147, 12), // "slotSetPkAvg"
QT_MOC_LITERAL(11, 160, 13), // "slotSetFormat"
QT_MOC_LITERAL(12, 174, 14), // "slotSetMinimum"
QT_MOC_LITERAL(13, 189, 14), // "slotSetMaximum"
QT_MOC_LITERAL(14, 204, 12), // "slotSetCheck"
QT_MOC_LITERAL(15, 217, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(16, 237, 32), // "slotUnitAttributeEditorDestroyed"
QT_MOC_LITERAL(17, 270, 34), // "slotFormatAttributeEditorDest..."
QT_MOC_LITERAL(18, 305, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(19, 341, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(20, 377, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtComplexEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0QComplex\0slotRangeChanged\0"
    "slotPrecisionChanged\0slotReadOnlyChanged\0"
    "slotSetValue\0slotSetScale\0slotSetPkAvg\0"
    "slotSetFormat\0slotSetMinimum\0"
    "slotSetMaximum\0slotSetCheck\0"
    "slotEditorDestroyed\0"
    "slotUnitAttributeEditorDestroyed\0"
    "slotFormatAttributeEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtComplexEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      17,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   99,    2, 0x08 /* Private */,
       5,    3,  104,    2, 0x08 /* Private */,
       6,    2,  111,    2, 0x08 /* Private */,
       7,    2,  116,    2, 0x08 /* Private */,
       8,    1,  121,    2, 0x08 /* Private */,
       9,    1,  124,    2, 0x08 /* Private */,
      10,    1,  127,    2, 0x08 /* Private */,
      11,    1,  130,    2, 0x08 /* Private */,
      12,    1,  133,    2, 0x08 /* Private */,
      13,    1,  136,    2, 0x08 /* Private */,
      14,    1,  139,    2, 0x08 /* Private */,
      15,    1,  142,    2, 0x08 /* Private */,
      16,    1,  145,    2, 0x08 /* Private */,
      17,    1,  148,    2, 0x08 /* Private */,
      18,    1,  151,    2, 0x08 /* Private */,
      19,    1,  154,    2, 0x08 /* Private */,
      20,    1,  157,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, 0x80000000 | 4,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Double, QMetaType::Double,    2,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, 0x80000000 | 4,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Double,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtComplexEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtComplexEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QComplex(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2])),(*reinterpret_cast< double(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotPrecisionChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 4: _t->d_func()->slotSetValue((*reinterpret_cast< const QComplex(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotSetScale((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetPkAvg((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotSetFormat((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotSetMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotSetMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 11: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 12: _t->d_func()->slotUnitAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 13: _t->d_func()->slotFormatAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 14: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 15: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 16: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtComplexEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtComplexPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtComplexEditFactory.data,
    qt_meta_data_QtComplexEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtComplexEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtComplexEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtComplexEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtComplexPropertyManager>::qt_metacast(_clname);
}

int QtComplexEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtComplexPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 17)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 17;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 17)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 17;
    }
    return _id;
}
struct qt_meta_stringdata_QtTFTensorEditFactory_t {
    QByteArrayData data[16];
    char stringdata0[340];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtTFTensorEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtTFTensorEditFactory_t qt_meta_stringdata_QtTFTensorEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 21), // "QtTFTensorEditFactory"
QT_MOC_LITERAL(1, 22, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 42, 0), // ""
QT_MOC_LITERAL(3, 43, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 55, 17), // "QVector<QComplex>"
QT_MOC_LITERAL(5, 73, 5), // "value"
QT_MOC_LITERAL(6, 79, 12), // "slotSetScale"
QT_MOC_LITERAL(7, 92, 12), // "slotSetPkAvg"
QT_MOC_LITERAL(8, 105, 13), // "slotSetFormat"
QT_MOC_LITERAL(9, 119, 12), // "slotSetCheck"
QT_MOC_LITERAL(10, 132, 32), // "slotUnitAttributeEditorDestroyed"
QT_MOC_LITERAL(11, 165, 33), // "slotPkAvgAttributeEditorDestr..."
QT_MOC_LITERAL(12, 199, 34), // "slotFormatAttributeEditorDest..."
QT_MOC_LITERAL(13, 234, 35), // "slotMinimumAttributeEditorDes..."
QT_MOC_LITERAL(14, 270, 35), // "slotMaximumAttributeEditorDes..."
QT_MOC_LITERAL(15, 306, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtTFTensorEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0QVector<QComplex>\0value\0"
    "slotSetScale\0slotSetPkAvg\0slotSetFormat\0"
    "slotSetCheck\0slotUnitAttributeEditorDestroyed\0"
    "slotPkAvgAttributeEditorDestroyed\0"
    "slotFormatAttributeEditorDestroyed\0"
    "slotMinimumAttributeEditorDestroyed\0"
    "slotMaximumAttributeEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtTFTensorEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   69,    2, 0x08 /* Private */,
       6,    1,   74,    2, 0x08 /* Private */,
       7,    1,   77,    2, 0x08 /* Private */,
       8,    1,   80,    2, 0x08 /* Private */,
       9,    1,   83,    2, 0x08 /* Private */,
      10,    1,   86,    2, 0x08 /* Private */,
      11,    1,   89,    2, 0x08 /* Private */,
      12,    1,   92,    2, 0x08 /* Private */,
      13,    1,   95,    2, 0x08 /* Private */,
      14,    1,   98,    2, 0x08 /* Private */,
      15,    1,  101,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, 0x80000000 | 4,    2,    5,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtTFTensorEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtTFTensorEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QVector<QComplex>(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotSetScale((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotSetPkAvg((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetFormat((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotUnitAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotPkAvgAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotFormatAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 8: _t->d_func()->slotMinimumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 9: _t->d_func()->slotMaximumAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 10: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtTFTensorEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtTFTensorPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtTFTensorEditFactory.data,
    qt_meta_data_QtTFTensorEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtTFTensorEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtTFTensorEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtTFTensorEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtTFTensorPropertyManager>::qt_metacast(_clname);
}

int QtTFTensorEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtTFTensorPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 11)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 11;
    }
    return _id;
}
struct qt_meta_stringdata_QtLineEditFactory_t {
    QByteArrayData data[11];
    char stringdata0[189];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtLineEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtLineEditFactory_t qt_meta_stringdata_QtLineEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 17), // "QtLineEditFactory"
QT_MOC_LITERAL(1, 18, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 38, 0), // ""
QT_MOC_LITERAL(3, 39, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 51, 17), // "slotRegExpChanged"
QT_MOC_LITERAL(5, 69, 19), // "slotEchoModeChanged"
QT_MOC_LITERAL(6, 89, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(7, 109, 12), // "slotSetValue"
QT_MOC_LITERAL(8, 122, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(9, 142, 12), // "slotSetCheck"
QT_MOC_LITERAL(10, 155, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtLineEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRegExpChanged\0"
    "slotEchoModeChanged\0slotReadOnlyChanged\0"
    "slotSetValue\0slotEditorDestroyed\0"
    "slotSetCheck\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtLineEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   54,    2, 0x08 /* Private */,
       4,    2,   59,    2, 0x08 /* Private */,
       5,    2,   64,    2, 0x08 /* Private */,
       6,    2,   69,    2, 0x08 /* Private */,
       7,    1,   74,    2, 0x08 /* Private */,
       8,    1,   77,    2, 0x08 /* Private */,
       9,    1,   80,    2, 0x08 /* Private */,
      10,    1,   83,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QString,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::QRegExp,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtLineEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtLineEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRegExpChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QRegExp(*)>(_a[2]))); break;
        case 2: _t->d_func()->slotEchoModeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 4: _t->d_func()->slotSetValue((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 7: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtLineEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtStringPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtLineEditFactory.data,
    qt_meta_data_QtLineEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtLineEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtLineEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtLineEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtStringPropertyManager>::qt_metacast(_clname);
}

int QtLineEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtStringPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 8)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 8;
    }
    return _id;
}
struct qt_meta_stringdata_QtDateEditFactory_t {
    QByteArrayData data[9];
    char stringdata0[148];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtDateEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtDateEditFactory_t qt_meta_stringdata_QtDateEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 17), // "QtDateEditFactory"
QT_MOC_LITERAL(1, 18, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 38, 0), // ""
QT_MOC_LITERAL(3, 39, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 51, 16), // "slotRangeChanged"
QT_MOC_LITERAL(5, 68, 12), // "slotSetValue"
QT_MOC_LITERAL(6, 81, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 94, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(8, 114, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtDateEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotRangeChanged\0"
    "slotSetValue\0slotSetCheck\0slotEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtDateEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   44,    2, 0x08 /* Private */,
       4,    3,   49,    2, 0x08 /* Private */,
       5,    1,   56,    2, 0x08 /* Private */,
       6,    1,   59,    2, 0x08 /* Private */,
       7,    1,   62,    2, 0x08 /* Private */,
       8,    1,   65,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QDate,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::QDate, QMetaType::QDate,    2,    2,    2,
    QMetaType::Void, QMetaType::QDate,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtDateEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtDateEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QDate(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotRangeChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QDate(*)>(_a[2])),(*reinterpret_cast< const QDate(*)>(_a[3]))); break;
        case 2: _t->d_func()->slotSetValue((*reinterpret_cast< const QDate(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtDateEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtDatePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtDateEditFactory.data,
    qt_meta_data_QtDateEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtDateEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtDateEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtDateEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtDatePropertyManager>::qt_metacast(_clname);
}

int QtDateEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtDatePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}
struct qt_meta_stringdata_QtTimeEditFactory_t {
    QByteArrayData data[8];
    char stringdata0[131];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtTimeEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtTimeEditFactory_t qt_meta_stringdata_QtTimeEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 17), // "QtTimeEditFactory"
QT_MOC_LITERAL(1, 18, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 38, 0), // ""
QT_MOC_LITERAL(3, 39, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 51, 12), // "slotSetValue"
QT_MOC_LITERAL(5, 64, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(6, 84, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 97, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtTimeEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotSetValue\0slotEditorDestroyed\0"
    "slotSetCheck\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtTimeEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    1,   44,    2, 0x08 /* Private */,
       5,    1,   47,    2, 0x08 /* Private */,
       6,    1,   50,    2, 0x08 /* Private */,
       7,    1,   53,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QTime,    2,    2,
    QMetaType::Void, QMetaType::QTime,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtTimeEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtTimeEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QTime(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotSetValue((*reinterpret_cast< const QTime(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtTimeEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtTimePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtTimeEditFactory.data,
    qt_meta_data_QtTimeEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtTimeEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtTimeEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtTimeEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtTimePropertyManager>::qt_metacast(_clname);
}

int QtTimeEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtTimePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtDateTimeEditFactory_t {
    QByteArrayData data[8];
    char stringdata0[135];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtDateTimeEditFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtDateTimeEditFactory_t qt_meta_stringdata_QtDateTimeEditFactory = {
    {
QT_MOC_LITERAL(0, 0, 21), // "QtDateTimeEditFactory"
QT_MOC_LITERAL(1, 22, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 42, 0), // ""
QT_MOC_LITERAL(3, 43, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 55, 12), // "slotSetValue"
QT_MOC_LITERAL(5, 68, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(6, 88, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 101, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtDateTimeEditFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotSetValue\0slotEditorDestroyed\0"
    "slotSetCheck\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtDateTimeEditFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    1,   44,    2, 0x08 /* Private */,
       5,    1,   47,    2, 0x08 /* Private */,
       6,    1,   50,    2, 0x08 /* Private */,
       7,    1,   53,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QDateTime,    2,    2,
    QMetaType::Void, QMetaType::QDateTime,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtDateTimeEditFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtDateTimeEditFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QDateTime(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotSetValue((*reinterpret_cast< const QDateTime(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtDateTimeEditFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtDateTimePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtDateTimeEditFactory.data,
    qt_meta_data_QtDateTimeEditFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtDateTimeEditFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtDateTimeEditFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtDateTimeEditFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtDateTimePropertyManager>::qt_metacast(_clname);
}

int QtDateTimeEditFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtDateTimePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtKeySequenceEditorFactory_t {
    QByteArrayData data[8];
    char stringdata0[140];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtKeySequenceEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtKeySequenceEditorFactory_t qt_meta_stringdata_QtKeySequenceEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 26), // "QtKeySequenceEditorFactory"
QT_MOC_LITERAL(1, 27, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 47, 0), // ""
QT_MOC_LITERAL(3, 48, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 60, 12), // "slotSetValue"
QT_MOC_LITERAL(5, 73, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(6, 93, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 106, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtKeySequenceEditorFactory\0"
    "slotPropertyChanged\0\0QtProperty*\0"
    "slotSetValue\0slotEditorDestroyed\0"
    "slotSetCheck\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtKeySequenceEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    1,   44,    2, 0x08 /* Private */,
       5,    1,   47,    2, 0x08 /* Private */,
       6,    1,   50,    2, 0x08 /* Private */,
       7,    1,   53,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QKeySequence,    2,    2,
    QMetaType::Void, QMetaType::QKeySequence,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtKeySequenceEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtKeySequenceEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QKeySequence(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotSetValue((*reinterpret_cast< const QKeySequence(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtKeySequenceEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtKeySequencePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtKeySequenceEditorFactory.data,
    qt_meta_data_QtKeySequenceEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtKeySequenceEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtKeySequenceEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtKeySequenceEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtKeySequencePropertyManager>::qt_metacast(_clname);
}

int QtKeySequenceEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtKeySequencePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtCharEditorFactory_t {
    QByteArrayData data[8];
    char stringdata0[133];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtCharEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtCharEditorFactory_t qt_meta_stringdata_QtCharEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtCharEditorFactory"
QT_MOC_LITERAL(1, 20, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 53, 12), // "slotSetValue"
QT_MOC_LITERAL(5, 66, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(6, 86, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 99, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtCharEditorFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotSetValue\0slotEditorDestroyed\0"
    "slotSetCheck\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtCharEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    1,   44,    2, 0x08 /* Private */,
       5,    1,   47,    2, 0x08 /* Private */,
       6,    1,   50,    2, 0x08 /* Private */,
       7,    1,   53,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QChar,    2,    2,
    QMetaType::Void, QMetaType::QChar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtCharEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtCharEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QChar(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotSetValue((*reinterpret_cast< const QChar(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtCharEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtCharPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtCharEditorFactory.data,
    qt_meta_data_QtCharEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtCharEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtCharEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtCharEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtCharPropertyManager>::qt_metacast(_clname);
}

int QtCharEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtCharPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtLocaleEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[70];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtLocaleEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtLocaleEditorFactory_t qt_meta_stringdata_QtLocaleEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 21), // "QtLocaleEditorFactory"
QT_MOC_LITERAL(1, 22, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 35, 0), // ""
QT_MOC_LITERAL(3, 36, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtLocaleEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtLocaleEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtLocaleEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtLocaleEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtLocaleEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtLocalePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtLocaleEditorFactory.data,
    qt_meta_data_QtLocaleEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtLocaleEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtLocaleEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtLocaleEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtLocalePropertyManager>::qt_metacast(_clname);
}

int QtLocaleEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtLocalePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtPointEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[69];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtPointEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtPointEditorFactory_t qt_meta_stringdata_QtPointEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 20), // "QtPointEditorFactory"
QT_MOC_LITERAL(1, 21, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 34, 0), // ""
QT_MOC_LITERAL(3, 35, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtPointEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtPointEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtPointEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtPointEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtPointEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtPointPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtPointEditorFactory.data,
    qt_meta_data_QtPointEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtPointEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtPointEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtPointEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtPointPropertyManager>::qt_metacast(_clname);
}

int QtPointEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtPointPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtPointFEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[70];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtPointFEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtPointFEditorFactory_t qt_meta_stringdata_QtPointFEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 21), // "QtPointFEditorFactory"
QT_MOC_LITERAL(1, 22, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 35, 0), // ""
QT_MOC_LITERAL(3, 36, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtPointFEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtPointFEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtPointFEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtPointFEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtPointFEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtPointFPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtPointFEditorFactory.data,
    qt_meta_data_QtPointFEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtPointFEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtPointFEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtPointFEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtPointFPropertyManager>::qt_metacast(_clname);
}

int QtPointFEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtPointFPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtSizeEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[68];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtSizeEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtSizeEditorFactory_t qt_meta_stringdata_QtSizeEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtSizeEditorFactory"
QT_MOC_LITERAL(1, 20, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 33, 0), // ""
QT_MOC_LITERAL(3, 34, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtSizeEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtSizeEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtSizeEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtSizeEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtSizeEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtSizePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtSizeEditorFactory.data,
    qt_meta_data_QtSizeEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtSizeEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtSizeEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtSizeEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtSizePropertyManager>::qt_metacast(_clname);
}

int QtSizeEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtSizePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtSizeFEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[69];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtSizeFEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtSizeFEditorFactory_t qt_meta_stringdata_QtSizeFEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 20), // "QtSizeFEditorFactory"
QT_MOC_LITERAL(1, 21, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 34, 0), // ""
QT_MOC_LITERAL(3, 35, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtSizeFEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtSizeFEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtSizeFEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtSizeFEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtSizeFEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtSizeFPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtSizeFEditorFactory.data,
    qt_meta_data_QtSizeFEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtSizeFEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtSizeFEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtSizeFEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtSizeFPropertyManager>::qt_metacast(_clname);
}

int QtSizeFEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtSizeFPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtRectEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[68];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtRectEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtRectEditorFactory_t qt_meta_stringdata_QtRectEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtRectEditorFactory"
QT_MOC_LITERAL(1, 20, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 33, 0), // ""
QT_MOC_LITERAL(3, 34, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtRectEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtRectEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtRectEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtRectEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtRectEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtRectPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtRectEditorFactory.data,
    qt_meta_data_QtRectEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtRectEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtRectEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtRectEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtRectPropertyManager>::qt_metacast(_clname);
}

int QtRectEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtRectPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtRectFEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[69];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtRectFEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtRectFEditorFactory_t qt_meta_stringdata_QtRectFEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 20), // "QtRectFEditorFactory"
QT_MOC_LITERAL(1, 21, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 34, 0), // ""
QT_MOC_LITERAL(3, 35, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtRectFEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtRectFEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtRectFEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtRectFEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtRectFEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtRectFPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtRectFEditorFactory.data,
    qt_meta_data_QtRectFEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtRectFEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtRectFEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtRectFEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtRectFPropertyManager>::qt_metacast(_clname);
}

int QtRectFEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtRectFPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtEnumEditorFactory_t {
    QByteArrayData data[11];
    char stringdata0[191];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtEnumEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtEnumEditorFactory_t qt_meta_stringdata_QtEnumEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtEnumEditorFactory"
QT_MOC_LITERAL(1, 20, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 53, 20), // "slotEnumNamesChanged"
QT_MOC_LITERAL(5, 74, 20), // "slotEnumIconsChanged"
QT_MOC_LITERAL(6, 95, 15), // "QMap<int,QIcon>"
QT_MOC_LITERAL(7, 111, 12), // "slotSetValue"
QT_MOC_LITERAL(8, 124, 12), // "slotSetCheck"
QT_MOC_LITERAL(9, 137, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(10, 157, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtEnumEditorFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotEnumNamesChanged\0"
    "slotEnumIconsChanged\0QMap<int,QIcon>\0"
    "slotSetValue\0slotSetCheck\0slotEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtEnumEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   49,    2, 0x08 /* Private */,
       4,    2,   54,    2, 0x08 /* Private */,
       5,    2,   59,    2, 0x08 /* Private */,
       7,    1,   64,    2, 0x08 /* Private */,
       8,    1,   67,    2, 0x08 /* Private */,
       9,    1,   70,    2, 0x08 /* Private */,
      10,    1,   73,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::QStringList,    2,    2,
    QMetaType::Void, 0x80000000 | 3, 0x80000000 | 6,    2,    2,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtEnumEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtEnumEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotEnumNamesChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QStringList(*)>(_a[2]))); break;
        case 2: _t->d_func()->slotEnumIconsChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QMap<int,QIcon>(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotSetValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtEnumEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtEnumPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtEnumEditorFactory.data,
    qt_meta_data_QtEnumEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtEnumEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtEnumEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtEnumEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtEnumPropertyManager>::qt_metacast(_clname);
}

int QtEnumEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtEnumPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 7;
    }
    return _id;
}
struct qt_meta_stringdata_QtFlagEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[68];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtFlagEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtFlagEditorFactory_t qt_meta_stringdata_QtFlagEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtFlagEditorFactory"
QT_MOC_LITERAL(1, 20, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 33, 0), // ""
QT_MOC_LITERAL(3, 34, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtFlagEditorFactory\0slotSetCheck\0\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtFlagEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtFlagEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtFlagEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtFlagEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtFlagPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtFlagEditorFactory.data,
    qt_meta_data_QtFlagEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtFlagEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtFlagEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtFlagEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtFlagPropertyManager>::qt_metacast(_clname);
}

int QtFlagEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtFlagPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtSizePolicyEditorFactory_t {
    QByteArrayData data[4];
    char stringdata0[74];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtSizePolicyEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtSizePolicyEditorFactory_t qt_meta_stringdata_QtSizePolicyEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 25), // "QtSizePolicyEditorFactory"
QT_MOC_LITERAL(1, 26, 12), // "slotSetCheck"
QT_MOC_LITERAL(2, 39, 0), // ""
QT_MOC_LITERAL(3, 40, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtSizePolicyEditorFactory\0slotSetCheck\0"
    "\0slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtSizePolicyEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   24,    2, 0x08 /* Private */,
       3,    1,   27,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtSizePolicyEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtSizePolicyEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtSizePolicyEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtSizePolicyPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtSizePolicyEditorFactory.data,
    qt_meta_data_QtSizePolicyEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtSizePolicyEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtSizePolicyEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtSizePolicyEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtSizePolicyPropertyManager>::qt_metacast(_clname);
}

int QtSizePolicyEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtSizePolicyPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 2;
    }
    return _id;
}
struct qt_meta_stringdata_QtCursorEditorFactory_t {
    QByteArrayData data[8];
    char stringdata0[138];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtCursorEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtCursorEditorFactory_t qt_meta_stringdata_QtCursorEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 21), // "QtCursorEditorFactory"
QT_MOC_LITERAL(1, 22, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 42, 0), // ""
QT_MOC_LITERAL(3, 43, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 55, 15), // "slotEnumChanged"
QT_MOC_LITERAL(5, 71, 12), // "slotSetCheck"
QT_MOC_LITERAL(6, 84, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(7, 104, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtCursorEditorFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotEnumChanged\0slotSetCheck\0"
    "slotEditorDestroyed\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtCursorEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    2,   44,    2, 0x08 /* Private */,
       5,    1,   49,    2, 0x08 /* Private */,
       6,    1,   52,    2, 0x08 /* Private */,
       7,    1,   55,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QCursor,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Int,    2,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtCursorEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtCursorEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QCursor(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotEnumChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 2: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtCursorEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtCursorPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtCursorEditorFactory.data,
    qt_meta_data_QtCursorEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtCursorEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtCursorEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtCursorEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtCursorPropertyManager>::qt_metacast(_clname);
}

int QtCursorEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtCursorPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtColorEditorFactory_t {
    QByteArrayData data[8];
    char stringdata0[134];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtColorEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtColorEditorFactory_t qt_meta_stringdata_QtColorEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 20), // "QtColorEditorFactory"
QT_MOC_LITERAL(1, 21, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 41, 0), // ""
QT_MOC_LITERAL(3, 42, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 54, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(5, 74, 12), // "slotSetValue"
QT_MOC_LITERAL(6, 87, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 100, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtColorEditorFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotEditorDestroyed\0"
    "slotSetValue\0slotSetCheck\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtColorEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    1,   44,    2, 0x08 /* Private */,
       5,    1,   47,    2, 0x08 /* Private */,
       6,    1,   50,    2, 0x08 /* Private */,
       7,    1,   53,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QColor,    2,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QColor,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtColorEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtColorEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QColor(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotSetValue((*reinterpret_cast< const QColor(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtColorEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtColorPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtColorEditorFactory.data,
    qt_meta_data_QtColorEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtColorEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtColorEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtColorEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtColorPropertyManager>::qt_metacast(_clname);
}

int QtColorEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtColorPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtFontEditorFactory_t {
    QByteArrayData data[8];
    char stringdata0[133];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtFontEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtFontEditorFactory_t qt_meta_stringdata_QtFontEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtFontEditorFactory"
QT_MOC_LITERAL(1, 20, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 53, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(5, 73, 12), // "slotSetValue"
QT_MOC_LITERAL(6, 86, 12), // "slotSetCheck"
QT_MOC_LITERAL(7, 99, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtFontEditorFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotEditorDestroyed\0"
    "slotSetValue\0slotSetCheck\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtFontEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   39,    2, 0x08 /* Private */,
       4,    1,   44,    2, 0x08 /* Private */,
       5,    1,   47,    2, 0x08 /* Private */,
       6,    1,   50,    2, 0x08 /* Private */,
       7,    1,   53,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QFont,    2,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QFont,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtFontEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtFontEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QFont(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 2: _t->d_func()->slotSetValue((*reinterpret_cast< const QFont(*)>(_a[1]))); break;
        case 3: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtFontEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtFontPropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtFontEditorFactory.data,
    qt_meta_data_QtFontEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtFontEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtFontEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtFontEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtFontPropertyManager>::qt_metacast(_clname);
}

int QtFontEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtFontPropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
struct qt_meta_stringdata_QtFileEditorFactory_t {
    QByteArrayData data[10];
    char stringdata0[171];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtFileEditorFactory_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtFileEditorFactory_t qt_meta_stringdata_QtFileEditorFactory = {
    {
QT_MOC_LITERAL(0, 0, 19), // "QtFileEditorFactory"
QT_MOC_LITERAL(1, 20, 19), // "slotPropertyChanged"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 11), // "QtProperty*"
QT_MOC_LITERAL(4, 53, 17), // "slotFilterChanged"
QT_MOC_LITERAL(5, 71, 19), // "slotReadOnlyChanged"
QT_MOC_LITERAL(6, 91, 19), // "slotEditorDestroyed"
QT_MOC_LITERAL(7, 111, 12), // "slotSetValue"
QT_MOC_LITERAL(8, 124, 12), // "slotSetCheck"
QT_MOC_LITERAL(9, 137, 33) // "slotCheckAttributeEditorDestr..."

    },
    "QtFileEditorFactory\0slotPropertyChanged\0"
    "\0QtProperty*\0slotFilterChanged\0"
    "slotReadOnlyChanged\0slotEditorDestroyed\0"
    "slotSetValue\0slotSetCheck\0"
    "slotCheckAttributeEditorDestroyed"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtFileEditorFactory[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    2,   49,    2, 0x08 /* Private */,
       4,    2,   54,    2, 0x08 /* Private */,
       5,    2,   59,    2, 0x08 /* Private */,
       6,    1,   64,    2, 0x08 /* Private */,
       7,    1,   67,    2, 0x08 /* Private */,
       8,    1,   70,    2, 0x08 /* Private */,
       9,    1,   73,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 3, QMetaType::QString,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::QString,    2,    2,
    QMetaType::Void, 0x80000000 | 3, QMetaType::Bool,    2,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,
    QMetaType::Void, QMetaType::QString,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::QObjectStar,    2,

       0        // eod
};

void QtFileEditorFactory::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtFileEditorFactory *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->d_func()->slotPropertyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 1: _t->d_func()->slotFilterChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< const QString(*)>(_a[2]))); break;
        case 2: _t->d_func()->slotReadOnlyChanged((*reinterpret_cast< QtProperty*(*)>(_a[1])),(*reinterpret_cast< bool(*)>(_a[2]))); break;
        case 3: _t->d_func()->slotEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 4: _t->d_func()->slotSetValue((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->d_func()->slotSetCheck((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->d_func()->slotCheckAttributeEditorDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtFileEditorFactory::staticMetaObject = { {
    &QtAbstractEditorFactory<QtFilePropertyManager>::staticMetaObject,
    qt_meta_stringdata_QtFileEditorFactory.data,
    qt_meta_data_QtFileEditorFactory,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtFileEditorFactory::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtFileEditorFactory::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtFileEditorFactory.stringdata0))
        return static_cast<void*>(this);
    return QtAbstractEditorFactory<QtFilePropertyManager>::qt_metacast(_clname);
}

int QtFileEditorFactory::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtAbstractEditorFactory<QtFilePropertyManager>::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 7;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
