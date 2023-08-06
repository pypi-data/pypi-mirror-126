
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
#include <algorithm>
#include <set>

// module include
#include "qtpropertybrowser_python.h"

// main header
#include "qtabstractpropertybrowser_wrapper.h"

// inner classes

// Extra includes
#include <QList>
#include <qbytearray.h>
#include <qcursor.h>
#include <qfont.h>
#include <qfontinfo.h>
#include <qfontmetrics.h>
#include <qicon.h>
#include <qkeysequence.h>
#include <qlocale.h>
#include <qmargins.h>
#include <qobject.h>
#include <qobjectdefs.h>
#include <qpaintdevice.h>
#include <qpalette.h>
#include <qpixmap.h>
#include <qpoint.h>
#include <qrect.h>
#include <qregion.h>
#include <qsize.h>
#include <qsizepolicy.h>
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

// Begin code injection
// ========================================================================
// START of custom code block [file: ./glue/qtpropertybrowser.cpp (qtabstractpropertybrowser-setFactoryForManager)]
template <int SBK_IDX, class PropertyManager>
static void setFactoryForManager_template(QtAbstractPropertyBrowser* self, PyObject* pyManager, PyObject* pyFactory )
{
    Shiboken::GilState gil;
    PythonToCppFunc pythonToCpp;
    SbkObjectType* shiboType;
    pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_IDX]), pyManager);
    if (pythonToCpp) {
        PropertyManager* cppManager;
        QtAbstractEditorFactory< PropertyManager >* cppFactory;
        pythonToCpp( pyManager, &cppManager);
        if (pyFactory == Py_None)
            cppFactory = 0;
        shiboType = reinterpret_cast<SbkObjectType*>(pyFactory->ob_type);
        if (Shiboken::ObjectType::hasCast(shiboType))
            cppFactory = reinterpret_cast<QtAbstractEditorFactory< PropertyManager >*>(Shiboken::ObjectType::cast(shiboType, reinterpret_cast<SbkObject*>(pyFactory), Shiboken::SbkType<QtAbstractEditorFactory< PropertyManager >>()));
        cppFactory = (QtAbstractEditorFactory< PropertyManager >*) Shiboken::Object::cppPointer(reinterpret_cast<SbkObject*>(pyFactory), Shiboken::SbkType<QtAbstractEditorFactory< PropertyManager >>());
        gil.release();
        self->setFactoryForManager(cppManager, cppFactory);
        return;
    }
}
static void setFactoryForManager_glue(QtAbstractPropertyBrowser* self, PyObject* pyManager, PyObject* pyFactory )
{
    setFactoryForManager_template <SBK_QTGROUPPROPERTYMANAGER_IDX, QtGroupPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTINTPROPERTYMANAGER_IDX, QtIntPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTBOOLPROPERTYMANAGER_IDX, QtBoolPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTDOUBLEPROPERTYMANAGER_IDX, QtDoublePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCOMPLEXPROPERTYMANAGER_IDX, QtComplexPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTTFTENSORPROPERTYMANAGER_IDX, QtTFTensorPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSTRINGPROPERTYMANAGER_IDX, QtStringPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTFILEPROPERTYMANAGER_IDX, QtFilePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTDATEPROPERTYMANAGER_IDX, QtDatePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTTIMEPROPERTYMANAGER_IDX, QtTimePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTDATETIMEPROPERTYMANAGER_IDX, QtDateTimePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTKEYSEQUENCEPROPERTYMANAGER_IDX, QtKeySequencePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCHARPROPERTYMANAGER_IDX, QtCharPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTLOCALEPROPERTYMANAGER_IDX, QtLocalePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTPOINTPROPERTYMANAGER_IDX, QtPointPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTPOINTFPROPERTYMANAGER_IDX, QtPointFPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSIZEPROPERTYMANAGER_IDX, QtSizePropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSIZEFPROPERTYMANAGER_IDX, QtSizeFPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTRECTPROPERTYMANAGER_IDX, QtRectPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTRECTFPROPERTYMANAGER_IDX, QtRectFPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTENUMPROPERTYMANAGER_IDX, QtEnumPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTFLAGPROPERTYMANAGER_IDX, QtFlagPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTSIZEPOLICYPROPERTYMANAGER_IDX, QtSizePolicyPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCURSORPROPERTYMANAGER_IDX, QtCursorPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTFONTPROPERTYMANAGER_IDX, QtFontPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTCOLORPROPERTYMANAGER_IDX, QtColorPropertyManager> (self, pyManager, pyFactory );
    setFactoryForManager_template <SBK_QTVARIANTPROPERTYMANAGER_IDX, QtVariantPropertyManager> (self, pyManager, pyFactory );
}

// END of custom code block [file: ./glue/qtpropertybrowser.cpp (qtabstractpropertybrowser-setFactoryForManager)]
// ========================================================================

// End of code injection

// Native ---------------------------------------------------------

void QtAbstractPropertyBrowserWrapper::pysideInitQtMetaTypes()
{
}

