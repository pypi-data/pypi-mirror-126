/*
 * SPDX-FileCopyrightText: 2006-2021 Istituto Italiano di Tecnologia (IIT)
 * SPDX-License-Identifier: BSD-3-Clause
 */

#ifndef YARP_ROBOTINTERFACE_IMPL_XMLREADERFILEV3_H
#define YARP_ROBOTINTERFACE_IMPL_XMLREADERFILEV3_H

#include <yarp/robotinterface/impl/XMLReaderFileVx.h>

#include <string>

namespace yarp::robotinterface {
class XMLReaderResult;
} // namespace yarp::robotinterface

namespace yarp::robotinterface::impl {

class XMLReaderFileV3 : public XMLReaderFileVx
{
public:
    XMLReaderFileV3();
    ~XMLReaderFileV3() override;

    yarp::robotinterface::XMLReaderResult getRobotFromFile(const std::string& filename,
                                                                         const yarp::os::Searchable& config,
                                                                         bool verbose = false) override;
    yarp::robotinterface::XMLReaderResult getRobotFromString(const std::string& xmlString,
                                                                           const yarp::os::Searchable& config,
                                                                           bool verbose = false) override;

private:
    class Private;
    Private* const mPriv;
};

} // namespace yarp::robotinterface::impl

#endif // YARP_ROBOTINTERFACE_XMLREADERFILEV3_H
