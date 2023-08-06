#ifndef QRANGESLIDER_H
#define QRANGESLIDER_H

#include "sknrfconfig.h"
#include <QSlider>

#if defined(QRANGESLIDER_COMPILE_LIBRARY)
#  define QRANGESLIDER_DECL  Q_DECL_EXPORT
#elif defined(QRANGESLIDER_USE_LIBRARY)
#  define QRANGESLIDER_DECL Q_DECL_IMPORT
#else
#  define QRANGESLIDER_DECL
#endif

class QRangeSliderPrivate;

class QRANGESLIDER_DECL QRangeSlider : public QSlider
{
    Q_OBJECT
    Q_DECLARE_PRIVATE(QRangeSlider)
    Q_PROPERTY(int lowerValue READ lowerValue WRITE setLowerValue)
    Q_PROPERTY(int upperValue READ upperValue WRITE setUpperValue)
    Q_PROPERTY(int lowerPosition READ lowerPosition WRITE setLowerPosition)
    Q_PROPERTY(int upperPosition READ upperPosition WRITE setUpperPosition)
    Q_PROPERTY(HandleMovementMode handleMovementMode READ handleMovementMode WRITE setHandleMovementMode)
    Q_ENUMS(HandleMovementMode)

public:
    explicit QRangeSlider(QWidget *parent = 0);
    explicit QRangeSlider(Qt::Orientation orientation, QWidget* parent = 0);
    virtual ~QRangeSlider();

    enum HandleMovementMode
    {
        FreeMovement,
        NoCrossing,
        NoOverlapping
    };

    enum SpanHandle
    {
        NoHandle,
        LowerHandle,
        UpperHandle
    };

    HandleMovementMode handleMovementMode() const;
    void setHandleMovementMode(HandleMovementMode mode);

    int lowerValue() const;
    int upperValue() const;

    int lowerPosition() const;
    int upperPosition() const;

public Q_SLOTS:
    void setLowerValue(int lower);
    void setUpperValue(int upper);
    void setSpan(int lower, int upper);

    void setLowerPosition(int lower);
    void setUpperPosition(int upper);

Q_SIGNALS:
    void spanChanged(int lower, int upper);
    void lowerValueChanged(int lower);
    void upperValueChanged(int upper);

    void lowerPositionChanged(int lower);
    void upperPositionChanged(int upper);

    void sliderPressed(SpanHandle handle);

protected:
    virtual void keyPressEvent(QKeyEvent* event);
    virtual void mousePressEvent(QMouseEvent* event);
    virtual void mouseMoveEvent(QMouseEvent* event);
    virtual void mouseReleaseEvent(QMouseEvent* event);
    virtual void paintEvent(QPaintEvent* event);

private:
    QRangeSliderPrivate *d_ptr;
};

#endif // QRANGESLIDER_H