QtAbstractPropertyBrowserWrapper::QtAbstractPropertyBrowserWrapper(QWidget * parent) : QtAbstractPropertyBrowser(parent)
{
    // ... middle
}

void QtAbstractPropertyBrowserWrapper::actionEvent(QActionEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "actionEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::actionEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QACTIONEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::changeEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "changeEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::changeEvent(event);
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

void QtAbstractPropertyBrowserWrapper::childEvent(QChildEvent * event)
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

void QtAbstractPropertyBrowserWrapper::closeEvent(QCloseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "closeEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::closeEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCLOSEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::connectNotify(const QMetaMethod & signal)
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

void QtAbstractPropertyBrowserWrapper::contextMenuEvent(QContextMenuEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "contextMenuEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::contextMenuEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QCONTEXTMENUEVENT_IDX]), event)
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

QWidget * QtAbstractPropertyBrowserWrapper::createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createAttributeEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyBrowser::createAttributeEditor(property, parent, attribute);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NNN)",
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.createAttributeEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QWidget * QtAbstractPropertyBrowserWrapper::createEditor(QtProperty * property, QWidget * parent)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "createEditor"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QtAbstractPropertyBrowser::createEditor(property, parent);
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.createEditor", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QWidget >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QWidget *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::customEvent(QEvent * event)
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

int QtAbstractPropertyBrowserWrapper::devType() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "devType"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::devType();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return 0;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.devType", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::disconnectNotify(const QMetaMethod & signal)
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

void QtAbstractPropertyBrowserWrapper::dragEnterEvent(QDragEnterEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dragEnterEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dragEnterEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDRAGENTEREVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::dragLeaveEvent(QDragLeaveEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dragLeaveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dragLeaveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDRAGLEAVEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::dragMoveEvent(QDragMoveEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dragMoveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dragMoveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDRAGMOVEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::dropEvent(QDropEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "dropEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::dropEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QDROPEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::enterEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "enterEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::enterEvent(event);
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

bool QtAbstractPropertyBrowserWrapper::event(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "event"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::event(event);
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.event", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg1)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 0));
    return cppResult;
}

bool QtAbstractPropertyBrowserWrapper::eventFilter(QObject * watched, QEvent * event)
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
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.eventFilter", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    if (invalidateArg2)
        Shiboken::Object::invalidate(PyTuple_GET_ITEM(pyArgs, 1));
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::focusInEvent(QFocusEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "focusInEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::focusInEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QFOCUSEVENT_IDX]), event)
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

bool QtAbstractPropertyBrowserWrapper::focusNextPrevChild(bool next)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "focusNextPrevChild"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::focusNextPrevChild(next);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &next)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.focusNextPrevChild", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::focusOutEvent(QFocusEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "focusOutEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::focusOutEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QFOCUSEVENT_IDX]), event)
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

bool QtAbstractPropertyBrowserWrapper::hasHeightForWidth() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "hasHeightForWidth"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::hasHeightForWidth();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.hasHeightForWidth", "bool", Py_TYPE(pyResult)->tp_name);
        return false;
    }
    bool cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

int QtAbstractPropertyBrowserWrapper::heightForWidth(int arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "heightForWidth"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::heightForWidth(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(i)",
        arg__1
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return 0;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.heightForWidth", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::hideEvent(QHideEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "hideEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::hideEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QHIDEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::initPainter(QPainter * painter) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "initPainter"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::initPainter(painter);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTER_IDX]), painter)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::inputMethodEvent(QInputMethodEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "inputMethodEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::inputMethodEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QINPUTMETHODEVENT_IDX]), event)
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

QVariant QtAbstractPropertyBrowserWrapper::inputMethodQuery(Qt::InputMethodQuery arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return ::QVariant();
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "inputMethodQuery"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::inputMethodQuery(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkPySide2_QtCoreTypes[SBK_QT_INPUTMETHODQUERY_IDX])->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return ::QVariant();
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(SbkPySide2_QtCoreTypeConverters[SBK_QVARIANT_IDX], pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.inputMethodQuery", "QVariant", Py_TYPE(pyResult)->tp_name);
        return ::QVariant();
    }
    ::QVariant cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::itemChanged(QtBrowserItem * item)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemChanged"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractPropertyBrowser.itemChanged()' not implemented.");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemInserted"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractPropertyBrowser.itemInserted()' not implemented.");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), item),
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), afterItem)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::itemRemoved(QtBrowserItem * item)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "itemRemoved"));
    if (pyOverride.isNull()) {
        PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractPropertyBrowser.itemRemoved()' not implemented.");
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), item)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

