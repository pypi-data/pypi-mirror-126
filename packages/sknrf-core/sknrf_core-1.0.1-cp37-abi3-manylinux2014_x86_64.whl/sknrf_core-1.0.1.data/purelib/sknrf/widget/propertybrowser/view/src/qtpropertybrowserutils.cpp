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

#include "qtpropertybrowserutils_p.h"

#include <QApplication>
#include <QPainter>
#include <QHBoxLayout>
#include <QMouseEvent>
#include <QCheckBox>
#include <QLineEdit>
#include <QMenu>
#include <QStyleOption>
#include <QSpinBox>
#include <QScrollBar>
#include <QComboBox>
#include <QAbstractItemView>
#include <QLineEdit>
#include <QDateTimeEdit>
#include <QHBoxLayout>
#include <QMenu>
#include <QKeyEvent>
#include <QApplication>
#include <QLabel>
#include <QToolButton>
#include <QColorDialog>
#include <QFontDialog>
#include <QFileDialog>
#include <QSpacerItem>
#include <QStyleOption>
#include <QPainter>
#include <QMap>

#include <cmath>
#include <float.h>
#include <complex>
#include <stdio.h>

#if QT_VERSION >= 0x040400
QT_BEGIN_NAMESPACE
#endif

#ifdef Q_CC_MSVC
    #define isnan(x) _isnan(x)
    #define isinfinite(x) (!_finite(x) && !isnan(x))
    #define fpu_error(x) (isinf(x) || isnan(x))
#else
    #define isnan(x) std::isnan(x)
    #define isinfinite(x) std::isinf(x)
    #define fpu_error(x) (isinf(x) || isnan(x))
#endif

QT_BEGIN_NAMESPACE

double infinity(std::numeric_limits<double>::infinity());
double neg_infinity(-std::numeric_limits<double>::infinity());
double highest(std::numeric_limits<double>::max());
double lowest(-std::numeric_limits<double>::max());
double epsilon(std::numeric_limits<double>::epsilon());

bool isclose(QComplex a, QComplex b, double abs_tol, double rel_tol)
{
    if (std::abs(a-b) <= std::max( rel_tol * std::max(std::abs(a), std::abs(b)), abs_tol))
        return true;
    else
        return false;
}

bool isclose(QVector<QComplex> a, QVector<QComplex> b, QVector<double> abs_tol, QVector<double> rel_tol)
{
    for (unsigned short index=0; index < a.size(); index++) {
        if (!(std::abs(a[index]-b[index]) <= std::max(rel_tol[index] * std::max(std::abs(a[index]), std::abs(b[index])), abs_tol[index])))
            return false;
    }
    return true;
}

bool isclose(QDate a, QDate b, QDate abs_tol, QDate rel_tol)
{
    Q_UNUSED(abs_tol);
    Q_UNUSED(rel_tol);
    return a == b;
}

bool isclose(QSize a, QSize b, QSize abs_tol, QSize rel_tol)
{
    return (isclose(a.width(), b.width(), abs_tol.width(), rel_tol.width()) &&
            isclose(a.height(), b.height(), abs_tol.height(), rel_tol.height()));
}

bool isclose(QPointF a, QPointF b, QPointF abs_tol, QPointF rel_tol)
{
    return (isclose(a.x(), b.x(), abs_tol.x(), rel_tol.x()) &&
            isclose(a.y(), b.y(), abs_tol.y(), rel_tol.y()));
}

bool isclose(QSizeF a, QSizeF b, QSizeF abs_tol, QSizeF rel_tol)
{
    return (isclose(a.width(), b.width(), abs_tol.width(), rel_tol.width()) &&
            isclose(a.height(), b.height(), abs_tol.height(), rel_tol.height()));
}

bool isclose(QRectF a, QRectF b, QRectF abs_tol, QRectF rel_tol)
{
    return (isclose(a.x(), b.x(), abs_tol.x(), rel_tol.x()) &&
            isclose(a.y(), b.y(), abs_tol.y(), rel_tol.y()) &&
            isclose(a.width(), b.width(), abs_tol.width(), rel_tol.width()) &&
            isclose(a.height(), b.height(), abs_tol.height(), rel_tol.height()));
}

QMap<Format, QString> FormatNameMap = {
    {Format::RE, "Re"},
    {Format::RE_IM, "Re+Imj"},
    {Format::LIN_DEG, QString("Lin") + QString(QChar(0x2220)) + QString("Deg")},
    {Format::LOG_DEG, QString("Log") + QString(QChar(0x2220)) + QString("Deg")}
};

QMap<Scale, QString> ScaleNameMap = {
    {Scale::T, "T"},
    {Scale::G, "G"},
    {Scale::M, "M"},
    {Scale::K, "K"},
    {Scale::_, " "},
    {Scale::m, "m"},
    {Scale::u, "u"},
    {Scale::n, "n"},
    {Scale::p, "p"},
};
QMap<Scale, int> ScaleValueMap = {
    {Scale::T, 12},
    {Scale::G, 9},
    {Scale::M, 6},
    {Scale::K, 3},
    {Scale::_, 0},
    {Scale::m, -3},
    {Scale::u, -6},
    {Scale::n, -9},
    {Scale::p, -12},
};

