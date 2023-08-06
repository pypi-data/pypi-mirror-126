#ifndef SBK_QTABSTRACTEDITORFACTORYBASEWRAPPER_H
#define SBK_QTABSTRACTEDITORFACTORYBASEWRAPPER_H

#include <qtpropertybrowser.h>

namespace PySide { class DynamicQMetaObject; }

class QtAbstractEditorFactoryBaseWrapper : public QtAbstractEditorFactoryBase
{
public:
    QtAbstractEditorFactoryBaseWrapper(QObject * parent = nullptr);
    inline void breakConnection_protected(QtAbstractPropertyManager * manager) { breakConnection(manager); }
    void breakConnection(QtAbstractPropertyManager * manager) override;
    inline void childEvent_protected(QChildEvent * event) { QtAbstractEditorFactoryBase::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QtAbstractEditorFactoryBase::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    QWidget * createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol atttribute) override;
    QWidget * createEditor(QtProperty * property, QWidget * parent) override;
    inline void customEvent_protected(QEvent * event) { QtAbstractEditorFactoryBase::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QtAbstractEditorFactoryBase::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline bool isSignalConnected_protected(const QMetaMethod & signal) const { return QtAbstractEditorFactoryBase::isSignalConnected(signal); }
    inline void managerDestroyed_protected(QObject * manager) { managerDestroyed(manager); }
    void managerDestroyed(QObject * manager) override;
    const QMetaObject * metaObject() const override;
    inline int receivers_protected(const char * signal) const { return QtAbstractEditorFactoryBase::receivers(signal); }
    inline QObject * sender_protected() const { return QtAbstractEditorFactoryBase::sender(); }
    inline int senderSignalIndex_protected() const { return QtAbstractEditorFactoryBase::senderSignalIndex(); }
    inline void timerEvent_protected(QTimerEvent * event) { QtAbstractEditorFactoryBase::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    ~QtAbstractEditorFactoryBaseWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  ifndef SBK_QOBJECTWRAPPER_H
#  define SBK_QOBJECTWRAPPER_H

// Inherited base class:
class QObjectWrapper : public QObject
{
public:
    QObjectWrapper(QObject * parent = nullptr);
    inline void childEvent_protected(QChildEvent * event) { QObject::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QObject::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void customEvent_protected(QEvent * event) { QObject::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QObject::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline bool isSignalConnected_protected(const QMetaMethod & signal) const { return QObject::isSignalConnected(signal); }
    const QMetaObject * metaObject() const override;
    inline int receivers_protected(const char * signal) const { return QObject::receivers(signal); }
    inline QObject * sender_protected() const { return QObject::sender(); }
    inline int senderSignalIndex_protected() const { return QObject::senderSignalIndex(); }
    inline void timerEvent_protected(QTimerEvent * event) { QObject::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    ~QObjectWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QOBJECTWRAPPER_H

#endif // SBK_QTABSTRACTEDITORFACTORYBASEWRAPPER_H