void QtAbstractPropertyBrowserWrapper::keyPressEvent(QKeyEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "keyPressEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::keyPressEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QKEYEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::keyReleaseEvent(QKeyEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "keyReleaseEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::keyReleaseEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QKEYEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::leaveEvent(QEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "leaveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::leaveEvent(event);
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

int QtAbstractPropertyBrowserWrapper::metric(QPaintDevice::PaintDeviceMetric arg__1) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return 0;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "metric"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::metric(arg__1);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(*PepType_SGTP(SbkPySide2_QtGuiTypes[SBK_QPAINTDEVICE_PAINTDEVICEMETRIC_IDX])->converter, &arg__1)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return 0;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppConvertible(Shiboken::Conversions::PrimitiveTypeConverter<int>(), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.metric", "int", Py_TYPE(pyResult)->tp_name);
        return 0;
    }
    int cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

QSize QtAbstractPropertyBrowserWrapper::minimumSizeHint() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "minimumSizeHint"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::minimumSizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QSIZE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.minimumSizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::mouseDoubleClickEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mouseDoubleClickEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mouseDoubleClickEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::mouseMoveEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mouseMoveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mouseMoveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::mousePressEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mousePressEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mousePressEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::mouseReleaseEvent(QMouseEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "mouseReleaseEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::mouseReleaseEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOUSEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::moveEvent(QMoveEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "moveEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::moveEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QMOVEEVENT_IDX]), event)
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

bool QtAbstractPropertyBrowserWrapper::nativeEvent(const QByteArray & eventType, void * message, long * result)
{

    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return false;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "nativeEvent"));
    if (pyOverride.isNull()) {

        gil.release();
        return this->::QWidget::nativeEvent(eventType, message, result);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(NN)",
        Shiboken::Conversions::copyToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QBYTEARRAY_IDX]), &eventType),
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<void *>(), message)
    ));


    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return false;
    }
    // Begin code injection

    // TEMPLATE - return_native_eventfilter_conversion - START
    bool cppResult = false;
    if (PySequence_Check(pyResult) && (PySequence_Size(pyResult) == 2)) {
    Shiboken::AutoDecRef pyItem(PySequence_GetItem(pyResult, 0));
    Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), pyItem, &(cppResult));
    if (result) {
        Shiboken::AutoDecRef pyResultItem(PySequence_GetItem(pyResult, 1));
        Shiboken::Conversions::pythonToCppCopy(Shiboken::Conversions::PrimitiveTypeConverter<long>(), pyResultItem, (result));
    }
    }
    // TEMPLATE - return_native_eventfilter_conversion - END

    // End of code injection

    return cppResult;
}

QPaintEngine * QtAbstractPropertyBrowserWrapper::paintEngine() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "paintEngine"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::paintEngine();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTENGINE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.paintEngine", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintEngine >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintEngine *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::paintEvent(QPaintEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "paintEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::paintEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTEVENT_IDX]), event)
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

QPaintDevice * QtAbstractPropertyBrowserWrapper::redirected(QPoint * offset) const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "redirected"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::redirected(offset);
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QPOINT_IDX]), offset)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTDEVICE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.redirected", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPaintDevice >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPaintDevice *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::resizeEvent(QResizeEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "resizeEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::resizeEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QRESIZEEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::setVisible(bool visible)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "setVisible"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::setVisible(visible);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::copyToPython(Shiboken::Conversions::PrimitiveTypeConverter<bool>(), &visible)
    ));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return;
    }
}

QPainter * QtAbstractPropertyBrowserWrapper::sharedPainter() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return nullptr;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "sharedPainter"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::sharedPainter();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return nullptr;
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTER_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.sharedPainter", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QPainter >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return nullptr;
    }
    ::QPainter *cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::showEvent(QShowEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "showEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::showEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QSHOWEVENT_IDX]), event)
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

QSize QtAbstractPropertyBrowserWrapper::sizeHint() const
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return {};
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "sizeHint"));
    if (pyOverride.isNull()) {
        gil.release();
        return this->::QWidget::sizeHint();
    }

    Shiboken::AutoDecRef pyArgs(PyTuple_New(0));

    Shiboken::AutoDecRef pyResult(PyObject_Call(pyOverride, pyArgs, nullptr));
    // An error happened in python code!
    if (pyResult.isNull()) {
        PyErr_Print();
        return {};
    }
    // Check return type
    PythonToCppFunc pythonToCpp = Shiboken::Conversions::isPythonToCppValueConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QSIZE_IDX]), pyResult);
    if (!pythonToCpp) {
        Shiboken::warning(PyExc_RuntimeWarning, 2, "Invalid return value in function %s, expected %s, got %s.", "QtAbstractPropertyBrowser.sizeHint", reinterpret_cast<PyTypeObject *>(Shiboken::SbkType< QSize >())->tp_name, Py_TYPE(pyResult)->tp_name);
        return {};
    }
    ::QSize cppResult;
    pythonToCpp(pyResult, &cppResult);
    return cppResult;
}

