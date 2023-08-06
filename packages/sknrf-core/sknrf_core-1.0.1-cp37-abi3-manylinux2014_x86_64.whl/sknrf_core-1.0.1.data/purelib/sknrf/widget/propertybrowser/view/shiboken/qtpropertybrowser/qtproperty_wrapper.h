#ifndef SBK_QTPROPERTYWRAPPER_H
#define SBK_QTPROPERTYWRAPPER_H

#include <qtpropertybrowser.h>

class QtPropertyWrapper : public QtProperty
{
public:
    QtPropertyWrapper(QtAbstractPropertyManager * manager);
    inline void propertyChanged_protected() { QtProperty::propertyChanged(); }
    ~QtPropertyWrapper();
    static void pysideInitQtMetaTypes();
};

#endif // SBK_QTPROPERTYWRAPPER_H

