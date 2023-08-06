#ifndef SBK_QTTFTENSOREDITFACTORYWRAPPER_H
#define SBK_QTTFTENSOREDITFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtTFTensorEditFactoryWrapper : public QtTFTensorEditFactory
{
public:
    QtTFTensorEditFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtTFTensorPropertyManager * manager) { QtTFTensorEditFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtTFTensorPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtTFTensorPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtTFTensorEditFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtTFTensorPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtTFTensorPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtTFTensorEditFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtTFTensorPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtTFTensorPropertyManager * manager) { QtTFTensorEditFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtTFTensorPropertyManager * manager) override;
    inline void setSubFactory_protected(QtComplexEditFactory * subFactory) { QtTFTensorEditFactory::setSubFactory(subFactory); }
    inline QtComplexEditFactory * subFactory_protected() const { return QtTFTensorEditFactory::subFactory(); }
    ~QtTFTensorEditFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTTFTENSOREDITFACTORYWRAPPER_H

