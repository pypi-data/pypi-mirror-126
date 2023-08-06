#ifndef SBK_QTRECTEDITORFACTORYWRAPPER_H
#define SBK_QTRECTEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtRectEditorFactoryWrapper : public QtRectEditorFactory
{
public:
    QtRectEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtRectPropertyManager * manager) { QtRectEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtRectPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtRectPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtRectEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtRectPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtRectPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtRectEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtRectPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtRectPropertyManager * manager) { QtRectEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtRectPropertyManager * manager) override;
    ~QtRectEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTRECTEDITORFACTORYWRAPPER_H

