/****************************************************************************
** Meta object code from reading C++ file 'qtpropertybrowserutils_p.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.13.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../../../../../../../../sknrf/widget/propertybrowser/view/src/qtpropertybrowserutils_p.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qtpropertybrowserutils_p.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.13.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_QIntEdit_t {
    QByteArrayData data[19];
    char stringdata0[155];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QIntEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QIntEdit_t qt_meta_stringdata_QIntEdit = {
    {
QT_MOC_LITERAL(0, 0, 8), // "QIntEdit"
QT_MOC_LITERAL(1, 9, 12), // "valueChanged"
QT_MOC_LITERAL(2, 22, 0), // ""
QT_MOC_LITERAL(3, 23, 3), // "val"
QT_MOC_LITERAL(4, 27, 9), // "destroyed"
QT_MOC_LITERAL(5, 37, 3), // "obj"
QT_MOC_LITERAL(6, 41, 8), // "setValue"
QT_MOC_LITERAL(7, 50, 10), // "setMinimum"
QT_MOC_LITERAL(8, 61, 3), // "min"
QT_MOC_LITERAL(9, 65, 10), // "setMaximum"
QT_MOC_LITERAL(10, 76, 3), // "max"
QT_MOC_LITERAL(11, 80, 8), // "setRange"
QT_MOC_LITERAL(12, 89, 12), // "setPrecision"
QT_MOC_LITERAL(13, 102, 8), // "setScale"
QT_MOC_LITERAL(14, 111, 5), // "Scale"
QT_MOC_LITERAL(15, 117, 9), // "setFormat"
QT_MOC_LITERAL(16, 127, 6), // "Format"
QT_MOC_LITERAL(17, 134, 11), // "setReadOnly"
QT_MOC_LITERAL(18, 146, 8) // "readOnly"

    },
    "QIntEdit\0valueChanged\0\0val\0destroyed\0"
    "obj\0setValue\0setMinimum\0min\0setMaximum\0"
    "max\0setRange\0setPrecision\0setScale\0"
    "Scale\0setFormat\0Format\0setReadOnly\0"
    "readOnly"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QIntEdit[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   69,    2, 0x06 /* Public */,
       4,    1,   72,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       6,    0,   75,    2, 0x0a /* Public */,
       6,    1,   76,    2, 0x0a /* Public */,
       7,    1,   79,    2, 0x0a /* Public */,
       9,    1,   82,    2, 0x0a /* Public */,
      11,    2,   85,    2, 0x0a /* Public */,
      12,    1,   90,    2, 0x0a /* Public */,
      13,    1,   93,    2, 0x0a /* Public */,
      15,    1,   96,    2, 0x0a /* Public */,
      17,    1,   99,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, QMetaType::QObjectStar,    5,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Int,    3,
    QMetaType::Void, QMetaType::Double,    8,
    QMetaType::Void, QMetaType::Double,   10,
    QMetaType::Void, QMetaType::Double, QMetaType::Double,    8,   10,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, 0x80000000 | 14,    2,
    QMetaType::Void, 0x80000000 | 16,    2,
    QMetaType::Void, QMetaType::Bool,   18,

 // enums: name, alias, flags, count, data

 // enum data: key, value

       0        // eod
};

void QIntEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QIntEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->destroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 2: _t->setValue(); break;
        case 3: _t->setValue((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->setMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 5: _t->setMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->setRange((*reinterpret_cast< double(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2]))); break;
        case 7: _t->setPrecision((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->setScale((*reinterpret_cast< Scale(*)>(_a[1]))); break;
        case 9: _t->setFormat((*reinterpret_cast< Format(*)>(_a[1]))); break;
        case 10: _t->setReadOnly((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (QIntEdit::*)(int );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QIntEdit::valueChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (QIntEdit::*)(QObject * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QIntEdit::destroyed)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QIntEdit::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_QIntEdit.data,
    qt_meta_data_QIntEdit,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QIntEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QIntEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QIntEdit.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QIntEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QIntEdit::valueChanged(int _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void QIntEdit::destroyed(QObject * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
struct qt_meta_stringdata_QDoubleEdit_t {
    QByteArrayData data[19];
    char stringdata0[158];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QDoubleEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QDoubleEdit_t qt_meta_stringdata_QDoubleEdit = {
    {
QT_MOC_LITERAL(0, 0, 11), // "QDoubleEdit"
QT_MOC_LITERAL(1, 12, 12), // "valueChanged"
QT_MOC_LITERAL(2, 25, 0), // ""
QT_MOC_LITERAL(3, 26, 3), // "val"
QT_MOC_LITERAL(4, 30, 9), // "destroyed"
QT_MOC_LITERAL(5, 40, 3), // "obj"
QT_MOC_LITERAL(6, 44, 8), // "setValue"
QT_MOC_LITERAL(7, 53, 10), // "setMinimum"
QT_MOC_LITERAL(8, 64, 3), // "min"
QT_MOC_LITERAL(9, 68, 10), // "setMaximum"
QT_MOC_LITERAL(10, 79, 3), // "max"
QT_MOC_LITERAL(11, 83, 8), // "setRange"
QT_MOC_LITERAL(12, 92, 12), // "setPrecision"
QT_MOC_LITERAL(13, 105, 8), // "setScale"
QT_MOC_LITERAL(14, 114, 5), // "Scale"
QT_MOC_LITERAL(15, 120, 9), // "setFormat"
QT_MOC_LITERAL(16, 130, 6), // "Format"
QT_MOC_LITERAL(17, 137, 11), // "setReadOnly"
QT_MOC_LITERAL(18, 149, 8) // "readOnly"

    },
    "QDoubleEdit\0valueChanged\0\0val\0destroyed\0"
    "obj\0setValue\0setMinimum\0min\0setMaximum\0"
    "max\0setRange\0setPrecision\0setScale\0"
    "Scale\0setFormat\0Format\0setReadOnly\0"
    "readOnly"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QDoubleEdit[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   69,    2, 0x06 /* Public */,
       4,    1,   72,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       6,    0,   75,    2, 0x0a /* Public */,
       6,    1,   76,    2, 0x0a /* Public */,
       7,    1,   79,    2, 0x0a /* Public */,
       9,    1,   82,    2, 0x0a /* Public */,
      11,    2,   85,    2, 0x0a /* Public */,
      12,    1,   90,    2, 0x0a /* Public */,
      13,    1,   93,    2, 0x0a /* Public */,
      15,    1,   96,    2, 0x0a /* Public */,
      17,    1,   99,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::Double,    3,
    QMetaType::Void, QMetaType::QObjectStar,    5,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, QMetaType::Double,    3,
    QMetaType::Void, QMetaType::Double,    8,
    QMetaType::Void, QMetaType::Double,   10,
    QMetaType::Void, QMetaType::Double, QMetaType::Double,    8,   10,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, 0x80000000 | 14,    2,
    QMetaType::Void, 0x80000000 | 16,    2,
    QMetaType::Void, QMetaType::Bool,   18,

 // enums: name, alias, flags, count, data

 // enum data: key, value

       0        // eod
};

void QDoubleEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QDoubleEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 1: _t->destroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 2: _t->setValue(); break;
        case 3: _t->setValue((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 4: _t->setMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 5: _t->setMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->setRange((*reinterpret_cast< double(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2]))); break;
        case 7: _t->setPrecision((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->setScale((*reinterpret_cast< Scale(*)>(_a[1]))); break;
        case 9: _t->setFormat((*reinterpret_cast< Format(*)>(_a[1]))); break;
        case 10: _t->setReadOnly((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (QDoubleEdit::*)(double );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QDoubleEdit::valueChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (QDoubleEdit::*)(QObject * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QDoubleEdit::destroyed)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QDoubleEdit::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_QDoubleEdit.data,
    qt_meta_data_QDoubleEdit,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QDoubleEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QDoubleEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QDoubleEdit.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QDoubleEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QDoubleEdit::valueChanged(double _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void QDoubleEdit::destroyed(QObject * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
struct qt_meta_stringdata_QComplexEdit_t {
    QByteArrayData data[20];
    char stringdata0[168];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QComplexEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QComplexEdit_t qt_meta_stringdata_QComplexEdit = {
    {
QT_MOC_LITERAL(0, 0, 12), // "QComplexEdit"
QT_MOC_LITERAL(1, 13, 12), // "valueChanged"
QT_MOC_LITERAL(2, 26, 0), // ""
QT_MOC_LITERAL(3, 27, 8), // "QComplex"
QT_MOC_LITERAL(4, 36, 3), // "val"
QT_MOC_LITERAL(5, 40, 9), // "destroyed"
QT_MOC_LITERAL(6, 50, 3), // "obj"
QT_MOC_LITERAL(7, 54, 8), // "setValue"
QT_MOC_LITERAL(8, 63, 10), // "setMinimum"
QT_MOC_LITERAL(9, 74, 3), // "min"
QT_MOC_LITERAL(10, 78, 10), // "setMaximum"
QT_MOC_LITERAL(11, 89, 3), // "max"
QT_MOC_LITERAL(12, 93, 8), // "setRange"
QT_MOC_LITERAL(13, 102, 12), // "setPrecision"
QT_MOC_LITERAL(14, 115, 8), // "setScale"
QT_MOC_LITERAL(15, 124, 5), // "Scale"
QT_MOC_LITERAL(16, 130, 9), // "setFormat"
QT_MOC_LITERAL(17, 140, 6), // "Format"
QT_MOC_LITERAL(18, 147, 11), // "setReadOnly"
QT_MOC_LITERAL(19, 159, 8) // "readOnly"

    },
    "QComplexEdit\0valueChanged\0\0QComplex\0"
    "val\0destroyed\0obj\0setValue\0setMinimum\0"
    "min\0setMaximum\0max\0setRange\0setPrecision\0"
    "setScale\0Scale\0setFormat\0Format\0"
    "setReadOnly\0readOnly"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QComplexEdit[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   69,    2, 0x06 /* Public */,
       5,    1,   72,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       7,    0,   75,    2, 0x0a /* Public */,
       7,    1,   76,    2, 0x0a /* Public */,
       8,    1,   79,    2, 0x0a /* Public */,
      10,    1,   82,    2, 0x0a /* Public */,
      12,    2,   85,    2, 0x0a /* Public */,
      13,    1,   90,    2, 0x0a /* Public */,
      14,    1,   93,    2, 0x0a /* Public */,
      16,    1,   96,    2, 0x0a /* Public */,
      18,    1,   99,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void, 0x80000000 | 3,    4,
    QMetaType::Void, QMetaType::QObjectStar,    6,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 3,    4,
    QMetaType::Void, QMetaType::Double,    9,
    QMetaType::Void, QMetaType::Double,   11,
    QMetaType::Void, QMetaType::Double, QMetaType::Double,    9,   11,
    QMetaType::Void, QMetaType::Int,    2,
    QMetaType::Void, 0x80000000 | 15,    2,
    QMetaType::Void, 0x80000000 | 17,    2,
    QMetaType::Void, QMetaType::Bool,   19,

 // enums: name, alias, flags, count, data

 // enum data: key, value

       0        // eod
};

void QComplexEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QComplexEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< const QComplex(*)>(_a[1]))); break;
        case 1: _t->destroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 2: _t->setValue(); break;
        case 3: _t->setValue((*reinterpret_cast< const QComplex(*)>(_a[1]))); break;
        case 4: _t->setMinimum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 5: _t->setMaximum((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 6: _t->setRange((*reinterpret_cast< double(*)>(_a[1])),(*reinterpret_cast< double(*)>(_a[2]))); break;
        case 7: _t->setPrecision((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 8: _t->setScale((*reinterpret_cast< Scale(*)>(_a[1]))); break;
        case 9: _t->setFormat((*reinterpret_cast< Format(*)>(_a[1]))); break;
        case 10: _t->setReadOnly((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (QComplexEdit::*)(const QComplex & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QComplexEdit::valueChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (QComplexEdit::*)(QObject * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QComplexEdit::destroyed)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QComplexEdit::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_QComplexEdit.data,
    qt_meta_data_QComplexEdit,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QComplexEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QComplexEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QComplexEdit.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QComplexEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QComplexEdit::valueChanged(const QComplex & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void QComplexEdit::destroyed(QObject * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
struct qt_meta_stringdata_QFileEdit_t {
    QByteArrayData data[16];
    char stringdata0[165];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QFileEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QFileEdit_t qt_meta_stringdata_QFileEdit = {
    {
QT_MOC_LITERAL(0, 0, 9), // "QFileEdit"
QT_MOC_LITERAL(1, 10, 12), // "valueChanged"
QT_MOC_LITERAL(2, 23, 0), // ""
QT_MOC_LITERAL(3, 24, 5), // "value"
QT_MOC_LITERAL(4, 30, 9), // "destroyed"
QT_MOC_LITERAL(5, 40, 3), // "obj"
QT_MOC_LITERAL(6, 44, 8), // "setValue"
QT_MOC_LITERAL(7, 53, 9), // "setFilter"
QT_MOC_LITERAL(8, 63, 6), // "filter"
QT_MOC_LITERAL(9, 70, 11), // "setFileMode"
QT_MOC_LITERAL(10, 82, 21), // "QFileDialog::FileMode"
QT_MOC_LITERAL(11, 104, 4), // "mode"
QT_MOC_LITERAL(12, 109, 11), // "setReadOnly"
QT_MOC_LITERAL(13, 121, 8), // "readOnly"
QT_MOC_LITERAL(14, 130, 16), // "slotEditFinished"
QT_MOC_LITERAL(15, 147, 17) // "slotButtonClicked"

    },
    "QFileEdit\0valueChanged\0\0value\0destroyed\0"
    "obj\0setValue\0setFilter\0filter\0setFileMode\0"
    "QFileDialog::FileMode\0mode\0setReadOnly\0"
    "readOnly\0slotEditFinished\0slotButtonClicked"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QFileEdit[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   54,    2, 0x06 /* Public */,
       4,    1,   57,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       6,    1,   60,    2, 0x0a /* Public */,
       7,    1,   63,    2, 0x0a /* Public */,
       9,    1,   66,    2, 0x0a /* Public */,
      12,    1,   69,    2, 0x0a /* Public */,
      14,    0,   72,    2, 0x08 /* Private */,
      15,    0,   73,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QObjectStar,    5,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    8,
    QMetaType::Void, 0x80000000 | 10,   11,
    QMetaType::Void, QMetaType::Bool,   13,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void QFileEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QFileEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->valueChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->destroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 2: _t->setValue((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 3: _t->setFilter((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 4: _t->setFileMode((*reinterpret_cast< const QFileDialog::FileMode(*)>(_a[1]))); break;
        case 5: _t->setReadOnly((*reinterpret_cast< const bool(*)>(_a[1]))); break;
        case 6: _t->slotEditFinished(); break;
        case 7: _t->slotButtonClicked(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (QFileEdit::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QFileEdit::valueChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (QFileEdit::*)(QObject * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QFileEdit::destroyed)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QFileEdit::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_QFileEdit.data,
    qt_meta_data_QFileEdit,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QFileEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QFileEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QFileEdit.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QFileEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QFileEdit::valueChanged(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void QFileEdit::destroyed(QObject * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
struct qt_meta_stringdata_QtBoolEdit_t {
    QByteArrayData data[3];
    char stringdata0[20];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtBoolEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtBoolEdit_t qt_meta_stringdata_QtBoolEdit = {
    {
QT_MOC_LITERAL(0, 0, 10), // "QtBoolEdit"
QT_MOC_LITERAL(1, 11, 7), // "toggled"
QT_MOC_LITERAL(2, 19, 0) // ""

    },
    "QtBoolEdit\0toggled\0"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtBoolEdit[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       1,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   19,    2, 0x06 /* Public */,

 // signals: parameters
    QMetaType::Void, QMetaType::Bool,    2,

       0        // eod
};

void QtBoolEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtBoolEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->toggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (QtBoolEdit::*)(bool );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QtBoolEdit::toggled)) {
                *result = 0;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtBoolEdit::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_QtBoolEdit.data,
    qt_meta_data_QtBoolEdit,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtBoolEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtBoolEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtBoolEdit.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QtBoolEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QtBoolEdit::toggled(bool _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
struct qt_meta_stringdata_QtKeySequenceEdit_t {
    QByteArrayData data[6];
    char stringdata0[80];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_QtKeySequenceEdit_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_QtKeySequenceEdit_t qt_meta_stringdata_QtKeySequenceEdit = {
    {
QT_MOC_LITERAL(0, 0, 17), // "QtKeySequenceEdit"
QT_MOC_LITERAL(1, 18, 18), // "keySequenceChanged"
QT_MOC_LITERAL(2, 37, 0), // ""
QT_MOC_LITERAL(3, 38, 8), // "sequence"
QT_MOC_LITERAL(4, 47, 14), // "setKeySequence"
QT_MOC_LITERAL(5, 62, 17) // "slotClearShortcut"

    },
    "QtKeySequenceEdit\0keySequenceChanged\0"
    "\0sequence\0setKeySequence\0slotClearShortcut"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_QtKeySequenceEdit[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   29,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       4,    1,   32,    2, 0x0a /* Public */,
       5,    0,   35,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, QMetaType::QKeySequence,    3,

 // slots: parameters
    QMetaType::Void, QMetaType::QKeySequence,    3,
    QMetaType::Void,

       0        // eod
};

void QtKeySequenceEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<QtKeySequenceEdit *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->keySequenceChanged((*reinterpret_cast< const QKeySequence(*)>(_a[1]))); break;
        case 1: _t->setKeySequence((*reinterpret_cast< const QKeySequence(*)>(_a[1]))); break;
        case 2: _t->slotClearShortcut(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (QtKeySequenceEdit::*)(const QKeySequence & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&QtKeySequenceEdit::keySequenceChanged)) {
                *result = 0;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject QtKeySequenceEdit::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_QtKeySequenceEdit.data,
    qt_meta_data_QtKeySequenceEdit,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *QtKeySequenceEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtKeySequenceEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_QtKeySequenceEdit.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int QtKeySequenceEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void QtKeySequenceEdit::keySequenceChanged(const QKeySequence & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
