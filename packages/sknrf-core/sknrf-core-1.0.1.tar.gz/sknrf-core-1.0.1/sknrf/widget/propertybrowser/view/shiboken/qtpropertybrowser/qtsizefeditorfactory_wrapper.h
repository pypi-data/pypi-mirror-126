#ifndef SBK_QTSIZEFEDITORFACTORYWRAPPER_H
#define SBK_QTSIZEFEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtSizeFEditorFactoryWrapper : public QtSizeFEditorFactory
{
public:
    QtSizeFEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtSizeFPropertyManager * manager) { QtSizeFEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtSizeFPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtSizeFEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtSizeFEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtSizeFPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtSizeFPropertyManager * manager) { QtSizeFEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtSizeFPropertyManager * manager) override;
    ~QtSizeFEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTSIZEFEDITORFACTORYWRAPPER_H