void QtAbstractPropertyBrowserWrapper::tabletEvent(QTabletEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "tabletEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::tabletEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QTABLETEVENT_IDX]), event)
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

void QtAbstractPropertyBrowserWrapper::timerEvent(QTimerEvent * event)
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

void QtAbstractPropertyBrowserWrapper::wheelEvent(QWheelEvent * event)
{
    Shiboken::GilState gil;
    if (PyErr_Occurred())
        return;
    Shiboken::AutoDecRef pyOverride(Shiboken::BindingManager::instance().getOverride(this, "wheelEvent"));
    if (pyOverride.isNull()) {
        gil.release();
        this->::QWidget::wheelEvent(event);
        return;
    }

    Shiboken::AutoDecRef pyArgs(Py_BuildValue("(N)",
        Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QWHEELEVENT_IDX]), event)
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

const QMetaObject *QtAbstractPropertyBrowserWrapper::metaObject() const
{
    if (QObject::d_ptr->metaObject)
        return QObject::d_ptr->dynamicMetaObject();
    SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
    if (pySelf == nullptr)
        return QtAbstractPropertyBrowser::metaObject();
    return PySide::SignalManager::retrieveMetaObject(reinterpret_cast<PyObject *>(pySelf));
}

int QtAbstractPropertyBrowserWrapper::qt_metacall(QMetaObject::Call call, int id, void **args)
{
    int result = QtAbstractPropertyBrowser::qt_metacall(call, id, args);
    return result < 0 ? result : PySide::SignalManager::qt_metacall(this, call, id, args);
}

void *QtAbstractPropertyBrowserWrapper::qt_metacast(const char *_clname)
{
        if (!_clname) return {};
        SbkObject *pySelf = Shiboken::BindingManager::instance().retrieveWrapper(this);
        if (pySelf && PySide::inherits(Py_TYPE(pySelf), _clname))
                return static_cast<void *>(const_cast< QtAbstractPropertyBrowserWrapper *>(this));
        return QtAbstractPropertyBrowser::qt_metacast(_clname);
}

QtAbstractPropertyBrowserWrapper::~QtAbstractPropertyBrowserWrapper()
{
    SbkObject *wrapper = Shiboken::BindingManager::instance().retrieveWrapper(this);
    Shiboken::Object::destroy(wrapper, this);
}

// Target ---------------------------------------------------------

extern "C" {
static int
Sbk_QtAbstractPropertyBrowser_Init(PyObject *self, PyObject *args, PyObject *kwds)
{
    const char *argNames[] = {"parent"};
    const QMetaObject *metaObject;
    SbkObject *sbkSelf = reinterpret_cast<SbkObject *>(self);
    SbkObjectType *type = reinterpret_cast<SbkObjectType *>(self->ob_type);
    SbkObjectType *myType = reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX]);
    if (type == myType) {
        PyErr_SetString(PyExc_NotImplementedError,
            "'QtAbstractPropertyBrowser' represents a C++ abstract class and cannot be instantiated");
        return -1;
    }

    if (Shiboken::Object::isUserType(self) && !Shiboken::ObjectType::canCallConstructor(self->ob_type, Shiboken::SbkType< ::QtAbstractPropertyBrowser >()))
        return -1;

    ::QtAbstractPropertyBrowserWrapper *cptr{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0};

    // invalid argument lengths


    if (!PyArg_ParseTuple(args, "|O:QtAbstractPropertyBrowser", &(pyArgs[0])))
        return -1;


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::QtAbstractPropertyBrowser(QWidget*)
    if (numArgs == 0) {
        overloadId = 0; // QtAbstractPropertyBrowser(QWidget*)
    } else if ((pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[0])))) {
        overloadId = 0; // QtAbstractPropertyBrowser(QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;

    // Call function/method
    {
        if (kwds) {
            PyObject *keyName = nullptr;
            PyObject *value = nullptr;
            keyName = Py_BuildValue("s","parent");
            if (PyDict_Contains(kwds, keyName)) {
            value = PyDict_GetItemString(kwds, "parent");
            if (value && pyArgs[0]) {
                PyErr_SetString(PyExc_TypeError, "qtpropertybrowser.QtAbstractPropertyBrowser(): got multiple values for keyword argument 'parent'.");
                return -1;
                        } else if (value) {
                pyArgs[0] = value;
                if (!(pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[0]))))
                    goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;
            }
}
        }
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return -1;
        ::QWidget *cppArg0 = nullptr;
        if (pythonToCpp[0]) pythonToCpp[0](pyArgs[0], &cppArg0);

        if (!PyErr_Occurred()) {
            // QtAbstractPropertyBrowser(QWidget*)
            void *addr = PySide::nextQObjectMemoryAddr();
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            if (addr) {
                cptr = new (addr) ::QtAbstractPropertyBrowserWrapper(cppArg0);
                PySide::setNextQObjectMemoryAddr(0);
            } else {
                cptr = new ::QtAbstractPropertyBrowserWrapper(cppArg0);
            }

            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            Shiboken::Object::setParent(pyArgs[0], self);
        }
    }

    if (PyErr_Occurred() || !Shiboken::Object::setCppPointer(sbkSelf, Shiboken::SbkType< ::QtAbstractPropertyBrowser >(), cptr)) {
        delete cptr;
        return -1;
    }
    if (!cptr) goto Sbk_QtAbstractPropertyBrowser_Init_TypeError;

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

    Sbk_QtAbstractPropertyBrowser_Init_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractPropertyBrowser");
        return -1;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_addProperty(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::addProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // addProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_addProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // addProperty(QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QtBrowserItem * cppResult = cppSelf->addProperty(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_addProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.addProperty");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_clear(PyObject *self)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // clear()
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->clear();
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor(PyObject *self, PyObject *args)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
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
    // 0: QtAbstractPropertyBrowser::createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
    if (numArgs == 3
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[1])))
        && (pythonToCpp[2] = Shiboken::Conversions::isPythonToCppConvertible(*PepType_SGTP(SbkqtpropertybrowserTypes[SBK_BROWSERCOL_IDX])->converter, (pyArgs[2])))) {
        overloadId = 0; // createAttributeEditor(QtProperty*,QWidget*,BrowserCol)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor_TypeError;

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
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->QtAbstractPropertyBrowserWrapper::createAttributeEditor_protected(cppArg0, cppArg1, cppArg2);
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

    Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractPropertyBrowser.createAttributeEditor");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_createEditor(PyObject *self, PyObject *args)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
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
    // 0: QtAbstractPropertyBrowser::createEditor(QtProperty*,QWidget*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]), (pyArgs[1])))) {
        overloadId = 0; // createEditor(QtProperty*,QWidget*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_createEditor_TypeError;

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
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QWidget * cppResult = static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->QtAbstractPropertyBrowserWrapper::createEditor_protected(cppArg0, cppArg1);
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

    Sbk_QtAbstractPropertyBrowserFunc_createEditor_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractPropertyBrowser.createEditor");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_currentItem(PyObject *self)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // currentItem()const
            QtBrowserItem * cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->currentItem();
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_insertProperty(PyObject *self, PyObject *args)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "insertProperty", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::insertProperty(QtProperty*,QtProperty*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArgs[1])))) {
        overloadId = 0; // insertProperty(QtProperty*,QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_insertProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtProperty *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // insertProperty(QtProperty*,QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QtBrowserItem * cppResult = cppSelf->insertProperty(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_insertProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractPropertyBrowser.insertProperty");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_itemChanged(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemChanged(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // itemChanged(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_itemChanged_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemChanged(QtBrowserItem*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractPropertyBrowser.itemChanged()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->itemChanged_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_itemChanged_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.itemChanged");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_itemInserted(PyObject *self, PyObject *args)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "itemInserted", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemInserted(QtBrowserItem*,QtBrowserItem*)
    if (numArgs == 2
        && (pythonToCpp[0] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[0])))
        && (pythonToCpp[1] = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArgs[1])))) {
        overloadId = 0; // itemInserted(QtBrowserItem*,QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_itemInserted_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArgs[0]))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp[0](pyArgs[0], &cppArg0);
        if (!Shiboken::Object::isValid(pyArgs[1]))
            return {};
        ::QtBrowserItem *cppArg1;
        pythonToCpp[1](pyArgs[1], &cppArg1);

        if (!PyErr_Occurred()) {
            // itemInserted(QtBrowserItem*,QtBrowserItem*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractPropertyBrowser.itemInserted()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->itemInserted_protected(cppArg0, cppArg1);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_itemInserted_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractPropertyBrowser.itemInserted");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_itemRemoved(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::itemRemoved(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // itemRemoved(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_itemRemoved_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // itemRemoved(QtBrowserItem*)
            if (Shiboken::Object::hasCppWrapper(reinterpret_cast<SbkObject *>(self))) {
                PyErr_SetString(PyExc_NotImplementedError, "pure virtual method 'QtAbstractPropertyBrowser.itemRemoved()' not implemented.");
                return {};
            }
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            static_cast<::QtAbstractPropertyBrowserWrapper *>(cppSelf)->itemRemoved_protected(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_itemRemoved_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.itemRemoved");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_items(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::items(QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // items(QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_items_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // items(QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QList<QtBrowserItem* > cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->items(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_items_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.items");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_properties(PyObject *self)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // properties()const
            QList<QtProperty* > cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->properties();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTPROPERTYPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_removeProperty(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::removeProperty(QtProperty*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // removeProperty(QtProperty*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_removeProperty_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // removeProperty(QtProperty*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->removeProperty(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_removeProperty_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.removeProperty");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::setCurrentItem(QtBrowserItem*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), (pyArg)))) {
        overloadId = 0; // setCurrentItem(QtBrowserItem*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtBrowserItem *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // setCurrentItem(QtBrowserItem*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->setCurrentItem(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.setCurrentItem");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager(PyObject *self, PyObject *args)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp[] = { nullptr, nullptr };
    SBK_UNUSED(pythonToCpp)
    int numArgs = PyTuple_GET_SIZE(args);
    SBK_UNUSED(numArgs)
    PyObject *pyArgs[] = {0, 0};

    // invalid argument lengths


    if (!PyArg_UnpackTuple(args, "setFactoryForManager", 2, 2, &(pyArgs[0]), &(pyArgs[1])))
        return {};


    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::setFactoryForManager(PyObject*,PyObject*)
    if (numArgs == 2
        && PyObject_Check(pyArgs[0])
        && PyObject_Check(pyArgs[1])) {
        overloadId = 0; // setFactoryForManager(PyObject*,PyObject*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager_TypeError;

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // setFactoryForManager(PyObject*,PyObject*)
            // Begin code injection

            setFactoryForManager_glue( cppSelf, pyArgs[1-1], pyArgs[2-1] );

            // End of code injection


        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(args, "qtpropertybrowser.QtAbstractPropertyBrowser.setFactoryForManager");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_topLevelItem(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::topLevelItem(QtProperty*)const
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTPROPERTY_IDX]), (pyArg)))) {
        overloadId = 0; // topLevelItem(QtProperty*)const
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_topLevelItem_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtProperty *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // topLevelItem(QtProperty*)const
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            QtBrowserItem * cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->topLevelItem(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
            pyResult = Shiboken::Conversions::pointerToPython(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTBROWSERITEM_IDX]), cppResult);
            Shiboken::Object::setParent(self, pyResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;

    Sbk_QtAbstractPropertyBrowserFunc_topLevelItem_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.topLevelItem");
        return {};
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_topLevelItems(PyObject *self)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    PyObject *pyResult{};

    // Call function/method
    {

        if (!PyErr_Occurred()) {
            // topLevelItems()const
            QList<QtBrowserItem* > cppResult = const_cast<const ::QtAbstractPropertyBrowserWrapper *>(cppSelf)->topLevelItems();
            pyResult = Shiboken::Conversions::copyToPython(SbkqtpropertybrowserTypeConverters[SBK_QTPROPERTYBROWSER_QLIST_QTBROWSERITEMPTR_IDX], &cppResult);
        }
    }

    if (PyErr_Occurred() || !pyResult) {
        Py_XDECREF(pyResult);
        return {};
    }
    return pyResult;
}

static PyObject *Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager(PyObject *self, PyObject *pyArg)
{
    QtAbstractPropertyBrowserWrapper *cppSelf = nullptr;
    SBK_UNUSED(cppSelf)
    if (!Shiboken::Object::isValid(self))
        return {};
    cppSelf = static_cast<QtAbstractPropertyBrowserWrapper *>(reinterpret_cast< ::QtAbstractPropertyBrowser *>(Shiboken::Conversions::cppPointer(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX], reinterpret_cast<SbkObject *>(self))));
    int overloadId = -1;
    PythonToCppFunc pythonToCpp{};
    SBK_UNUSED(pythonToCpp)

    // Overloaded function decisor
    // 0: QtAbstractPropertyBrowser::unsetFactoryForManager(QtAbstractPropertyManager*)
    if ((pythonToCpp = Shiboken::Conversions::isPythonToCppPointerConvertible(reinterpret_cast<SbkObjectType *>(SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYMANAGER_IDX]), (pyArg)))) {
        overloadId = 0; // unsetFactoryForManager(QtAbstractPropertyManager*)
    }

    // Function signature not found.
    if (overloadId == -1) goto Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager_TypeError;

    // Call function/method
    {
        if (!Shiboken::Object::isValid(pyArg))
            return {};
        ::QtAbstractPropertyManager *cppArg0;
        pythonToCpp(pyArg, &cppArg0);

        if (!PyErr_Occurred()) {
            // unsetFactoryForManager(QtAbstractPropertyManager*)
            PyThreadState *_save = PyEval_SaveThread(); // Py_BEGIN_ALLOW_THREADS
            cppSelf->unsetFactoryForManager(cppArg0);
            PyEval_RestoreThread(_save); // Py_END_ALLOW_THREADS
        }
    }

    if (PyErr_Occurred()) {
        return {};
    }
    Py_RETURN_NONE;

    Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager_TypeError:
        Shiboken::setErrorAboutWrongArguments(pyArg, "qtpropertybrowser.QtAbstractPropertyBrowser.unsetFactoryForManager");
        return {};
}

