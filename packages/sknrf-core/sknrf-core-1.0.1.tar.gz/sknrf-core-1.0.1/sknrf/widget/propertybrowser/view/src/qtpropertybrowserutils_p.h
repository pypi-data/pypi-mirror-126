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


//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of Qt Designer.  This header
// file may change from version to version without notice, or even be removed.
//
// We mean it.
//

#ifndef QTPROPERTYBROWSERUTILS_H
#define QTPROPERTYBROWSERUTILS_H

#include "sknrfconfig.h"
#include <QMap>
#include <QIcon>
#include <QWidget>
#include <QStringList>
#include <QToolButton>
#include <QLineEdit>
#include <QFileDialog>

#include <complex>
#include <qvalidator.h>

#if QT_VERSION >= 0x040400
QT_BEGIN_NAMESPACE
#endif

#if defined(Q_OS_WIN)
#  if !defined(QT_QTPROPERTYBROWSER_EXPORT) && !defined(QT_QTPROPERTYBROWSER_IMPORT)
#    define QT_QTPROPERTYBROWSER_EXPORT
#  elif defined(QT_QTPROPERTYBROWSER_IMPORT)
#    if defined(QT_QTPROPERTYBROWSER_EXPORT)
#      undef QT_QTPROPERTYBROWSER_EXPORT
#    endif
#    define QT_QTPROPERTYBROWSER_EXPORT __declspec(dllimport)
#  elif defined(QT_QTPROPERTYBROWSER_EXPORT)
#    undef QT_QTPROPERTYBROWSER_EXPORT
#    define QT_QTPROPERTYBROWSER_EXPORT __declspec(dllexport)
#  endif
#else
#  define QT_QTPROPERTYBROWSER_EXPORT
#endif

extern double infinity;
extern double neg_infinity;
extern double highest;
extern double lowest;
extern double epsilon;

class QT_QTPROPERTYBROWSER_EXPORT QComplex : public std::complex<double>
{
public:
    QComplex(double re = 0.0, double im = 0.0);
    QComplex(std::complex<double> parent);
};

// Matches the Python isclose() function in PEP 0485 and Boost Weak Approach
template <class Value>
bool isclose(Value a, Value b, Value abs_tol, Value rel_tol)
{
    if (std::abs(a-b) <= std::max( rel_tol * std::max(std::abs(a), std::abs(b)), abs_tol))
        return true;
    else
        return false;
}
bool isclose(QComplex a, QComplex b, double abs_tol, double rel_tol);
bool isclose(QVector<QComplex> a, QVector<QComplex> b, QVector<double> abs_tol, QVector<double> rel_tol);
bool isclose(QDate a, QDate b, QDate abs_tol, QDate rel_tol);
bool isclose(QSize a, QSize b, QSize abs_tol, QSize rel_tol);
bool isclose(QPointF a, QPointF b, QPointF abs_tol, QPointF rel_tol);
bool isclose(QSizeF a, QSizeF b, QSizeF abs_tol, QSizeF rel_tol);
bool isclose(QRectF a, QRectF b, QRectF abs_tol, QRectF rel_tol);

class QMouseEvent;
class QCheckBox;
class QLineEdit;

QString double2str(double val, int precision);

enum Format
{
    RE,
    RE_IM,
    LIN_DEG,
    LOG_DEG
};
extern QMap<Format, QString> FormatNameMap;

enum Scale {
    T,
    G,
    M,
    K,
    _,
    m,
    u,
    n,
    p,
};
extern QMap<Scale, QString> ScaleNameMap;
extern QMap<Scale, int> ScaleValueMap;

enum PkAvg
{
    PK,
    AVG
};
extern QMap<PkAvg, QString> PkAvgNameMap;

enum Domain
{
    TF,
    FF,
    FT,
    TT,
    TH,
};
extern QMap<Domain, QString> DomainNameMap;


enum BrowserCol
{
    NONE,
    UNIT,
    PKAVG,
    FORMAT,
    MINIMUM,
    MAXIMUM,
    CHECK
};
extern QMap<BrowserCol, QString> AttributeNameMap;

class QIntEditPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QIntEdit : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QIntEdit(QWidget *parent = nullptr);
    ~QIntEdit();

    int value() const;
    double minimum() const;
    double maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

public Q_SLOTS:
    void setValue();
    void setValue(int val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);

Q_SIGNALS:
    void valueChanged(int val);
    void destroyed(QObject *obj);

protected:
    void paintEvent(QPaintEvent *);

private:
    QIntEditPrivate *d_ptr;
    Q_DISABLE_COPY(QIntEdit)
    Q_DECLARE_PRIVATE(QIntEdit)

public:
    static QString num2str(int val, const Scale scale, const Format format, int precision);
    static int str2num(const QString &text, const Scale scale, const Format format);
};


class QDoubleEditPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QDoubleEdit : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:

    explicit QDoubleEdit(QWidget *parent = nullptr);
    ~QDoubleEdit();

    double value() const;
    double minimum() const;
    double maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

    public Q_SLOTS:
    void setValue();
    void setValue(double val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);

Q_SIGNALS:
    void valueChanged(double val);
    void destroyed(QObject *obj);

protected:
    void paintEvent(QPaintEvent *);

private:
    QDoubleEditPrivate *d_ptr;
    Q_DISABLE_COPY(QDoubleEdit)
    Q_DECLARE_PRIVATE(QDoubleEdit)

