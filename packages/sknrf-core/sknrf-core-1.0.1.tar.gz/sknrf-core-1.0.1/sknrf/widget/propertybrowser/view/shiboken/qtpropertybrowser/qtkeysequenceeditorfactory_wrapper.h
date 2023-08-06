#ifndef SBK_QTKEYSEQUENCEEDITORFACTORYWRAPPER_H
#define SBK_QTKEYSEQUENCEEDITORFACTORYWRAPPER_H

#include <qteditorfactory.h>

class QtKeySequenceEditorFactoryWrapper : public QtKeySequenceEditorFactory
{
public:
    QtKeySequenceEditorFactoryWrapper(QObject * parent = nullptr);
    inline void connectPropertyManager_protected(QtKeySequencePropertyManager * manager) { QtKeySequenceEditorFactory::connectPropertyManager(manager); }
    void connectPropertyManager(QtKeySequencePropertyManager * manager) override;
    inline QWidget * createAttributeEditor_protected(QtKeySequencePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtKeySequenceEditorFactory::createAttributeEditor(manager, property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtKeySequencePropertyManager * manager, QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtKeySequencePropertyManager * manager, QtProperty * property, QWidget * parent) { return QtKeySequenceEditorFactory::createEditor(manager, property, parent); }
    QWidget * createEditor(QtKeySequencePropertyManager * manager, QtProperty * property, QWidget * parent) override;
    inline void disconnectPropertyManager_protected(QtKeySequencePropertyManager * manager) { QtKeySequenceEditorFactory::disconnectPropertyManager(manager); }
    void disconnectPropertyManager(QtKeySequencePropertyManager * manager) override;
    ~QtKeySequenceEditorFactoryWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTKEYSEQUENCEEDITORFACTORYWRAPPER_H