static PyMethodDef Sbk_QtAbstractPropertyBrowser_methods[] = {
    {"addProperty", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_addProperty), METH_O},
    {"clear", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_clear), METH_NOARGS},
    {"createAttributeEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_createAttributeEditor), METH_VARARGS},
    {"createEditor", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_createEditor), METH_VARARGS},
    {"currentItem", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_currentItem), METH_NOARGS},
    {"insertProperty", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_insertProperty), METH_VARARGS},
    {"itemChanged", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_itemChanged), METH_O},
    {"itemInserted", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_itemInserted), METH_VARARGS},
    {"itemRemoved", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_itemRemoved), METH_O},
    {"items", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_items), METH_O},
    {"properties", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_properties), METH_NOARGS},
    {"removeProperty", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_removeProperty), METH_O},
    {"setCurrentItem", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_setCurrentItem), METH_O},
    {"setFactoryForManager", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_setFactoryForManager), METH_VARARGS},
    {"topLevelItem", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_topLevelItem), METH_O},
    {"topLevelItems", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_topLevelItems), METH_NOARGS},
    {"unsetFactoryForManager", reinterpret_cast<PyCFunction>(Sbk_QtAbstractPropertyBrowserFunc_unsetFactoryForManager), METH_O},

    {nullptr, nullptr} // Sentinel
};

} // extern "C"

