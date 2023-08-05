/*
 * SPDX-FileCopyrightText: 2006-2021 Istituto Italiano di Tecnologia (IIT)
 * SPDX-FileCopyrightText: 2006-2010 RobotCub Consortium
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <yarp/os/PortInfo.h>


yarp::os::PortInfo::PortInfo() :
        tag(PORTINFO_NULL),
        incoming(false),
        created(true),
        message("no information")
{
}