QMap<PkAvg, QString> PkAvgNameMap = {
    {PkAvg::PK, "pk"},
    {PkAvg::AVG, "avg"},
};
QMap<Domain, QString> DomainNameMap = {
    {Domain::TF, "TF"},
    {Domain::FF, "FF"},
    {Domain::FT, "FT"},
    {Domain::TT, "TT"},
    {Domain::TH, "TH"},
};
QMap<BrowserCol, QString> AttributeNameMap = {
    {BrowserCol::UNIT, "Unit"},
    {BrowserCol::PKAVG, "PkAvg"},
    {BrowserCol::FORMAT, "Format"},
    {BrowserCol::MINIMUM, "Minimum"},
    {BrowserCol::MAXIMUM, "Maximum"},
};

const QRegExp regExps[4] = {
    QRegExp("\\s*([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+|inf)(?:[eE][+-]?[0-9]+)?).*"),
    QRegExp("\\s*([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+|inf)(?:[eE][+-]?[0-9]+)?)?\\s*([+-]?)\\s*(?:([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+|inf)(?:[eE][+-]?[0-9]+)?)[JjIi])?.*"),
    QRegExp("\\s*([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+|inf)(?:[eE][+-]?[0-9]+)?)(\\s*[<\\x2220]\\s*)?([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+)(?:[eE][+-]?[0-9]+)?)?.*"),
    QRegExp("\\s*([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+|inf)(?:[eE][+-]?[0-9]+)?)(\\s*[<\\x2220]\\s*)?([+-]?(?:(?:\\d+(?:\\.\\d*)?)|\\.\\d+)(?:[eE][+-]?[0-9]+)?)?.*")};

// Set a hard coded left margin to account for the indentation
// of the tree view icon when switching to an editor
static inline void setupTreeViewEditorMargin(QLayout *lt)
{
    enum { DecorationMargin = 4 };
    if (QApplication::layoutDirection() == Qt::LeftToRight)
        lt->setContentsMargins(DecorationMargin, 0, 0, 0);
    else
        lt->setContentsMargins(0, 0, DecorationMargin, 0);
}

QString double2str(double val, int precision)
{
    char text[50];
    if(val < lowest)
        std::sprintf(text,"%s","-inf");
    else if(val > highest)
        std::sprintf(text,"%s","inf");
    else
        std::sprintf(text,"%0.*g",precision+1, val);
    return QString(text);
}

// QComplex
QComplex::QComplex(std::complex<double> parent)
: std::complex<double>(parent)
{

}

QComplex::QComplex(double re, double im)
: std::complex<double>(re,im)
{

}


// QIntEdit

class QIntEditPrivate
{
    QIntEdit *q_ptr;
    Q_DECLARE_PUBLIC(QIntEdit)
public:
    QIntEditPrivate()
        : m_value(0),
          m_minimum(lowest),
          m_maximum(highest),
          m_precision(3),
          m_format(Format::LIN_DEG),
          m_scale(Scale::_),
          m_readOnly(false),
          m_edit(nullptr){}

    int m_value;
    double m_minimum;
    double m_maximum;
    int m_precision;
    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    QLineEdit* m_edit;

private:
    QRegExpValidator *validator;
};

QIntEdit::QIntEdit(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QIntEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegExpValidator(regExps[Format::LIN_DEG], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QIntEdit::~QIntEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

int QIntEdit::value() const
{
    return d_ptr->m_value;
}

double QIntEdit::minimum() const
{
    return d_ptr->m_minimum;
}

double QIntEdit::maximum() const
{
    return d_ptr->m_maximum;
}

int QIntEdit::precision() const
{
    return d_ptr->m_precision;
}

Format QIntEdit::format() const
{
    return d_ptr->m_format;
}

Scale QIntEdit::scale() const
{
    return d_ptr->m_scale;
}

void QIntEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    int val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = QIntEdit::str2num(d_ptr->m_edit->text(), d_ptr->m_scale, d_ptr->m_format);
        if (d_ptr->m_value != val) {
            d_ptr->m_value = val;
            emit valueChanged(val);
        }
    }
}

void QIntEdit::setValue(int val)
{
    if (d_ptr->m_value != val) {
        d_ptr->m_value = val;
        d_ptr->m_edit->setText(QIntEdit::num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
        emit valueChanged(val);
    }
}

void QIntEdit::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, epsilon, epsilon)){
        if(d_ptr->m_value < min)
            setValue(int(min));
        d_ptr->m_minimum = min;
    }
}

void QIntEdit::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, epsilon, epsilon)){
        if(d_ptr->m_value > max)
            setValue(int(max));
        d_ptr->m_maximum = max;
    }
}

void QIntEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QIntEdit::setPrecision(int prec)
{
    if (d_ptr->m_precision != prec) {
        d_ptr->m_precision = prec;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QIntEdit::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QIntEdit::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QIntEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_edit->setReadOnly(readOnly);
}

bool QIntEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

void QIntEdit::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}

QValidator::State QIntEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);

}