static int Sbk_QtAbstractPropertyBrowser_traverse(PyObject *self, visitproc visit, void *arg)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_traverse(self, visit, arg);
}
static int Sbk_QtAbstractPropertyBrowser_clear(PyObject *self)
{
    return reinterpret_cast<PyTypeObject *>(SbkObject_TypeF())->tp_clear(self);
}
static void * Sbk_QtAbstractPropertyBrowserSpecialCastFunction(void *obj, SbkObjectType *desiredType)
{
    auto me = reinterpret_cast< ::QtAbstractPropertyBrowser *>(obj);
    if (desiredType == reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]))
        return static_cast< ::QWidget *>(me);
    else if (desiredType == reinterpret_cast<SbkObjectType *>(SbkPySide2_QtCoreTypes[SBK_QOBJECT_IDX]))
        return static_cast< ::QObject *>(me);
    else if (desiredType == reinterpret_cast<SbkObjectType *>(SbkPySide2_QtGuiTypes[SBK_QPAINTDEVICE_IDX]))
        return static_cast< ::QPaintDevice *>(me);
    return me;
}


// Class Definition -----------------------------------------------
extern "C" {
static SbkObjectType *_Sbk_QtAbstractPropertyBrowser_Type = nullptr;
static SbkObjectType *Sbk_QtAbstractPropertyBrowser_TypeF(void)
{
    return _Sbk_QtAbstractPropertyBrowser_Type;
}

static PyType_Slot Sbk_QtAbstractPropertyBrowser_slots[] = {
    {Py_tp_base,        nullptr}, // inserted by introduceWrapperType
    {Py_tp_dealloc,     reinterpret_cast<void *>(&SbkDeallocWrapper)},
    {Py_tp_repr,        nullptr},
    {Py_tp_hash,        nullptr},
    {Py_tp_call,        nullptr},
    {Py_tp_str,         nullptr},
    {Py_tp_getattro,    nullptr},
    {Py_tp_setattro,    nullptr},
    {Py_tp_traverse,    reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_traverse)},
    {Py_tp_clear,       reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_clear)},
    {Py_tp_richcompare, nullptr},
    {Py_tp_iter,        nullptr},
    {Py_tp_iternext,    nullptr},
    {Py_tp_methods,     reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_methods)},
    {Py_tp_getset,      nullptr},
    {Py_tp_init,        reinterpret_cast<void *>(Sbk_QtAbstractPropertyBrowser_Init)},
    {Py_tp_new,         reinterpret_cast<void *>(SbkObjectTpNew)},
    {0, nullptr}
};
static PyType_Spec Sbk_QtAbstractPropertyBrowser_spec = {
    "qtpropertybrowser.QtAbstractPropertyBrowser",
    sizeof(SbkObject),
    0,
    Py_TPFLAGS_DEFAULT|Py_TPFLAGS_BASETYPE|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_GC,
    Sbk_QtAbstractPropertyBrowser_slots
};

} //extern "C"

