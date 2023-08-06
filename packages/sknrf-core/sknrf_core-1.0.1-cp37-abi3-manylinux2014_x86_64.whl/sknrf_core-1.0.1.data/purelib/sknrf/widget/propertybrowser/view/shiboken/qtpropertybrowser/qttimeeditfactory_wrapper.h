#ifndef SBK_QTTIMEEDITFACTORYWRAPPER_H
#define SBK_QTTIMEEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtTimeEditFactoryWrapper : public QtTimeEditFactory
{
public:
    QtTimeEditFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtTimePropertyManager * manager) { QtTimeEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtTimePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtTimePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtTimeEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtTimePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtTimePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtTimeEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtTimePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtTimePropertyManager * manager) { QtTimeEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtTimePropertyManager * manager) override;
    ~QtTimeEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTTIMEEDITFACTORYWRAPPER_H