public:
    static QString num2str(double val, const Scale scale, const Format format, int precision);
    static double str2num(const QString &text, const Scale scale, const Format format);
};

class QComplexEditPrivate;

class QT_QTPROPERTYBROWSER_EXPORT QComplexEdit : public QWidget
{
    Q_OBJECT
    Q_ENUMS(Format)
public:
    explicit QComplexEdit(QWidget *parent = nullptr);
    ~QComplexEdit();

    QComplex value() const;
    double minimum() const;
    double maximum() const;
    int precision() const;
    Scale scale() const;
    Format format() const;

    QValidator::State validate(QString &input, int &pos) const;
    bool eventFilter(QObject *obj, QEvent *ev);

    public Q_SLOTS:
    void setValue();
    void setValue(const QComplex &val);
    void setMinimum(double min);
    void setMaximum(double max);
    void setRange(double min, double max);
    void setPrecision(int);
    void setScale(Scale);
    void setFormat(Format);
    void setReadOnly(bool readOnly);

Q_SIGNALS:
    void valueChanged(const QComplex &val);
    void destroyed(QObject *obj);

protected:
    void paintEvent(QPaintEvent *);

private:
    QComplexEditPrivate *d_ptr;
    Q_DISABLE_COPY(QComplexEdit)
    Q_DECLARE_PRIVATE(QComplexEdit)

public:
    static QString num2str(const QComplex &val, const Scale scale, const Format format, int precision);
    static QComplex str2num(const QString &text, const Scale scale, const Format format);
};

class QFileEdit : public QWidget {
    Q_OBJECT

public:
    QFileEdit(QWidget *parent);
    ~QFileEdit();

    bool eventFilter(QObject *obj, QEvent *ev);

    bool fileExists(QString path) const;
    bool validExtension(QString path) const;

    public Q_SLOTS:
    void setValue(const QString &value);
    void setFilter(const QString &filter);
    void setFileMode(const QFileDialog::FileMode mode);
    void setReadOnly(const bool readOnly);

Q_SIGNALS:
    void valueChanged(const QString &value);
    void destroyed(QObject *obj);
protected:
    void paintEvent(QPaintEvent *);

private Q_SLOTS:
    void slotEditFinished();
    void slotButtonClicked();

private:
    QString m_fileName;
    QString m_filter;
    QFileDialog::FileMode m_fileMode;
    bool m_readOnly;
    QLineEdit *m_edit;
    QToolButton *m_button;
};

class QtCursorDatabase
{
public:
    QtCursorDatabase();
    void clear();

    QStringList cursorShapeNames() const;
    QMap<int, QIcon> cursorShapeIcons() const;
    QString cursorToShapeName(const QCursor &cursor) const;
    QIcon cursorToShapeIcon(const QCursor &cursor) const;
    int cursorToValue(const QCursor &cursor) const;
#ifndef QT_NO_CURSOR
    QCursor valueToCursor(int value) const;
#endif
private:
    void appendCursor(Qt::CursorShape shape, const QString &name, const QIcon &icon);
    QStringList m_cursorNames;
    QMap<int, QIcon> m_cursorIcons;
    QMap<int, Qt::CursorShape> m_valueToCursorShape;
    QMap<Qt::CursorShape, int> m_cursorShapeToValue;
};

class QtPropertyBrowserUtils
{
public:
    static QPixmap brushValuePixmap(const QBrush &b);
    static QIcon brushValueIcon(const QBrush &b);
    static QString colorValueText(const QColor &c);
    static QPixmap fontValuePixmap(const QFont &f);
    static QIcon fontValueIcon(const QFont &f);
    static QString fontValueText(const QFont &f);
};

class QtBoolEdit : public QWidget {
    Q_OBJECT
public:
    QtBoolEdit(QWidget *parent = nullptr);

    bool textVisible() const { return m_textVisible; }
    void setTextVisible(bool textVisible);

    Qt::CheckState checkState() const;
    void setCheckState(Qt::CheckState state);

    bool isChecked() const;
    void setChecked(bool c);

    bool blockCheckBoxSignals(bool block);

Q_SIGNALS:
    void toggled(bool);

protected:
    void mousePressEvent(QMouseEvent * event);
    void paintEvent(QPaintEvent *);

private:
    QCheckBox *m_checkBox;
    bool m_textVisible;
};

class QtKeySequenceEdit : public QWidget
{
    Q_OBJECT
public:
    QtKeySequenceEdit(QWidget *parent = nullptr);

    QKeySequence keySequence() const;
    bool eventFilter(QObject *o, QEvent *e);
public Q_SLOTS:
    void setKeySequence(const QKeySequence &sequence);
Q_SIGNALS:
    void keySequenceChanged(const QKeySequence &sequence);
protected:
    void focusInEvent(QFocusEvent *e);
    void focusOutEvent(QFocusEvent *e);
    void keyPressEvent(QKeyEvent *e);
    void keyReleaseEvent(QKeyEvent *e);
    void paintEvent(QPaintEvent *);
    bool event(QEvent *e);
private slots:
    void slotClearShortcut();
private:
    void handleKeyEvent(QKeyEvent *e);
    int translateModifiers(Qt::KeyboardModifiers state, const QString &text) const;

    int m_num;
    QKeySequence m_keySequence;
    QLineEdit *m_lineEdit;
};

#if QT_VERSION >= 0x040400
QT_END_NAMESPACE
#endif

#endif