static void *Sbk_QtAbstractPropertyBrowser_typeDiscovery(void *cptr, SbkObjectType *instanceType)
{
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QObject >()))
        return dynamic_cast< ::QtAbstractPropertyBrowser *>(reinterpret_cast< ::QObject *>(cptr));
    if (instanceType == reinterpret_cast<SbkObjectType *>(Shiboken::SbkType< ::QPaintDevice >()))
        return dynamic_cast< ::QtAbstractPropertyBrowser *>(reinterpret_cast< ::QPaintDevice *>(cptr));
    return {};
}


// Type conversion functions.

// Python to C++ pointer conversion - returns the C++ object of the Python wrapper (keeps object identity).
static void QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR(PyObject *pyIn, void *cppOut) {
    Shiboken::Conversions::pythonToCppPointer(Sbk_QtAbstractPropertyBrowser_TypeF(), pyIn, cppOut);
}
static PythonToCppFunc is_QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR_Convertible(PyObject *pyIn) {
    if (pyIn == Py_None)
        return Shiboken::Conversions::nonePythonToCppNullPtr;
    if (PyObject_TypeCheck(pyIn, reinterpret_cast<PyTypeObject *>(Sbk_QtAbstractPropertyBrowser_TypeF())))
        return QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR;
    return {};
}

// C++ to Python pointer conversion - tries to find the Python wrapper for the C++ object (keeps object identity).
static PyObject *QtAbstractPropertyBrowser_PTR_CppToPython_QtAbstractPropertyBrowser(const void *cppIn) {
    return PySide::getWrapperForQObject(reinterpret_cast<::QtAbstractPropertyBrowser *>(const_cast<void *>(cppIn)), Sbk_QtAbstractPropertyBrowser_TypeF());

}

