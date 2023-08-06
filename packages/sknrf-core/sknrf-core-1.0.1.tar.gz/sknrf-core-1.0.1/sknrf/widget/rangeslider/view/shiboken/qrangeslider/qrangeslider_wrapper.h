#ifndef SBK_QRANGESLIDERWRAPPER_H
#define SBK_QRANGESLIDERWRAPPER_H

#include <qrangeslider.h>

namespace PySide { class DynamicQMetaObject; }

class QRangeSliderWrapper : public QRangeSlider
{
public:
    QRangeSliderWrapper(QWidget * parent = 0);
    QRangeSliderWrapper(Qt::Orientation orientation, QWidget * parent = 0);
    inline void actionEvent_protected(QActionEvent * event) { QRangeSlider::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * e) { QRangeSlider::changeEvent(e); }
    void changeEvent(QEvent * e) override;
    inline void childEvent_protected(QChildEvent * event) { QRangeSlider::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QRangeSlider::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QRangeSlider::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QRangeSlider::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QRangeSlider::create(arg__1, initializeWindow, destroyOldWindow); }
    inline void customEvent_protected(QEvent * event) { QRangeSlider::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QRangeSlider::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QRangeSlider::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QRangeSlider::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QRangeSlider::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QRangeSlider::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QRangeSlider::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEvent * event) { QRangeSlider::enterEvent(event); }
    void enterEvent(QEvent * event) override;
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QRangeSlider::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QRangeSlider::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QRangeSlider::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QRangeSlider::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QRangeSlider::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QRangeSlider::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QRangeSlider::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void initStyleOption_protected(QStyleOptionSlider * option) const { QRangeSlider::initStyleOption(option); }
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QRangeSlider::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void keyPressEvent_protected(QKeyEvent * event) { QRangeSlider::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QRangeSlider::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QRangeSlider::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QRangeSlider::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QRangeSlider::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QRangeSlider::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QRangeSlider::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QRangeSlider::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QRangeSlider::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, long * result) { return QRangeSlider::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, long * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QRangeSlider::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QRangeSlider::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline QAbstractSlider::SliderAction repeatAction_protected() const { return QRangeSlider::repeatAction(); }
    inline void resizeEvent_protected(QResizeEvent * event) { QRangeSlider::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    inline void setRepeatAction_protected(QAbstractSlider::SliderAction action, int thresholdTime = 500, int repeatTime = 50) { QRangeSlider::setRepeatAction(QAbstractSlider::SliderAction(action), thresholdTime, repeatTime); }
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QRangeSlider::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QRangeSlider::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void sliderChange_protected(int change) { QRangeSlider::sliderChange(QAbstractSlider::SliderChange(change)); }
    void sliderChange(QAbstractSlider::SliderChange change) override;
    inline void tabletEvent_protected(QTabletEvent * event) { QRangeSlider::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * arg__1) { QRangeSlider::timerEvent(arg__1); }
    void timerEvent(QTimerEvent * arg__1) override;
    inline void updateMicroFocus_protected() { QRangeSlider::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * e) { QRangeSlider::wheelEvent(e); }
    void wheelEvent(QWheelEvent * e) override;
    ~QRangeSliderWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  ifndef SBK_QSLIDERWRAPPER_H
#  define SBK_QSLIDERWRAPPER_H

// Inherited base class:
class QSliderWrapper : public QSlider
{
public:
    QSliderWrapper(QWidget * parent = nullptr);
    QSliderWrapper(Qt::Orientation orientation, QWidget * parent = nullptr);
    inline void actionEvent_protected(QActionEvent * event) { QSlider::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * e) { QSlider::changeEvent(e); }
    void changeEvent(QEvent * e) override;
    inline void childEvent_protected(QChildEvent * event) { QSlider::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QSlider::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QSlider::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QSlider::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QSlider::create(arg__1, initializeWindow, destroyOldWindow); }
    inline void customEvent_protected(QEvent * event) { QSlider::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QSlider::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QSlider::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QSlider::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QSlider::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QSlider::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QSlider::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEvent * event) { QSlider::enterEvent(event); }
    void enterEvent(QEvent * event) override;
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QSlider::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QSlider::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QSlider::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QSlider::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QSlider::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QSlider::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QSlider::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void initStyleOption_protected(QStyleOptionSlider * option) const { QSlider::initStyleOption(option); }
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QSlider::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void keyPressEvent_protected(QKeyEvent * ev) { QSlider::keyPressEvent(ev); }
    void keyPressEvent(QKeyEvent * ev) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QSlider::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QSlider::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QSlider::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QSlider::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * ev) { QSlider::mouseMoveEvent(ev); }
    void mouseMoveEvent(QMouseEvent * ev) override;
    inline void mousePressEvent_protected(QMouseEvent * ev) { QSlider::mousePressEvent(ev); }
    void mousePressEvent(QMouseEvent * ev) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * ev) { QSlider::mouseReleaseEvent(ev); }
    void mouseReleaseEvent(QMouseEvent * ev) override;
    inline void moveEvent_protected(QMoveEvent * event) { QSlider::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, long * result) { return QSlider::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, long * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * ev) { QSlider::paintEvent(ev); }
    void paintEvent(QPaintEvent * ev) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QSlider::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline QAbstractSlider::SliderAction repeatAction_protected() const { return QSlider::repeatAction(); }
    inline void resizeEvent_protected(QResizeEvent * event) { QSlider::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    inline void setRepeatAction_protected(QAbstractSlider::SliderAction action, int thresholdTime = 500, int repeatTime = 50) { QSlider::setRepeatAction(QAbstractSlider::SliderAction(action), thresholdTime, repeatTime); }
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QSlider::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QSlider::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void sliderChange_protected(int change) { QSlider::sliderChange(QAbstractSlider::SliderChange(change)); }
    void sliderChange(QAbstractSlider::SliderChange change) override;
    inline void tabletEvent_protected(QTabletEvent * event) { QSlider::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * arg__1) { QSlider::timerEvent(arg__1); }
    void timerEvent(QTimerEvent * arg__1) override;
    inline void updateMicroFocus_protected() { QSlider::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * e) { QSlider::wheelEvent(e); }
    void wheelEvent(QWheelEvent * e) override;
    ~QSliderWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QSLIDERWRAPPER_H

#  ifndef SBK_QABSTRACTSLIDERWRAPPER_H
#  define SBK_QABSTRACTSLIDERWRAPPER_H

// Inherited base class:
class QAbstractSliderWrapper : public QAbstractSlider
{
public:
    QAbstractSliderWrapper(QWidget * parent = nullptr);
    inline void actionEvent_protected(QActionEvent * event) { QAbstractSlider::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * e) { QAbstractSlider::changeEvent(e); }
    void changeEvent(QEvent * e) override;
    inline void childEvent_protected(QChildEvent * event) { QAbstractSlider::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QAbstractSlider::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QAbstractSlider::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QAbstractSlider::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QAbstractSlider::create(arg__1, initializeWindow, destroyOldWindow); }
    inline void customEvent_protected(QEvent * event) { QAbstractSlider::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QAbstractSlider::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QAbstractSlider::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QAbstractSlider::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QAbstractSlider::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QAbstractSlider::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QAbstractSlider::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEvent * event) { QAbstractSlider::enterEvent(event); }
    void enterEvent(QEvent * event) override;
    inline bool event_protected(QEvent * e) { return QAbstractSlider::event(e); }
    bool event(QEvent * e) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QAbstractSlider::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QAbstractSlider::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QAbstractSlider::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QAbstractSlider::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QAbstractSlider::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QAbstractSlider::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QAbstractSlider::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QAbstractSlider::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void keyPressEvent_protected(QKeyEvent * ev) { QAbstractSlider::keyPressEvent(ev); }
    void keyPressEvent(QKeyEvent * ev) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QAbstractSlider::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QAbstractSlider::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QAbstractSlider::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QAbstractSlider::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QAbstractSlider::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QAbstractSlider::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QAbstractSlider::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QAbstractSlider::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, long * result) { return QAbstractSlider::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, long * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QAbstractSlider::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QAbstractSlider::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline QAbstractSlider::SliderAction repeatAction_protected() const { return QAbstractSlider::repeatAction(); }
    inline void resizeEvent_protected(QResizeEvent * event) { QAbstractSlider::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    inline void setRepeatAction_protected(QAbstractSlider::SliderAction action, int thresholdTime = 500, int repeatTime = 50) { QAbstractSlider::setRepeatAction(QAbstractSlider::SliderAction(action), thresholdTime, repeatTime); }
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QAbstractSlider::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QAbstractSlider::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void sliderChange_protected(int change) { QAbstractSlider::sliderChange(QAbstractSlider::SliderChange(change)); }
    void sliderChange(QAbstractSlider::SliderChange change) override;
    inline void tabletEvent_protected(QTabletEvent * event) { QAbstractSlider::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * arg__1) { QAbstractSlider::timerEvent(arg__1); }
    void timerEvent(QTimerEvent * arg__1) override;
    inline void updateMicroFocus_protected() { QAbstractSlider::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * e) { QAbstractSlider::wheelEvent(e); }
    void wheelEvent(QWheelEvent * e) override;
    ~QAbstractSliderWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QABSTRACTSLIDERWRAPPER_H

#  ifndef SBK_QWIDGETWRAPPER_H
#  define SBK_QWIDGETWRAPPER_H

// Inherited base class:
class QWidgetWrapper : public QWidget
{
public:
    QWidgetWrapper(QWidget * parent = nullptr, QFlags<Qt::WindowType> f = Qt::WindowFlags());
    inline void actionEvent_protected(QActionEvent * event) { QWidget::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * event) { QWidget::changeEvent(event); }
    void changeEvent(QEvent * event) override;
    inline void childEvent_protected(QChildEvent * event) { QWidget::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QWidget::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QWidget::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QWidget::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QWidget::create(arg__1, initializeWindow, destroyOldWindow); }
    inline void customEvent_protected(QEvent * event) { QWidget::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QWidget::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QWidget::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QWidget::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QWidget::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QWidget::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QWidget::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEvent * event) { QWidget::enterEvent(event); }
    void enterEvent(QEvent * event) override;
    inline bool event_protected(QEvent * event) { return QWidget::event(event); }
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QWidget::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QWidget::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QWidget::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QWidget::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QWidget::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QWidget::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QWidget::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QWidget::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline bool isSignalConnected_protected(const QMetaMethod & signal) const { return QWidget::isSignalConnected(signal); }
    inline void keyPressEvent_protected(QKeyEvent * event) { QWidget::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QWidget::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QWidget::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QWidget::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QWidget::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QWidget::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QWidget::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QWidget::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QWidget::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, long * result) { return QWidget::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, long * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QWidget::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline int receivers_protected(const char * signal) const { return QWidget::receivers(signal); }
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QWidget::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline void resizeEvent_protected(QResizeEvent * event) { QWidget::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    inline QObject * sender_protected() const { return QWidget::sender(); }
    inline int senderSignalIndex_protected() const { return QWidget::senderSignalIndex(); }
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QWidget::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QWidget::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void tabletEvent_protected(QTabletEvent * event) { QWidget::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * event) { QWidget::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    inline void updateMicroFocus_protected() { QWidget::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * event) { QWidget::wheelEvent(event); }
    void wheelEvent(QWheelEvent * event) override;
    ~QWidgetWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QWIDGETWRAPPER_H

#  ifndef SBK_QPAINTDEVICEWRAPPER_H
#  define SBK_QPAINTDEVICEWRAPPER_H

// Inherited base class:
class QPaintDeviceWrapper : public QPaintDevice
{
public:
    QPaintDeviceWrapper() noexcept;
    int devType() const override;
    inline void initPainter_protected(QPainter * painter) const { QPaintDevice::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric metric) const { return QPaintDevice::metric(QPaintDevice::PaintDeviceMetric(metric)); }
    int metric(QPaintDevice::PaintDeviceMetric metric) const override;
    QPaintEngine * paintEngine() const override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QPaintDevice::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline QPainter * sharedPainter_protected() const { return QPaintDevice::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline ushort  protected_painters_getter() { return  this->QPaintDevice::painters; }
    inline void protected_painters_setter(ushort value) { QPaintDevice::painters = value; }
    ~QPaintDeviceWrapper();
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QPAINTDEVICEWRAPPER_H

#endif // SBK_QRANGESLIDERWRAPPER_H