QString QIntEdit::num2str(int val, const Scale scale, const Format format, int precision)
{
    double scaled_val;
    QString text;
    int scale_ = ScaleValueMap[scale];
    switch (format) {
        case Format::LOG_DEG:
            scaled_val = val/sqrt(pow(10, scale_));
            text = double2str(20*log10(scaled_val), precision);
            break;
        default:
            scaled_val = val/pow(10, scale_);
            text = double2str(scaled_val, precision);
            break;
    }
    return text;
}

int QIntEdit::str2num(const QString &text, const Scale scale, const Format format)
{
    QRegExp regExp = regExps[format];
    int pos;
    int val = 0;
    int scale_ = ScaleValueMap[scale];
    switch (format) {
        case Format::LOG_DEG:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            val = int(pow(10,(regExp.cap(1).toDouble())/20));
            val *= sqrt(pow(10, scale_));
            break;
        default:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            val = regExp.cap(1).toInt();
            val *= pow(10, scale_);
            break;
    }
    if (isinfinite(std::abs(val)))
        val = 0;
    return val;
}

// QDoubleEdit

class QDoubleEditPrivate
{
    QDoubleEdit *q_ptr;
    Q_DECLARE_PUBLIC(QDoubleEdit)
public:
    QDoubleEditPrivate()
        : m_value(0),
          m_precision(3),
          m_format(Format::LIN_DEG),
          m_scale(Scale::_),
          m_readOnly(false) {}

    double m_value;
    double m_minimum;
    double m_maximum;
    int m_precision;

    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    QLineEdit* m_edit;

private:
    QRegExpValidator *validator;
};

QDoubleEdit::QDoubleEdit(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QDoubleEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegExpValidator(regExps[Format::LIN_DEG], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QDoubleEdit::~QDoubleEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

double QDoubleEdit::value() const
{
    return d_ptr->m_value;
}

double QDoubleEdit::minimum() const
{
    return d_ptr->m_minimum;
}

double QDoubleEdit::maximum() const
{
    return d_ptr->m_maximum;
}

int QDoubleEdit::precision() const
{
    return d_ptr->m_precision;
}

Format QDoubleEdit::format() const
{
    return d_ptr->m_format;
}

Scale QDoubleEdit::scale() const
{
    return d_ptr->m_scale;
}

void QDoubleEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    double val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = str2num(d_ptr->m_edit->text(), d_ptr->m_scale, d_ptr->m_format);
        if (!isclose(val, d_ptr->m_value, epsilon, epsilon)){
            d_ptr->m_value = val;
            emit valueChanged(val);
        }
    }
}

void QDoubleEdit::setValue(double val)
{
    if (!isclose(val, d_ptr->m_value, epsilon, epsilon)){
        d_ptr->m_value = val;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
        emit valueChanged(val);
    }
}

void QDoubleEdit::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, epsilon, epsilon)){
        if (d_ptr->m_value < min)
            setValue(min);
        d_ptr->m_minimum = min;
    }
}

void QDoubleEdit::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, epsilon, epsilon)){
        if (d_ptr->m_value > max)
            setValue(max);
        d_ptr->m_maximum = max;
    }
}

void QDoubleEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QDoubleEdit::setPrecision(int prec)
{
    if (d_ptr->m_precision != prec) {
        d_ptr->m_precision = prec;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QDoubleEdit::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QDoubleEdit::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QDoubleEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
    d_ptr->m_edit->setReadOnly(readOnly);
}

bool QDoubleEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

void QDoubleEdit::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}

QValidator::State QDoubleEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);

}

QString QDoubleEdit::num2str(double val, const Scale scale, const Format format, int precision)
{
    double scaled_val;
    QString text;
    int scale_ = ScaleValueMap[scale];
    switch (format) {
        case Format::LOG_DEG:
            scaled_val = val/sqrt(pow(10, scale_));
            text = double2str(20*log10(scaled_val), precision);
            break;
        default:
            scaled_val = val/pow(10, scale_);
            text = double2str(scaled_val, precision);
            break;
    }
    return text;
}

double QDoubleEdit::str2num(const QString &text, const Scale scale, const Format format)
{
    QRegExp regExp = regExps[format];
    int pos;
    double val = 0;
    int scale_ = ScaleValueMap[scale];
    switch (format) {
        case Format::LOG_DEG:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            val = pow(10,(regExp.cap(1).toDouble())/20);
            val *= sqrt(pow(10, scale_));
            break;
    default:
        pos = regExp.indexIn(text);
        if (pos == -1)
            return val;
        val = regExp.cap(1).toDouble();
        val *= pow(10, scale_);
        break;
    }
    if (isinfinite(std::abs(val)))
        val = 0;
    return val;
}

// QComplexEdit

class QComplexEditPrivate
{
    QComplexEdit *q_ptr;
    Q_DECLARE_PUBLIC(QComplexEdit)
public:
    QComplexEditPrivate()
        : m_value(0),
          m_precision(3),
          m_format(Format::RE_IM),
          m_scale(Scale::_),
          m_readOnly(false) {}

    QComplex m_value;
    double m_minimum;
    double m_maximum;
    int m_precision;

