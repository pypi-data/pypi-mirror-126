#ifndef SBK_QTFILEEDITORFACTORYWRAPPER_H
#define SBK_QTFILEEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtFileEditorFactoryWrapper : public QtFileEditorFactory
{
public:
    QtFileEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtFilePropertyManager * manager) { QtFileEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtFilePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtFilePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtFileEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtFilePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtFilePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtFileEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtFilePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtFilePropertyManager * manager) { QtFileEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtFilePropertyManager * manager) override;
    ~QtFileEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTFILEEDITORFACTORYWRAPPER_H

