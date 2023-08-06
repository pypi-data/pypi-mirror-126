/****************************************************************************
**
** Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt Solutions component.
**
** $QT_BEGIN_LICENSE:BSD$
** You may use this file under the terms of the BSD license as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
**     of its contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/


#ifndef QTEDITORFACTORY_H
#define QTEDITORFACTORY_H

#include "qtpropertybrowser.h"
#include "qtpropertymanager.h"

#if QT_VERSION >= 0x040400
QT_BEGIN_NAMESPACE
#endif

class QtGroupEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtGroupEditorFactory : public QtAbstractEditorFactory<QtGroupPropertyManager>
{
    Q_OBJECT
public:
    QtGroupEditorFactory(QObject *parent = nullptr);
    ~QtGroupEditorFactory();
protected:
    void connectPropertyManager(QtGroupPropertyManager *manager);
    QWidget *createEditor(QtGroupPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtGroupPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtGroupPropertyManager *manager);
private:
    QtGroupEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtGroupEditorFactory)
    Q_DISABLE_COPY(QtGroupEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSpinBoxFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtSpinBoxFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtSpinBoxFactory(QObject *parent = nullptr);
    ~QtSpinBoxFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
private:
    QtSpinBoxFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtSpinBoxFactory)
    Q_DISABLE_COPY(QtSpinBoxFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtIntEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtIntEditFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtIntEditFactory(QObject *parent = nullptr);
    ~QtIntEditFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
private:
    QtIntEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtIntEditFactory)
    Q_DISABLE_COPY(QtIntEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSliderFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtSliderFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtSliderFactory(QObject *parent = nullptr);
    ~QtSliderFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
private:
    QtSliderFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtSliderFactory)
    Q_DISABLE_COPY(QtSliderFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtScrollBarFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtScrollBarFactory : public QtAbstractEditorFactory<QtIntPropertyManager>
{
    Q_OBJECT
public:
    QtScrollBarFactory(QObject *parent = nullptr);
    ~QtScrollBarFactory();
protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditor(QtIntPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtIntPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
private:
    QtScrollBarFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtScrollBarFactory)
    Q_DISABLE_COPY(QtScrollBarFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, int, int))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtCheckBoxFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtCheckBoxFactory : public QtAbstractEditorFactory<QtBoolPropertyManager>
{
    Q_OBJECT
public:
    QtCheckBoxFactory(QObject *parent = nullptr);
    ~QtCheckBoxFactory();
protected:
    void connectPropertyManager(QtBoolPropertyManager *manager);
    QWidget *createEditor(QtBoolPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtBoolPropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtBoolPropertyManager *manager);
private:
    QtCheckBoxFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtCheckBoxFactory)
    Q_DISABLE_COPY(QtCheckBoxFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotTextVisibleChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDoubleSpinBoxFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtDoubleSpinBoxFactory : public QtAbstractEditorFactory<QtDoublePropertyManager>
{
    Q_OBJECT
public:
    QtDoubleSpinBoxFactory(QObject *parent = nullptr);
    ~QtDoubleSpinBoxFactory();
protected:
    void connectPropertyManager(QtDoublePropertyManager *manager);
    QWidget *createEditor(QtDoublePropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtDoublePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtDoublePropertyManager *manager);
private:
    QtDoubleSpinBoxFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtDoubleSpinBoxFactory)
    Q_DISABLE_COPY(QtDoubleSpinBoxFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotSingleStepChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDoubleEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtDoubleEditFactory : public QtAbstractEditorFactory<QtDoublePropertyManager>
{
    Q_OBJECT
public:
    QtDoubleEditFactory(QObject *parent = nullptr);
    ~QtDoubleEditFactory();
protected:
    void connectPropertyManager(QtDoublePropertyManager *manager);
    QWidget *createEditor(QtDoublePropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtDoublePropertyManager *manager, QtProperty *property,
                                   QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtDoublePropertyManager *manager);
private:
    QtDoubleEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtDoubleEditFactory)
    Q_DISABLE_COPY(QtDoubleEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, double))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtComplexEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtComplexEditFactory : public QtAbstractEditorFactory<QtComplexPropertyManager>
{
    Q_OBJECT
public:
    QtComplexEditFactory(QObject *parent = nullptr);
    ~QtComplexEditFactory();
protected:
    void connectPropertyManager(QtComplexPropertyManager *manager);
    QWidget *createEditor(QtComplexPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtComplexPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtComplexPropertyManager *manager);
private:
    QtComplexEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtComplexEditFactory)
    Q_DISABLE_COPY(QtComplexEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *, double, double))
    Q_PRIVATE_SLOT(d_func(), void slotPrecisionChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QComplex&))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetPkAvg(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetMinimum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetMaximum(double))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
    friend class QtTFTensorEditFactoryPrivate;
};

class QtTFTensorEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtTFTensorEditFactory : public QtAbstractEditorFactory<QtTFTensorPropertyManager>
{
    Q_OBJECT
public:
    QtTFTensorEditFactory(QObject *parent = nullptr);
    ~QtTFTensorEditFactory();
protected:
    void connectPropertyManager(QtTFTensorPropertyManager *manager);
    QWidget *createEditor(QtTFTensorPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtTFTensorPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtTFTensorPropertyManager *manager);
    QtComplexEditFactory* subFactory() const;
    void setSubFactory(QtComplexEditFactory* subFactory);
private:
    QtTFTensorEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtTFTensorEditFactory)
    Q_DISABLE_COPY(QtTFTensorEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QVector<QComplex>& value))
    Q_PRIVATE_SLOT(d_func(), void slotSetScale(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetPkAvg(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetFormat(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotUnitAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotPkAvgAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotFormatAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMinimumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotMaximumAttributeEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtLineEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtLineEditFactory : public QtAbstractEditorFactory<QtStringPropertyManager>
{
    Q_OBJECT
public:
    QtLineEditFactory(QObject *parent = nullptr);
    ~QtLineEditFactory();
protected:
    void connectPropertyManager(QtStringPropertyManager *manager);
    QWidget *createEditor(QtStringPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtStringPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtStringPropertyManager *manager);
private:
    QtLineEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtLineEditFactory)
    Q_DISABLE_COPY(QtLineEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotRegExpChanged(QtProperty *, const QRegExp &))
    Q_PRIVATE_SLOT(d_func(), void slotEchoModeChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDateEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtDateEditFactory : public QtAbstractEditorFactory<QtDatePropertyManager>
{
    Q_OBJECT
public:
    QtDateEditFactory(QObject *parent = nullptr);
    ~QtDateEditFactory();
protected:
    void connectPropertyManager(QtDatePropertyManager *manager);
    QWidget *createEditor(QtDatePropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtDatePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtDatePropertyManager *manager);
private:
    QtDateEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtDateEditFactory)
    Q_DISABLE_COPY(QtDateEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QDate &))
    Q_PRIVATE_SLOT(d_func(), void slotRangeChanged(QtProperty *,
                        const QDate &, const QDate &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QDate &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtTimeEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtTimeEditFactory : public QtAbstractEditorFactory<QtTimePropertyManager>
{
    Q_OBJECT
public:
    QtTimeEditFactory(QObject *parent = nullptr);
    ~QtTimeEditFactory();
protected:
    void connectPropertyManager(QtTimePropertyManager *manager);
    QWidget *createEditor(QtTimePropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtTimePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtTimePropertyManager *manager);
private:
    QtTimeEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtTimeEditFactory)
    Q_DISABLE_COPY(QtTimeEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QTime &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QTime &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtDateTimeEditFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtDateTimeEditFactory : public QtAbstractEditorFactory<QtDateTimePropertyManager>
{
    Q_OBJECT
public:
    QtDateTimeEditFactory(QObject *parent = nullptr);
    ~QtDateTimeEditFactory();
protected:
    void connectPropertyManager(QtDateTimePropertyManager *manager);
    QWidget *createEditor(QtDateTimePropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtDateTimePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtDateTimePropertyManager *manager);
private:
    QtDateTimeEditFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtDateTimeEditFactory)
    Q_DISABLE_COPY(QtDateTimeEditFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QDateTime &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QDateTime &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtKeySequenceEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtKeySequenceEditorFactory : public QtAbstractEditorFactory<QtKeySequencePropertyManager>
{
    Q_OBJECT
public:
    QtKeySequenceEditorFactory(QObject *parent = nullptr);
    ~QtKeySequenceEditorFactory();
protected:
    void connectPropertyManager(QtKeySequencePropertyManager *manager);
    QWidget *createEditor(QtKeySequencePropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtKeySequencePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtKeySequencePropertyManager *manager);
private:
    QtKeySequenceEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtKeySequenceEditorFactory)
    Q_DISABLE_COPY(QtKeySequenceEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QKeySequence &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QKeySequence &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtCharEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtCharEditorFactory : public QtAbstractEditorFactory<QtCharPropertyManager>
{
    Q_OBJECT
public:
    QtCharEditorFactory(QObject *parent = nullptr);
    ~QtCharEditorFactory();
protected:
    void connectPropertyManager(QtCharPropertyManager *manager);
    QWidget *createEditor(QtCharPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtCharPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtCharPropertyManager *manager);
private:
    QtCharEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtCharEditorFactory)
    Q_DISABLE_COPY(QtCharEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QChar &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QChar &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtLocaleEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtLocaleEditorFactory : public QtAbstractEditorFactory<QtLocalePropertyManager>
{
    Q_OBJECT
public:
    QtLocaleEditorFactory(QObject *parent = nullptr);
    ~QtLocaleEditorFactory();
protected:
    void connectPropertyManager(QtLocalePropertyManager *manager);
    QWidget *createEditor(QtLocalePropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtLocalePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtLocalePropertyManager *manager);
private:
    QtLocaleEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtLocaleEditorFactory)
    Q_DISABLE_COPY(QtLocaleEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtPointEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtPointEditorFactory : public QtAbstractEditorFactory<QtPointPropertyManager>
{
    Q_OBJECT
public:
    QtPointEditorFactory(QObject *parent = nullptr);
    ~QtPointEditorFactory();
protected:
    void connectPropertyManager(QtPointPropertyManager *manager);
    QWidget *createEditor(QtPointPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtPointPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtPointPropertyManager *manager);
private:
    QtPointEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtPointEditorFactory)
    Q_DISABLE_COPY(QtPointEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtPointFEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtPointFEditorFactory : public QtAbstractEditorFactory<QtPointFPropertyManager>
{
    Q_OBJECT
public:
    QtPointFEditorFactory(QObject *parent = nullptr);
    ~QtPointFEditorFactory();
protected:
    void connectPropertyManager(QtPointFPropertyManager *manager);
    QWidget *createEditor(QtPointFPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtPointFPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtPointFPropertyManager *manager);
private:
    QtPointFEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtPointFEditorFactory)
    Q_DISABLE_COPY(QtPointFEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSizeEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtSizeEditorFactory : public QtAbstractEditorFactory<QtSizePropertyManager>
{
    Q_OBJECT
public:
    QtSizeEditorFactory(QObject *parent = nullptr);
    ~QtSizeEditorFactory();
protected:
    void connectPropertyManager(QtSizePropertyManager *manager);
    QWidget *createEditor(QtSizePropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtSizePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtSizePropertyManager *manager);
private:
    QtSizeEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtSizeEditorFactory)
    Q_DISABLE_COPY(QtSizeEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSizeFEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtSizeFEditorFactory : public QtAbstractEditorFactory<QtSizeFPropertyManager>
{
    Q_OBJECT
public:
    QtSizeFEditorFactory(QObject *parent = nullptr);
    ~QtSizeFEditorFactory();
protected:
    void connectPropertyManager(QtSizeFPropertyManager *manager);
    QWidget *createEditor(QtSizeFPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtSizeFPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtSizeFPropertyManager *manager);
private:
    QtSizeFEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtSizeFEditorFactory)
    Q_DISABLE_COPY(QtSizeFEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtRectEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtRectEditorFactory : public QtAbstractEditorFactory<QtRectPropertyManager>
{
    Q_OBJECT
public:
    QtRectEditorFactory(QObject *parent = nullptr);
    ~QtRectEditorFactory();
protected:
    void connectPropertyManager(QtRectPropertyManager *manager);
    QWidget *createEditor(QtRectPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtRectPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtRectPropertyManager *manager);
private:
    QtRectEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtRectEditorFactory)
    Q_DISABLE_COPY(QtRectEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtRectFEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtRectFEditorFactory : public QtAbstractEditorFactory<QtRectFPropertyManager>
{
    Q_OBJECT
public:
    QtRectFEditorFactory(QObject *parent = nullptr);
    ~QtRectFEditorFactory();
protected:
    void connectPropertyManager(QtRectFPropertyManager *manager);
    QWidget *createEditor(QtRectFPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtRectFPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtRectFPropertyManager *manager);
private:
    QtRectFEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtRectFEditorFactory)
    Q_DISABLE_COPY(QtRectFEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtEnumEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtEnumEditorFactory : public QtAbstractEditorFactory<QtEnumPropertyManager>
{
    Q_OBJECT
public:
    QtEnumEditorFactory(QObject *parent = nullptr);
    ~QtEnumEditorFactory();
protected:
    void connectPropertyManager(QtEnumPropertyManager *manager);
    QWidget *createEditor(QtEnumPropertyManager *manager, QtProperty *property, QWidget *parent);
    QWidget *createAttributeEditor(QtEnumPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtEnumPropertyManager *manager);
private:
    QtEnumEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtEnumEditorFactory)
    Q_DISABLE_COPY(QtEnumEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotEnumNamesChanged(QtProperty *,
                        const QStringList &))
    Q_PRIVATE_SLOT(d_func(), void slotEnumIconsChanged(QtProperty *,
                        const QMap<int, QIcon> &))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(int))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtFlagEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtFlagEditorFactory : public QtAbstractEditorFactory<QtFlagPropertyManager>
{
    Q_OBJECT
public:
    QtFlagEditorFactory(QObject *parent = nullptr);
    ~QtFlagEditorFactory();
protected:
    void connectPropertyManager(QtFlagPropertyManager *manager);
    QWidget *createEditor(QtFlagPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtFlagPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtFlagPropertyManager *manager);
private:
    QtFlagEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtFlagEditorFactory)
    Q_DISABLE_COPY(QtFlagEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtSizePolicyEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtSizePolicyEditorFactory : public QtAbstractEditorFactory<QtSizePolicyPropertyManager>
{
    Q_OBJECT
public:
    QtSizePolicyEditorFactory(QObject *parent = nullptr);
    ~QtSizePolicyEditorFactory();
protected:
    void connectPropertyManager(QtSizePolicyPropertyManager *manager);
    QWidget *createEditor(QtSizePolicyPropertyManager *manager, QtProperty *property,
                          QWidget *parent);
    QWidget *createAttributeEditor(QtSizePolicyPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtSizePolicyPropertyManager *manager);
private:
    QtSizePolicyEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtSizePolicyEditorFactory)
    Q_DISABLE_COPY(QtSizePolicyEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtCursorEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtCursorEditorFactory : public QtAbstractEditorFactory<QtCursorPropertyManager>
{
    Q_OBJECT
public:
    QtCursorEditorFactory(QObject *parent = nullptr);
    ~QtCursorEditorFactory();
protected:
    void connectPropertyManager(QtCursorPropertyManager *manager);
    QWidget *createEditor(QtCursorPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtCursorPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtCursorPropertyManager *manager);
private:
    QtCursorEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtCursorEditorFactory)
    Q_DISABLE_COPY(QtCursorEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QCursor &))
    Q_PRIVATE_SLOT(d_func(), void slotEnumChanged(QtProperty *, int))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtColorEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtColorEditorFactory : public QtAbstractEditorFactory<QtColorPropertyManager>
{
    Q_OBJECT
public:
    QtColorEditorFactory(QObject *parent = nullptr);
    ~QtColorEditorFactory();
protected:
    void connectPropertyManager(QtColorPropertyManager *manager);
    QWidget *createEditor(QtColorPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtColorPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtColorPropertyManager *manager);
private:
    QtColorEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtColorEditorFactory)
    Q_DISABLE_COPY(QtColorEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QColor &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QColor &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtFontEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtFontEditorFactory : public QtAbstractEditorFactory<QtFontPropertyManager>
{
    Q_OBJECT
public:
    QtFontEditorFactory(QObject *parent = nullptr);
    ~QtFontEditorFactory();
protected:
    void connectPropertyManager(QtFontPropertyManager *manager);
    QWidget *createEditor(QtFontPropertyManager *manager, QtProperty *property,
                QWidget *parent);
    QWidget *createAttributeEditor(QtFontPropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtFontPropertyManager *manager);
private:
    QtFontEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtFontEditorFactory)
    Q_DISABLE_COPY(QtFontEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QFont &))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QFont &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

class QtFileEditorFactoryPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QtFileEditorFactory: public QtAbstractEditorFactory<QtFilePropertyManager>
{
    Q_OBJECT
public:
    QtFileEditorFactory(QObject *parent = nullptr);
    ~QtFileEditorFactory();
protected:
    void connectPropertyManager(QtFilePropertyManager *manager);
    QWidget *createEditor(QtFilePropertyManager *manager, QtProperty *property, QWidget *parent);
    QWidget *createAttributeEditor(QtFilePropertyManager *manager, QtProperty *property, QWidget *parent, BrowserCol attribute);
    void disconnectPropertyManager(QtFilePropertyManager *manager);
private:
    QtFileEditorFactoryPrivate *d_ptr;
    Q_DECLARE_PRIVATE(QtFileEditorFactory)
    Q_DISABLE_COPY(QtFileEditorFactory)
    Q_PRIVATE_SLOT(d_func(), void slotPropertyChanged(QtProperty *, const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotFilterChanged(QtProperty *, const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotReadOnlyChanged(QtProperty *, bool))
    Q_PRIVATE_SLOT(d_func(), void slotEditorDestroyed(QObject *))
    Q_PRIVATE_SLOT(d_func(), void slotSetValue(const QString &))
    Q_PRIVATE_SLOT(d_func(), void slotSetCheck(bool))
    Q_PRIVATE_SLOT(d_func(), void slotCheckAttributeEditorDestroyed(QObject *))
};

#if QT_VERSION >= 0x040400
QT_END_NAMESPACE
#endif

#endif
