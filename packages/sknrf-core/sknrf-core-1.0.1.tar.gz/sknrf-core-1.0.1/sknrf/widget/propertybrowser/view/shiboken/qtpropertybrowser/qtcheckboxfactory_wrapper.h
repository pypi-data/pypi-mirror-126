#ifndef SBK_QTCHECKBOXFACTORYWRAPPER_H
#define SBK_QTCHECKBOXFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtCheckBoxFactoryWrapper : public QtCheckBoxFactory
{
public:
    QtCheckBoxFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtBoolPropertyManager * manager) { QtCheckBoxFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtBoolPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtCheckBoxFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtCheckBoxFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtBoolPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtBoolPropertyManager * manager) { QtCheckBoxFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtBoolPropertyManager * manager) override;
    ~QtCheckBoxFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTCHECKBOXFACTORYWRAPPER_H

