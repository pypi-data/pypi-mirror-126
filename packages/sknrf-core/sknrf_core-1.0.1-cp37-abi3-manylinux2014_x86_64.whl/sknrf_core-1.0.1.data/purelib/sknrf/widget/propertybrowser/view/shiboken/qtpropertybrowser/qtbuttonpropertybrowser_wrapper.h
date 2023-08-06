#ifndef SBK_QTBUTTONPROPERTYBROWSERWRAPPER_H
#define SBK_QTBUTTONPROPERTYBROWSERWRAPPER_H

#include <qtbuttonpropertybrowser.h>

namespace PySide { class DynamicQMetaObject; }

class QtButtonPropertyBrowserWrapper : public QtButtonPropertyBrowser
{
public:
    QtButtonPropertyBrowserWrapper(QWidget * parent = nullptr);
    inline void actionEvent_protected(QActionEvent * event) { QtButtonPropertyBrowser::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * event) { QtButtonPropertyBrowser::changeEvent(event); }
    void changeEvent(QEvent * event) override;
    inline void childEvent_protected(QChildEvent * event) { QtButtonPropertyBrowser::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QtButtonPropertyBrowser::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QtButtonPropertyBrowser::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QtButtonPropertyBrowser::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QtButtonPropertyBrowser::create(arg__1, initializeWindow, destroyOldWindow); }
    inline QWidget * createAttributeEditor_protected(QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtButtonPropertyBrowser::createAttributeEditor(property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtProperty * property, QWidget * parent) { return QtButtonPropertyBrowser::createEditor(property, parent); }
    QWidget * createEditor(QtProperty * property, QWidget * parent) override;
    inline void customEvent_protected(QEvent * event) { QtButtonPropertyBrowser::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QtButtonPropertyBrowser::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QtButtonPropertyBrowser::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QtButtonPropertyBrowser::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QtButtonPropertyBrowser::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QtButtonPropertyBrowser::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QtButtonPropertyBrowser::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEvent * event) { QtButtonPropertyBrowser::enterEvent(event); }
    void enterEvent(QEvent * event) override;
    inline bool event_protected(QEvent * event) { return QtButtonPropertyBrowser::event(event); }
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QtButtonPropertyBrowser::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QtButtonPropertyBrowser::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QtButtonPropertyBrowser::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QtButtonPropertyBrowser::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QtButtonPropertyBrowser::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QtButtonPropertyBrowser::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QtButtonPropertyBrowser::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QtButtonPropertyBrowser::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void itemChanged_protected(QtBrowserItem * item) { QtButtonPropertyBrowser::itemChanged(item); }
    void itemChanged(QtBrowserItem * item) override;
    inline void itemInserted_protected(QtBrowserItem * item, QtBrowserItem * afterItem) { QtButtonPropertyBrowser::itemInserted(item, afterItem); }
    void itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem) override;
    inline void itemRemoved_protected(QtBrowserItem * item) { QtButtonPropertyBrowser::itemRemoved(item); }
    void itemRemoved(QtBrowserItem * item) override;
    inline void keyPressEvent_protected(QKeyEvent * event) { QtButtonPropertyBrowser::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QtButtonPropertyBrowser::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QtButtonPropertyBrowser::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QtButtonPropertyBrowser::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QtButtonPropertyBrowser::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QtButtonPropertyBrowser::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QtButtonPropertyBrowser::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QtButtonPropertyBrowser::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QtButtonPropertyBrowser::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, long * result) { return QtButtonPropertyBrowser::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, long * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QtButtonPropertyBrowser::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QtButtonPropertyBrowser::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline void resizeEvent_protected(QResizeEvent * event) { QtButtonPropertyBrowser::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QtButtonPropertyBrowser::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QtButtonPropertyBrowser::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void tabletEvent_protected(QTabletEvent * event) { QtButtonPropertyBrowser::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * event) { QtButtonPropertyBrowser::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    inline void updateMicroFocus_protected() { QtButtonPropertyBrowser::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * event) { QtButtonPropertyBrowser::wheelEvent(event); }
    void wheelEvent(QWheelEvent * event) override;
    ~QtButtonPropertyBrowserWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  ifndef SBK_QTABSTRACTPROPERTYBROWSERWRAPPER_H
#  define SBK_QTABSTRACTPROPERTYBROWSERWRAPPER_H

// Inherited base class:
class QtAbstractPropertyBrowserWrapper : public QtAbstractPropertyBrowser
{
public:
    QtAbstractPropertyBrowserWrapper(QWidget * parent = nullptr);
    inline void actionEvent_protected(QActionEvent * event) { QtAbstractPropertyBrowser::actionEvent(event); }
    void actionEvent(QActionEvent * event) override;
    inline void changeEvent_protected(QEvent * event) { QtAbstractPropertyBrowser::changeEvent(event); }
    void changeEvent(QEvent * event) override;
    inline void childEvent_protected(QChildEvent * event) { QtAbstractPropertyBrowser::childEvent(event); }
    void childEvent(QChildEvent * event) override;
    inline void closeEvent_protected(QCloseEvent * event) { QtAbstractPropertyBrowser::closeEvent(event); }
    void closeEvent(QCloseEvent * event) override;
    inline void connectNotify_protected(const QMetaMethod & signal) { QtAbstractPropertyBrowser::connectNotify(signal); }
    void connectNotify(const QMetaMethod & signal) override;
    inline void contextMenuEvent_protected(QContextMenuEvent * event) { QtAbstractPropertyBrowser::contextMenuEvent(event); }
    void contextMenuEvent(QContextMenuEvent * event) override;
    inline void create_protected(WId arg__1 = 0, bool initializeWindow = true, bool destroyOldWindow = true) { QtAbstractPropertyBrowser::create(arg__1, initializeWindow, destroyOldWindow); }
    inline QWidget * createAttributeEditor_protected(QtProperty * property, QWidget * parent, BrowserCol attribute) { return QtAbstractPropertyBrowser::createAttributeEditor(property, parent, BrowserCol(attribute)); }
    QWidget * createAttributeEditor(QtProperty * property, QWidget * parent, BrowserCol attribute) override;
    inline QWidget * createEditor_protected(QtProperty * property, QWidget * parent) { return QtAbstractPropertyBrowser::createEditor(property, parent); }
    QWidget * createEditor(QtProperty * property, QWidget * parent) override;
    inline void customEvent_protected(QEvent * event) { QtAbstractPropertyBrowser::customEvent(event); }
    void customEvent(QEvent * event) override;
    inline void destroy_protected(bool destroyWindow = true, bool destroySubWindows = true) { QtAbstractPropertyBrowser::destroy(destroyWindow, destroySubWindows); }
    int devType() const override;
    inline void disconnectNotify_protected(const QMetaMethod & signal) { QtAbstractPropertyBrowser::disconnectNotify(signal); }
    void disconnectNotify(const QMetaMethod & signal) override;
    inline void dragEnterEvent_protected(QDragEnterEvent * event) { QtAbstractPropertyBrowser::dragEnterEvent(event); }
    void dragEnterEvent(QDragEnterEvent * event) override;
    inline void dragLeaveEvent_protected(QDragLeaveEvent * event) { QtAbstractPropertyBrowser::dragLeaveEvent(event); }
    void dragLeaveEvent(QDragLeaveEvent * event) override;
    inline void dragMoveEvent_protected(QDragMoveEvent * event) { QtAbstractPropertyBrowser::dragMoveEvent(event); }
    void dragMoveEvent(QDragMoveEvent * event) override;
    inline void dropEvent_protected(QDropEvent * event) { QtAbstractPropertyBrowser::dropEvent(event); }
    void dropEvent(QDropEvent * event) override;
    inline void enterEvent_protected(QEvent * event) { QtAbstractPropertyBrowser::enterEvent(event); }
    void enterEvent(QEvent * event) override;
    inline bool event_protected(QEvent * event) { return QtAbstractPropertyBrowser::event(event); }
    bool event(QEvent * event) override;
    bool eventFilter(QObject * watched, QEvent * event) override;
    inline void focusInEvent_protected(QFocusEvent * event) { QtAbstractPropertyBrowser::focusInEvent(event); }
    void focusInEvent(QFocusEvent * event) override;
    inline bool focusNextChild_protected() { return QtAbstractPropertyBrowser::focusNextChild(); }
    inline bool focusNextPrevChild_protected(bool next) { return QtAbstractPropertyBrowser::focusNextPrevChild(next); }
    bool focusNextPrevChild(bool next) override;
    inline void focusOutEvent_protected(QFocusEvent * event) { QtAbstractPropertyBrowser::focusOutEvent(event); }
    void focusOutEvent(QFocusEvent * event) override;
    inline bool focusPreviousChild_protected() { return QtAbstractPropertyBrowser::focusPreviousChild(); }
    bool hasHeightForWidth() const override;
    int heightForWidth(int arg__1) const override;
    inline void hideEvent_protected(QHideEvent * event) { QtAbstractPropertyBrowser::hideEvent(event); }
    void hideEvent(QHideEvent * event) override;
    inline void initPainter_protected(QPainter * painter) const { QtAbstractPropertyBrowser::initPainter(painter); }
    void initPainter(QPainter * painter) const override;
    inline void inputMethodEvent_protected(QInputMethodEvent * event) { QtAbstractPropertyBrowser::inputMethodEvent(event); }
    void inputMethodEvent(QInputMethodEvent * event) override;
    QVariant inputMethodQuery(Qt::InputMethodQuery arg__1) const override;
    inline void itemChanged_protected(QtBrowserItem * item) { itemChanged(item); }
    void itemChanged(QtBrowserItem * item) override;
    inline void itemInserted_protected(QtBrowserItem * item, QtBrowserItem * afterItem) { itemInserted(item, afterItem); }
    void itemInserted(QtBrowserItem * item, QtBrowserItem * afterItem) override;
    inline void itemRemoved_protected(QtBrowserItem * item) { itemRemoved(item); }
    void itemRemoved(QtBrowserItem * item) override;
    inline void keyPressEvent_protected(QKeyEvent * event) { QtAbstractPropertyBrowser::keyPressEvent(event); }
    void keyPressEvent(QKeyEvent * event) override;
    inline void keyReleaseEvent_protected(QKeyEvent * event) { QtAbstractPropertyBrowser::keyReleaseEvent(event); }
    void keyReleaseEvent(QKeyEvent * event) override;
    inline void leaveEvent_protected(QEvent * event) { QtAbstractPropertyBrowser::leaveEvent(event); }
    void leaveEvent(QEvent * event) override;
    const QMetaObject * metaObject() const override;
    inline int metric_protected(QPaintDevice::PaintDeviceMetric arg__1) const { return QtAbstractPropertyBrowser::metric(QPaintDevice::PaintDeviceMetric(arg__1)); }
    int metric(QPaintDevice::PaintDeviceMetric arg__1) const override;
    QSize minimumSizeHint() const override;
    inline void mouseDoubleClickEvent_protected(QMouseEvent * event) { QtAbstractPropertyBrowser::mouseDoubleClickEvent(event); }
    void mouseDoubleClickEvent(QMouseEvent * event) override;
    inline void mouseMoveEvent_protected(QMouseEvent * event) { QtAbstractPropertyBrowser::mouseMoveEvent(event); }
    void mouseMoveEvent(QMouseEvent * event) override;
    inline void mousePressEvent_protected(QMouseEvent * event) { QtAbstractPropertyBrowser::mousePressEvent(event); }
    void mousePressEvent(QMouseEvent * event) override;
    inline void mouseReleaseEvent_protected(QMouseEvent * event) { QtAbstractPropertyBrowser::mouseReleaseEvent(event); }
    void mouseReleaseEvent(QMouseEvent * event) override;
    inline void moveEvent_protected(QMoveEvent * event) { QtAbstractPropertyBrowser::moveEvent(event); }
    void moveEvent(QMoveEvent * event) override;
    inline bool nativeEvent_protected(const QByteArray & eventType, void * message, long * result) { return QtAbstractPropertyBrowser::nativeEvent(eventType, message, result); }
    bool nativeEvent(const QByteArray & eventType, void * message, long * result) override;
    QPaintEngine * paintEngine() const override;
    inline void paintEvent_protected(QPaintEvent * event) { QtAbstractPropertyBrowser::paintEvent(event); }
    void paintEvent(QPaintEvent * event) override;
    inline QPaintDevice * redirected_protected(QPoint * offset) const { return QtAbstractPropertyBrowser::redirected(offset); }
    QPaintDevice * redirected(QPoint * offset) const override;
    inline void resizeEvent_protected(QResizeEvent * event) { QtAbstractPropertyBrowser::resizeEvent(event); }
    void resizeEvent(QResizeEvent * event) override;
    void setVisible(bool visible) override;
    inline QPainter * sharedPainter_protected() const { return QtAbstractPropertyBrowser::sharedPainter(); }
    QPainter * sharedPainter() const override;
    inline void showEvent_protected(QShowEvent * event) { QtAbstractPropertyBrowser::showEvent(event); }
    void showEvent(QShowEvent * event) override;
    QSize sizeHint() const override;
    inline void tabletEvent_protected(QTabletEvent * event) { QtAbstractPropertyBrowser::tabletEvent(event); }
    void tabletEvent(QTabletEvent * event) override;
    inline void timerEvent_protected(QTimerEvent * event) { QtAbstractPropertyBrowser::timerEvent(event); }
    void timerEvent(QTimerEvent * event) override;
    inline void updateMicroFocus_protected() { QtAbstractPropertyBrowser::updateMicroFocus(); }
    inline void wheelEvent_protected(QWheelEvent * event) { QtAbstractPropertyBrowser::wheelEvent(event); }
    void wheelEvent(QWheelEvent * event) override;
    ~QtAbstractPropertyBrowserWrapper();
public:
    int qt_metacall(QMetaObject::Call call, int id, void **args) override;
    void *qt_metacast(const char *_clname) override;
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QTABSTRACTPROPERTYBROWSERWRAPPER_H

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

#endif // SBK_QTBUTTONPROPERTYBROWSERWRAPPER_H

