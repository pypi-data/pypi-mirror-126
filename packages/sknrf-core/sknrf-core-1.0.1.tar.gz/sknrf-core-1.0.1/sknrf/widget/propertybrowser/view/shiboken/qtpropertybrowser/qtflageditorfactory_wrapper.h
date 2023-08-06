#ifndef SBK_QTFLAGEDITORFACTORYWRAPPER_H
#define SBK_QTFLAGEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtFlagEditorFactoryWrapper : public QtFlagEditorFactory
{
public:
    QtFlagEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtFlagPropertyManager * manager) { QtFlagEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtFlagPropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtFlagEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent) { return QtFlagEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtFlagPropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtFlagPropertyManager * manager) { QtFlagEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtFlagPropertyManager * manager) override;
    ~QtFlagEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTFLAGEDITORFACTORYWRAPPER_H

