/*
 * SPDX-FileCopyrightText: 2006-2021 Istituto Italiano di Tecnologia (IIT)
 * SPDX-License-Identifier: BSD-3-Clause
 */

#ifndef YARP_OS_IDL_BOTTLESTYLE_H
#define YARP_OS_IDL_BOTTLESTYLE_H

#include <yarp/os/idl/WirePortable.h>
#include <yarp/os/idl/WireReader.h>
#include <yarp/os/idl/WireWriter.h>

namespace yarp::os::idl {

template <class T>
class BottleStyle : public T
{
public:
    bool read(yarp::os::ConnectionReader& reader) override
    {
        return T::readBottle(reader);
    }

    bool write(yarp::os::ConnectionWriter& writer) const override
    {
        return T::writeBottle(writer);
    }
};

} // namespace yarp::os::idl

#endif // YARP_OS_IDL_BOTTLESTYLE_H