    Format m_format;
    Scale m_scale;
    bool m_readOnly;
    QLineEdit* m_edit;

private:
    QRegExpValidator *validator;
};

QComplexEdit::QComplexEdit(QWidget *parent) :
QWidget(parent)
{
    d_ptr = new QComplexEditPrivate();
    d_ptr->q_ptr = this;

    d_ptr->m_edit = new QLineEdit("0");
    d_ptr->validator = new QRegExpValidator(regExps[Format::RE_IM], this);

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(d_ptr->m_edit);
    this->setFocusProxy(d_ptr->m_edit);

    connect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
}

QComplexEdit::~QComplexEdit()
{
    disconnect(d_ptr->m_edit, SIGNAL(editingFinished()), this, SLOT(setValue()));
    emit destroyed(this);
}

QComplex QComplexEdit::value() const
{
    return d_ptr->m_value;
}

double QComplexEdit::minimum() const
{
    return d_ptr->m_minimum;
}

double QComplexEdit::maximum() const
{
    return d_ptr->m_maximum;
}

int QComplexEdit::precision() const
{
    return d_ptr->m_precision;
}

Format QComplexEdit::format() const
{
    return d_ptr->m_format;
}

Scale QComplexEdit::scale() const
{
    return d_ptr->m_scale;
}

void QComplexEdit::setValue()
{
    QString text = d_ptr->m_edit->text();
    int pos = 0;
    QComplex val;

    if (!d_ptr->m_readOnly && validate(text,pos))
    {
        val = QComplexEdit::str2num(d_ptr->m_edit->text(), d_ptr->m_scale, d_ptr->m_format);
        if (!isclose(val, d_ptr->m_value, epsilon, epsilon)){
            d_ptr->m_value = val;
            emit valueChanged(val);
        }
    }
}

