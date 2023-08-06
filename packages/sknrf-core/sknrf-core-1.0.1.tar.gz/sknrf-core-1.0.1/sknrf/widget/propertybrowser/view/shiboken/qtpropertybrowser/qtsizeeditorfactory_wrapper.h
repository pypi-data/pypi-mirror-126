#ifndef SBK_QTSIZEEDITORFACTORYWRAPPER_H
#define SBK_QTSIZEEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtSizeEditorFactoryWrapper : public QtSizeEditorFactory
{
public:
    QtSizeEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtSizePropertyManager * manager) { QtSizeEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtSizePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtSizePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtSizeEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtSizePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtSizePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtSizeEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtSizePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtSizePropertyManager * manager) { QtSizeEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtSizePropertyManager * manager) override;
    ~QtSizeEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTSIZEEDITORFACTORYWRAPPER_H

