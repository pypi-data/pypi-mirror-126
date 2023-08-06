#ifndef SBK_QTDOUBLEEDITFACTORYWRAPPER_H
#define SBK_QTDOUBLEEDITFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtDoubleEditFactoryWrapper : public QtDoubleEditFactory
{
public:
    QtDoubleEditFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtDoublePropertyManager * manager) { QtDoubleEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtDoublePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtDoubleEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtDoubleEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtDoublePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtDoublePropertyManager * manager) { QtDoubleEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtDoublePropertyManager * manager) override;
    ~QtDoubleEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTDOUBLEEDITFACTORYWRAPPER_H

