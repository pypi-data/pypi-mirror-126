#ifndef SBK_QTSCROLLBARFACTORYWRAPPER_H
#define SBK_QTSCROLLBARFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtScrollBarFactoryWrapper : public QtScrollBarFactory
{
public:
    QtScrollBarFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtIntPropertyManager * manager) { QtScrollBarFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtIntPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtScrollBarFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtScrollBarFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtIntPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtIntPropertyManager * manager) { QtScrollBarFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtIntPropertyManager * manager) override;
    ~QtScrollBarFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTSCROLLBARFACTORYWRAPPER_H

