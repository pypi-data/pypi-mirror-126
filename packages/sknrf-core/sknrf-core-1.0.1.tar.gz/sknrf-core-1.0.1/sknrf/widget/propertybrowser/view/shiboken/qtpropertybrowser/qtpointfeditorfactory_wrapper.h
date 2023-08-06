#ifndef SBK_QTPOINTFEDITORFACTORYWRAPPER_H
#define SBK_QTPOINTFEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtPointFEditorFactoryWrapper : public QtPointFEditorFactory
{
public:
    QtPointFEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtPointFPropertyManager * manager) { QtPointFEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtPointFPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtPointFEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtPointFEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtPointFPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtPointFPropertyManager * manager) { QtPointFEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtPointFPropertyManager * manager) override;
    ~QtPointFEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTPOINTFEDITORFACTORYWRAPPER_H