// The signatures string for the functions.
// Multiple signatures have their index "n:" in front.
static const char *QtAbstractPropertyBrowser_SignatureStrings[] = {
    "qtpropertybrowser.QtAbstractPropertyBrowser(parent:PySide2.QtWidgets.QWidget=nullptr)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.addProperty(property:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.clear()",
    "qtpropertybrowser.QtAbstractPropertyBrowser.createAttributeEditor(property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget,attribute:qtpropertybrowser.BrowserCol)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractPropertyBrowser.createEditor(property:qtpropertybrowser.QtProperty,parent:PySide2.QtWidgets.QWidget)->PySide2.QtWidgets.QWidget",
    "qtpropertybrowser.QtAbstractPropertyBrowser.currentItem()->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.insertProperty(property:qtpropertybrowser.QtProperty,afterProperty:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.itemChanged(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.itemInserted(item:qtpropertybrowser.QtBrowserItem,afterItem:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.itemRemoved(item:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.items(property:qtpropertybrowser.QtProperty)->QList[qtpropertybrowser.QtBrowserItem]",
    "qtpropertybrowser.QtAbstractPropertyBrowser.properties()->QList[qtpropertybrowser.QtProperty]",
    "qtpropertybrowser.QtAbstractPropertyBrowser.removeProperty(property:qtpropertybrowser.QtProperty)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.setCurrentItem(arg__1:qtpropertybrowser.QtBrowserItem)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.setFactoryForManager(arg__1:PyObject,arg__2:PyObject)",
    "qtpropertybrowser.QtAbstractPropertyBrowser.topLevelItem(property:qtpropertybrowser.QtProperty)->qtpropertybrowser.QtBrowserItem",
    "qtpropertybrowser.QtAbstractPropertyBrowser.topLevelItems()->QList[qtpropertybrowser.QtBrowserItem]",
    "qtpropertybrowser.QtAbstractPropertyBrowser.unsetFactoryForManager(manager:qtpropertybrowser.QtAbstractPropertyManager)",
    nullptr}; // Sentinel

void init_QtAbstractPropertyBrowser(PyObject *module)
{
    _Sbk_QtAbstractPropertyBrowser_Type = Shiboken::ObjectType::introduceWrapperType(
        module,
        "QtAbstractPropertyBrowser",
        "QtAbstractPropertyBrowser*",
        &Sbk_QtAbstractPropertyBrowser_spec,
        QtAbstractPropertyBrowser_SignatureStrings,
        &Shiboken::callCppDestructor< ::QtAbstractPropertyBrowser >,
        reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]),
        0,
        Shiboken::ObjectType::WrapperFlags::DeleteInMainThread    );
    
    SbkqtpropertybrowserTypes[SBK_QTABSTRACTPROPERTYBROWSER_IDX]
        = reinterpret_cast<PyTypeObject *>(Sbk_QtAbstractPropertyBrowser_TypeF());

    // Register Converter
    SbkConverter *converter = Shiboken::Conversions::createConverter(Sbk_QtAbstractPropertyBrowser_TypeF(),
        QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR,
        is_QtAbstractPropertyBrowser_PythonToCpp_QtAbstractPropertyBrowser_PTR_Convertible,
        QtAbstractPropertyBrowser_PTR_CppToPython_QtAbstractPropertyBrowser);

    Shiboken::Conversions::registerConverterName(converter, "QtAbstractPropertyBrowser");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractPropertyBrowser*");
    Shiboken::Conversions::registerConverterName(converter, "QtAbstractPropertyBrowser&");
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractPropertyBrowser).name());
    Shiboken::Conversions::registerConverterName(converter, typeid(::QtAbstractPropertyBrowserWrapper).name());



    MultipleInheritanceInitFunction func = Shiboken::ObjectType::getMultipleInheritanceFunction(reinterpret_cast<SbkObjectType *>(SbkPySide2_QtWidgetsTypes[SBK_QWIDGET_IDX]));
    Shiboken::ObjectType::setMultipleInheritanceFunction(Sbk_QtAbstractPropertyBrowser_TypeF(), func);
    Shiboken::ObjectType::setCastFunction(Sbk_QtAbstractPropertyBrowser_TypeF(), &Sbk_QtAbstractPropertyBrowserSpecialCastFunction);
    Shiboken::ObjectType::setTypeDiscoveryFunctionV2(Sbk_QtAbstractPropertyBrowser_TypeF(), &Sbk_QtAbstractPropertyBrowser_typeDiscovery);

    PySide::Signal::registerSignals(Sbk_QtAbstractPropertyBrowser_TypeF(), &::QtAbstractPropertyBrowser::staticMetaObject);


    QtAbstractPropertyBrowserWrapper::pysideInitQtMetaTypes();
    Shiboken::ObjectType::setSubTypeInitHook(Sbk_QtAbstractPropertyBrowser_TypeF(), &PySide::initQObjectSubType);
    PySide::initDynamicMetaObject(Sbk_QtAbstractPropertyBrowser_TypeF(), &::QtAbstractPropertyBrowser::staticMetaObject, sizeof(::QtAbstractPropertyBrowser));
}