void QComplexEdit::setValue(const QComplex &val)
{
    if (!isclose(val, d_ptr->m_value, epsilon, epsilon)){
        d_ptr->m_value = val;
        d_ptr->m_edit->setText(QComplexEdit::num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
        emit valueChanged(val);
    }
}

void QComplexEdit::setMinimum(double min)
{
    if (!isclose(min, d_ptr->m_minimum, epsilon, epsilon)){
        if(abs(d_ptr->m_value) < min)
            setValue(min);
        d_ptr->m_minimum = min;
    }
}

void QComplexEdit::setMaximum(double max)
{
    if (!isclose(max, d_ptr->m_maximum, epsilon, epsilon)){
        if(abs(d_ptr->m_value) > max)
            setValue(max);
        d_ptr->m_maximum = max;
    }
}

void QComplexEdit::setRange(double min, double max)
{
    if (min < max)
    {
        setMinimum(min);
        setMaximum(max);
    }
}

void QComplexEdit::setPrecision(int prec)
{
    if (d_ptr->m_precision != prec) {
        d_ptr->m_precision = prec;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QComplexEdit::setFormat(Format format_)
{
    if (d_ptr->m_format!= format_) {
        d_ptr->m_format = format_;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QComplexEdit::setScale(Scale scale_)
{
    if (d_ptr->m_scale!= scale_) {
        d_ptr->m_scale = scale_;
        d_ptr->m_edit->setText(num2str(d_ptr->m_value, d_ptr->m_scale, d_ptr->m_format, d_ptr->m_precision));
    }
}

void QComplexEdit::setReadOnly(bool readOnly)
{
    if (d_ptr->m_readOnly != readOnly)
        d_ptr->m_edit->setReadOnly(readOnly);
}

bool QComplexEdit::eventFilter(QObject *obj, QEvent *ev)
{
    return QWidget::eventFilter(obj, ev);
}

void QComplexEdit::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}

QValidator::State QComplexEdit::validate(QString &text, int &pos) const
{
    return d_ptr->validator->validate(text, pos);

}

QString QComplexEdit::num2str(const QComplex& val, const Scale scale, const Format format, int precision)
{
    QComplex scaled_val;
    QString text1, sep, text2;
    int scale_ = ScaleValueMap[scale];
    switch (format) {
        case Format::RE:
            scaled_val = val/pow(10, scale_);
            text1 = double2str(scaled_val.real(), precision);
            sep = QString("");
            text2 = QString("");
            break;
        case Format::RE_IM:
            scaled_val = val/pow(10, scale_);
            text1 = double2str(scaled_val.real(), precision);
            sep = QString("+");
            text2 = double2str(scaled_val.imag(), precision) + "j";
            break;
        case Format::LOG_DEG:
            scaled_val = val/sqrt(pow(10, scale_));
            text1 = double2str(20*log10(abs(scaled_val)), precision);
            sep = QString(QChar(0x2220));
            text2 = double2str(arg(scaled_val)*180/M_PI, precision);
            break;
        default:
            scaled_val = val/pow(10, scale_);
            text1 = double2str(abs(scaled_val), precision);
            sep = QString(QChar(0x2220));
            text2 = double2str(arg(scaled_val)*180/M_PI, precision);
            break;
    }
    return text1 + sep + text2;
}

QComplex QComplexEdit::str2num(const QString &text, const Scale scale, const Format format)
{
    QRegExp regExp = regExps[format];
    int pos;
    int scale_ = ScaleValueMap[scale];
    QComplex val = 0;
    switch (format) {
        case Format::RE:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            val = QComplex(regExp.cap(1).toDouble());
            val *= pow(10, scale_);
            break;
        case Format::RE_IM:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            if(regExp.captureCount() == 3)
                val = QComplex(regExp.cap(1).toDouble(),regExp.cap(3).toDouble());
            else
                val = QComplex(regExp.cap(1).toDouble());
            val *= pow(10, scale_);
            break;
        case Format::LOG_DEG:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            if(regExp.captureCount() == 3)
                val = std::polar(pow(10,(regExp.cap(1).toDouble())/20),regExp.cap(3).toDouble()*M_PI/180);
            else
                val = QComplex(pow(10,(regExp.cap(1).toDouble())/20),0);
            val *= sqrt(pow(10, scale_));
            break;
        default:
            pos = regExp.indexIn(text);
            if (pos == -1)
                return val;
            if(regExp.captureCount() == 3)
                val = std::polar(regExp.cap(1).toDouble(),regExp.cap(3).toDouble()*M_PI/180);
            else
                val = QComplex(regExp.cap(1).toDouble(),0);
            val *= pow(10, scale_);
            break;
    }
    if (isinfinite(std::abs(val)))
        val = 0;
    return val;
}


// FileEditWidget
QFileEdit::QFileEdit(QWidget *parent) : QWidget(parent),
m_edit(new QLineEdit), m_button(new QToolButton)
{
    m_fileName = QString();
    m_filter = QString();
    m_fileMode = QFileDialog::AnyFile;
    m_readOnly = false;

    QHBoxLayout *lt = new QHBoxLayout(this);
    setupTreeViewEditorMargin(lt);
    lt->setSpacing(0);
    lt->addWidget(m_edit);

    m_button->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Ignored);
    m_button->setFixedWidth(20);
    setFocusProxy(m_button);
    setFocusPolicy(m_button->focusPolicy());
    m_button->setText(tr("..."));
    m_button->installEventFilter(this);

    connect(m_button, SIGNAL(clicked()), this, SLOT(slotButtonClicked()));
    connect(m_edit, SIGNAL(editingFinished()), this, SLOT(slotEditFinished()));

    lt->addWidget(m_button);
    m_edit->setText(m_fileName);
}

QFileEdit::~QFileEdit()
{
    emit destroyed(this);
}

bool QFileEdit::fileExists(QString path) const{
    QFileInfo checkFile(path);
    // check if file exists and if yes: Is it really a file and no directory?
    if (checkFile.exists() && m_fileMode != QFileDialog::Directory && checkFile.isFile())
        return true;
    else if (checkFile.exists() && m_fileMode == QFileDialog::Directory && checkFile.isDir())
        return true;
    else
        return false;
}

bool QFileEdit::validExtension(QString path) const{
    QFileInfo fileInfo = QFileInfo(path);
    QString ext = fileInfo.completeSuffix();
    QRegExp regExp = QRegExp("\\*(?:[\\.\\w\\d]+)?");
    QString match;
    int pos = 0;

    if (m_fileMode == QFileDialog::Directory){
        if (ext.isEmpty())
            return true;
        else
            return false;
    }
    else{
        if (ext.isEmpty())
            return false;
        while ((pos = regExp.indexIn(m_filter, pos)) != -1) {
            match = regExp.cap(0);
            pos += regExp.matchedLength();
            if (match == QString("*."+ext) || match == "*")
                return true;
        }
    }
    return false;

}

void QFileEdit::setValue(const QString &fileName)
{
    if (fileExists(fileName) && validExtension(fileName) && fileName != m_fileName) {
        m_fileName = fileName;
        m_edit->setText(fileName);
        emit valueChanged(fileName);
    }
}
void QFileEdit::setFilter(const QString &filter)
{
    if (m_filter != filter) {
        m_filter = filter;
    }
}

void QFileEdit::setFileMode(const QFileDialog::FileMode mode)
{
    if (m_fileMode != mode) {
        m_fileMode = mode;
    }
}

void QFileEdit::setReadOnly(const bool readOnly)
{
    if (m_readOnly != readOnly) {
        m_edit->setReadOnly(readOnly);
    }
}

void QFileEdit::slotEditFinished()
{
    QString fileName = m_edit->text();
    setValue(fileName);
}

void QFileEdit::slotButtonClicked()
{
//    QString fileName = QFileDialog::getOpenFileName(this,
//                                                    tr("QFileDialog::getOpenFileName()"),
//                                                    m_fileName,
//                                                    m_filter);
    QStringList fileNames;
    QFileDialog dialog(this);
    if (m_fileMode != QFileDialog::Directory)
        dialog.setNameFilter(m_filter);
    dialog.setFileMode(m_fileMode);
    dialog.setViewMode(QFileDialog::Detail);


    if (dialog.exec())
        fileNames = dialog.selectedFiles();

    if ((!fileNames.isEmpty()) && (fileNames.at(0) != m_fileName)){
        setValue(fileNames.at(0));
    }
}

bool QFileEdit::eventFilter(QObject *obj, QEvent *ev)
{
    if (obj == m_button) {
        switch (ev->type()) {
            case QEvent::KeyPress:
            case QEvent::KeyRelease: { // Prevent the QToolButton from handling Enter/Escape meant control the delegate
                switch (static_cast<const QKeyEvent*>(ev)->key()) {
                    case Qt::Key_Escape:
                    case Qt::Key_Enter:
                    case Qt::Key_Return:
                        ev->ignore();
                        return true;
                    default:
                        break;
                }
            }
                break;
            default:
                break;
        }
    }
    return QWidget::eventFilter(obj, ev);
}

void QFileEdit::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}

QtCursorDatabase::QtCursorDatabase()
{
    appendCursor(Qt::ArrowCursor, QCoreApplication::translate("QtCursorDatabase", "Arrow"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-arrow.png")));
    appendCursor(Qt::UpArrowCursor, QCoreApplication::translate("QtCursorDatabase", "Up Arrow"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-uparrow.png")));
    appendCursor(Qt::CrossCursor, QCoreApplication::translate("QtCursorDatabase", "Cross"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-cross.png")));
    appendCursor(Qt::WaitCursor, QCoreApplication::translate("QtCursorDatabase", "Wait"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-wait.png")));
    appendCursor(Qt::IBeamCursor, QCoreApplication::translate("QtCursorDatabase", "IBeam"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-ibeam.png")));
    appendCursor(Qt::SizeVerCursor, QCoreApplication::translate("QtCursorDatabase", "Size Vertical"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizev.png")));
    appendCursor(Qt::SizeHorCursor, QCoreApplication::translate("QtCursorDatabase", "Size Horizontal"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizeh.png")));
    appendCursor(Qt::SizeFDiagCursor, QCoreApplication::translate("QtCursorDatabase", "Size Backslash"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizef.png")));
    appendCursor(Qt::SizeBDiagCursor, QCoreApplication::translate("QtCursorDatabase", "Size Slash"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizeb.png")));
    appendCursor(Qt::SizeAllCursor, QCoreApplication::translate("QtCursorDatabase", "Size All"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-sizeall.png")));
    appendCursor(Qt::BlankCursor, QCoreApplication::translate("QtCursorDatabase", "Blank"),
                 QIcon());
    appendCursor(Qt::SplitVCursor, QCoreApplication::translate("QtCursorDatabase", "Split Vertical"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-vsplit.png")));
    appendCursor(Qt::SplitHCursor, QCoreApplication::translate("QtCursorDatabase", "Split Horizontal"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-hsplit.png")));
    appendCursor(Qt::PointingHandCursor, QCoreApplication::translate("QtCursorDatabase", "Pointing Hand"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-hand.png")));
    appendCursor(Qt::ForbiddenCursor, QCoreApplication::translate("QtCursorDatabase", "Forbidden"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-forbidden.png")));
    appendCursor(Qt::OpenHandCursor, QCoreApplication::translate("QtCursorDatabase", "Open Hand"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-openhand.png")));
    appendCursor(Qt::ClosedHandCursor, QCoreApplication::translate("QtCursorDatabase", "Closed Hand"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-closedhand.png")));
    appendCursor(Qt::WhatsThisCursor, QCoreApplication::translate("QtCursorDatabase", "What's This"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-whatsthis.png")));
    appendCursor(Qt::BusyCursor, QCoreApplication::translate("QtCursorDatabase", "Busy"),
                 QIcon(QLatin1String(":/qt-project.org/qtpropertybrowser/images/cursor-busy.png")));
}

void QtCursorDatabase::clear()
{
    m_cursorNames.clear();
    m_cursorIcons.clear();
    m_valueToCursorShape.clear();
    m_cursorShapeToValue.clear();
}

void QtCursorDatabase::appendCursor(Qt::CursorShape shape, const QString &name, const QIcon &icon)
{
    if (m_cursorShapeToValue.contains(shape))
        return;
    const int value = m_cursorNames.count();
    m_cursorNames.append(name);
    m_cursorIcons.insert(value, icon);
    m_valueToCursorShape.insert(value, shape);
    m_cursorShapeToValue.insert(shape, value);
}

QStringList QtCursorDatabase::cursorShapeNames() const
{
    return m_cursorNames;
}

QMap<int, QIcon> QtCursorDatabase::cursorShapeIcons() const
{
    return m_cursorIcons;
}

QString QtCursorDatabase::cursorToShapeName(const QCursor &cursor) const
{
    int val = cursorToValue(cursor);
    if (val >= 0)
        return m_cursorNames.at(val);
    return QString();
}

QIcon QtCursorDatabase::cursorToShapeIcon(const QCursor &cursor) const
{
    int val = cursorToValue(cursor);
    return m_cursorIcons.value(val);
}

int QtCursorDatabase::cursorToValue(const QCursor &cursor) const
{
#ifndef QT_NO_CURSOR
    Qt::CursorShape shape = cursor.shape();
    if (m_cursorShapeToValue.contains(shape))
        return m_cursorShapeToValue[shape];
#endif
    return -1;
}

#ifndef QT_NO_CURSOR
QCursor QtCursorDatabase::valueToCursor(int value) const
{
    if (m_valueToCursorShape.contains(value))
        return QCursor(m_valueToCursorShape[value]);
    return QCursor();
}
#endif

QPixmap QtPropertyBrowserUtils::brushValuePixmap(const QBrush &b)
{
    QImage img(16, 16, QImage::Format_ARGB32_Premultiplied);
    img.fill(0);

    QPainter painter(&img);
    painter.setCompositionMode(QPainter::CompositionMode_Source);
    painter.fillRect(0, 0, img.width(), img.height(), b);
    QColor color = b.color();
    if (color.alpha() != 255) { // indicate alpha by an inset
        QBrush  opaqueBrush = b;
        color.setAlpha(255);
        opaqueBrush.setColor(color);
        painter.fillRect(img.width() / 4, img.height() / 4,
                         img.width() / 2, img.height() / 2, opaqueBrush);
    }
    painter.end();
    return QPixmap::fromImage(img);
}

QIcon QtPropertyBrowserUtils::brushValueIcon(const QBrush &b)
{
    return QIcon(brushValuePixmap(b));
}

QString QtPropertyBrowserUtils::colorValueText(const QColor &c)
{
    return QCoreApplication::translate("QtPropertyBrowserUtils", "[%1, %2, %3] (%4)")
           .arg(c.red()).arg(c.green()).arg(c.blue()).arg(c.alpha());
}

QPixmap QtPropertyBrowserUtils::fontValuePixmap(const QFont &font)
{
    QFont f = font;
    QImage img(16, 16, QImage::Format_ARGB32_Premultiplied);
    img.fill(0);
    QPainter p(&img);
    p.setRenderHint(QPainter::TextAntialiasing, true);
    p.setRenderHint(QPainter::Antialiasing, true);
    f.setPointSize(13);
    p.setFont(f);
    QTextOption t;
    t.setAlignment(Qt::AlignCenter);
    p.drawText(QRect(0, 0, 16, 16), QString(QLatin1Char('A')), t);
    return QPixmap::fromImage(img);
}

QIcon QtPropertyBrowserUtils::fontValueIcon(const QFont &f)
{
    return QIcon(fontValuePixmap(f));
}

QString QtPropertyBrowserUtils::fontValueText(const QFont &f)
{
    return QCoreApplication::translate("QtPropertyBrowserUtils", "[%1, %2]")
           .arg(f.family()).arg(f.pointSize());
}


QtBoolEdit::QtBoolEdit(QWidget *parent) :
    QWidget(parent),
    m_checkBox(new QCheckBox(this)),
    m_textVisible(true)
{
    QHBoxLayout *lt = new QHBoxLayout;
    if (QApplication::layoutDirection() == Qt::LeftToRight)
        lt->setContentsMargins(4, 0, 0, 0);
    else
        lt->setContentsMargins(0, 0, 4, 0);
    lt->addWidget(m_checkBox);
    setLayout(lt);
    connect(m_checkBox, SIGNAL(toggled(bool)), this, SIGNAL(toggled(bool)));
    setFocusProxy(m_checkBox);
    m_checkBox->setText(tr("True"));
}

void QtBoolEdit::setTextVisible(bool textVisible)
{
    if (m_textVisible == textVisible)
        return;

    m_textVisible = textVisible;
    if (m_textVisible)
        m_checkBox->setText(isChecked() ? tr("True") : tr("False"));
    else
        m_checkBox->setText(QString());
}

Qt::CheckState QtBoolEdit::checkState() const
{
    return m_checkBox->checkState();
}

void QtBoolEdit::setCheckState(Qt::CheckState state)
{
    m_checkBox->setCheckState(state);
}

bool QtBoolEdit::isChecked() const
{
    return m_checkBox->isChecked();
}

void QtBoolEdit::setChecked(bool c)
{
    m_checkBox->setChecked(c);
    if (!m_textVisible)
        return;
    m_checkBox->setText(isChecked() ? tr("True") : tr("False"));
}

bool QtBoolEdit::blockCheckBoxSignals(bool block)
{
    return m_checkBox->blockSignals(block);
}

void QtBoolEdit::mousePressEvent(QMouseEvent *event)
{
    if (event->buttons() == Qt::LeftButton) {
        m_checkBox->click();
        event->accept();
    } else {
        QWidget::mousePressEvent(event);
    }
}

void QtBoolEdit::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}



QtKeySequenceEdit::QtKeySequenceEdit(QWidget *parent)
    : QWidget(parent), m_num(0), m_lineEdit(new QLineEdit(this))
{
    QHBoxLayout *layout = new QHBoxLayout(this);
    layout->addWidget(m_lineEdit);
    layout->setMargin(0);
    m_lineEdit->installEventFilter(this);
    m_lineEdit->setReadOnly(true);
    m_lineEdit->setFocusProxy(this);
    setFocusPolicy(m_lineEdit->focusPolicy());
    setAttribute(Qt::WA_InputMethodEnabled);
}

bool QtKeySequenceEdit::eventFilter(QObject *o, QEvent *e)
{
    if (o == m_lineEdit && e->type() == QEvent::ContextMenu) {
        QContextMenuEvent *c = static_cast<QContextMenuEvent *>(e);
        QMenu *menu = m_lineEdit->createStandardContextMenu();
        const QList<QAction *> actions = menu->actions();
        QListIterator<QAction *> itAction(actions);
        while (itAction.hasNext()) {
            QAction *action = itAction.next();
            action->setShortcut(QKeySequence());
            QString actionString = action->text();
            const int pos = actionString.lastIndexOf(QLatin1Char('\t'));
            if (pos > 0)
                actionString.remove(pos, actionString.length() - pos);
            action->setText(actionString);
        }
        QAction *actionBefore = nullptr;
        if (actions.count() > 0)
            actionBefore = actions[0];
        QAction *clearAction = new QAction(tr("Clear Shortcut"), menu);
        menu->insertAction(actionBefore, clearAction);
        menu->insertSeparator(actionBefore);
        clearAction->setEnabled(!m_keySequence.isEmpty());
        connect(clearAction, SIGNAL(triggered()), this, SLOT(slotClearShortcut()));
        menu->exec(c->globalPos());
        delete menu;
        e->accept();
        return true;
    }

    return QWidget::eventFilter(o, e);
}

void QtKeySequenceEdit::slotClearShortcut()
{
    if (m_keySequence.isEmpty())
        return;
    setKeySequence(QKeySequence());
    emit keySequenceChanged(m_keySequence);
}

void QtKeySequenceEdit::handleKeyEvent(QKeyEvent *e)
{
    int nextKey = e->key();
    if (nextKey == Qt::Key_Control || nextKey == Qt::Key_Shift ||
            nextKey == Qt::Key_Meta || nextKey == Qt::Key_Alt ||
            nextKey == Qt::Key_Super_L || nextKey == Qt::Key_AltGr)
        return;

    nextKey |= translateModifiers(e->modifiers(), e->text());
    int k0 = m_keySequence[0];
    int k1 = m_keySequence[1];
    int k2 = m_keySequence[2];
    int k3 = m_keySequence[3];
    switch (m_num) {
        case 0: k0 = nextKey; k1 = 0; k2 = 0; k3 = 0; break;
        case 1: k1 = nextKey; k2 = 0; k3 = 0; break;
        case 2: k2 = nextKey; k3 = 0; break;
        case 3: k3 = nextKey; break;
        default: break;
    }
    ++m_num;
    if (m_num > 3)
        m_num = 0;
    m_keySequence = QKeySequence(k0, k1, k2, k3);
    m_lineEdit->setText(m_keySequence.toString(QKeySequence::NativeText));
    e->accept();
    emit keySequenceChanged(m_keySequence);
}

void QtKeySequenceEdit::setKeySequence(const QKeySequence &sequence)
{
    if (sequence == m_keySequence)
        return;
    m_num = 0;
    m_keySequence = sequence;
    m_lineEdit->setText(m_keySequence.toString(QKeySequence::NativeText));
}

QKeySequence QtKeySequenceEdit::keySequence() const
{
    return m_keySequence;
}

int QtKeySequenceEdit::translateModifiers(Qt::KeyboardModifiers state, const QString &text) const
{
    int result = 0;
    if ((state & Qt::ShiftModifier) && (text.size() == 0 || !text.at(0).isPrint() || text.at(0).isLetter() || text.at(0).isSpace()))
        result |= Qt::SHIFT;
    if (state & Qt::ControlModifier)
        result |= Qt::CTRL;
    if (state & Qt::MetaModifier)
        result |= Qt::META;
    if (state & Qt::AltModifier)
        result |= Qt::ALT;
    return result;
}

void QtKeySequenceEdit::focusInEvent(QFocusEvent *e)
{
    m_lineEdit->event(e);
    m_lineEdit->selectAll();
    QWidget::focusInEvent(e);
}

void QtKeySequenceEdit::focusOutEvent(QFocusEvent *e)
{
    m_num = 0;
    m_lineEdit->event(e);
    QWidget::focusOutEvent(e);
}

void QtKeySequenceEdit::keyPressEvent(QKeyEvent *e)
{
    handleKeyEvent(e);
    e->accept();
}

void QtKeySequenceEdit::keyReleaseEvent(QKeyEvent *e)
{
    m_lineEdit->event(e);
}

void QtKeySequenceEdit::paintEvent(QPaintEvent *)
{
    QStyleOption opt;
    opt.init(this);
    QPainter p(this);
    style()->drawPrimitive(QStyle::PE_Widget, &opt, &p, this);
}

bool QtKeySequenceEdit::event(QEvent *e)
{
    if (e->type() == QEvent::Shortcut ||
            e->type() == QEvent::ShortcutOverride  ||
            e->type() == QEvent::KeyRelease) {
        e->accept();
        return true;
    }
    return QWidget::event(e);
}




#if QT_VERSION >= 0x040400
QT_END_NAMESPACE
#endif
