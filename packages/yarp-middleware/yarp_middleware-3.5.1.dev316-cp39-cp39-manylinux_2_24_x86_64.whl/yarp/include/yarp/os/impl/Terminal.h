/*
 * SPDX-FileCopyrightText: 2006-2021 Istituto Italiano di Tecnologia (IIT)
 * SPDX-FileCopyrightText: 2006-2010 RobotCub Consortium
 * SPDX-License-Identifier: BSD-3-Clause
 */

#ifndef YARP_OS_IMPL_TERMINAL_H
#define YARP_OS_IMPL_TERMINAL_H

#include <yarp/os/api.h>

#include <string>

namespace yarp::os::impl::Terminal {

YARP_os_impl_API
bool EOFreached();

YARP_os_impl_API
std::string getStdin();

YARP_os_impl_API
std::string readString(bool* eof);

} // namespace yarp::os::impl::Terminal

#endif // YARP_OS_IMPL_TERMINAL_H
