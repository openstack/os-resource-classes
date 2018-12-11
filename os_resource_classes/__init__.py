# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""Static symbols for resources classes used by OpenStack.

A resource class is a type of countable thing that exists in
a cloud environment, for example VCPU, DISK_GB. They are
upper case with underscores. They often include a unit in their
name.

This package provides a collection of standard resource classes
which are expected to be available in any OpenStack deployment.

There also exists a concept of custom resource classes. These
are countable types that are custom to a particular environment.
The OpenStack placement API provides a way to create these. A
custom resource class always begins with a "CUSTOM_" prefix.
"""

import sys

# NOTE(cdent): We don't expect there to be thousands of resource
# classes and we don't desire to track their history in any
# particular way so we maintain them as a list of strings ordered by
# by the time they were added to the list. From that we automatically
# create symbols in the same package. Ordering is important because
# it reflects database ids that have been used for resource classes
# prior to this package existing.


# Extend this list, if required, by adding **to the end of it**.
STANDARDS = [
    # Virtual CPUs
    'VCPU',
    # Memory Megabytes
    'MEMORY_MB',
    # Disk Gigabytes
    'DISK_GB',
    'PCI_DEVICE',
    'SRIOV_NET_VF',
    'NUMA_SOCKET',
    'NUMA_CORE',
    'NUMA_THREAD',
    'NUMA_MEMORY_MB',
    'IPV4_ADDRESS',
    'VGPU',
    'VGPU_DISPLAY_HEAD',
    # Standard resource class for network bandwidth egress measured in
    # kilobits per second.
    'NET_BW_EGR_KILOBIT_PER_SEC',
    # Standard resource class for network bandwidth ingress measured in
    # kilobits per second.
    'NET_BW_IGR_KILOBIT_PER_SEC',
]

# Namespace used for custom resource classes
CUSTOM_NAMESPACE = 'CUSTOM_'


def is_custom(resource_class):
    return resource_class.startswith(CUSTOM_NAMESPACE)


# Set symbols that match resource class name strings.
package = sys.modules[__name__]
for resource_class in STANDARDS:
    setattr(package, resource_class, resource_class)
