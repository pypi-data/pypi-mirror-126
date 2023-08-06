#ifndef SBK_QTVARIANTPROPERTYWRAPPER_H
#define SBK_QTVARIANTPROPERTYWRAPPER_H

#include <qtvariantproperty.h>

class QtVariantPropertyWrapper : public QtVariantProperty
{
public:
    QtVariantPropertyWrapper(QtVariantPropertyManager * manager);
    inline void propertyChanged_protected() { QtVariantProperty::propertyChanged(); }
    ~QtVariantPropertyWrapper();
    static void pysideInitQtMetaTypes();
};

#  ifndef SBK_QTPROPERTYWRAPPER_H
#  define SBK_QTPROPERTYWRAPPER_H

// Inherited base class:
class QtPropertyWrapper : public QtProperty
{
public:
    QtPropertyWrapper(QtAbstractPropertyManager * manager);
    inline void propertyChanged_protected() { QtProperty::propertyChanged(); }
    ~QtPropertyWrapper();
    static void pysideInitQtMetaTypes();
};

#  endif // SBK_QTPROPERTYWRAPPER_H

#endif // SBK_QTVARIANTPROPERTYWRAPPER_H

