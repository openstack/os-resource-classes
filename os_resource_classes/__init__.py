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

import re
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
    # Resource class representing an amount of dedicated CPUs for a single
    # guest. A dedicated CPU is a physical processor that has been marked
    # to be used for a single guest only
    'PCPU',
    # Resource class representing the number of guests a compute node can
    # host with memory encrypted at the hardware level.  See
    # http://specs.openstack.org/openstack/nova-specs/specs/train/approved/amd-sev-libvirt-support.html
    'MEM_ENCRYPTION_CONTEXT',
    # An accelerator (the "VF" that can be attached to the guest) from an FPGA.
    'FPGA',
    # A physical GPU for compute offload.
    'PGPU',
]

# Namespace used for custom resource classes
CUSTOM_NAMESPACE = 'CUSTOM_'


def is_custom(resource_class):
    return resource_class.startswith(CUSTOM_NAMESPACE)


# Set symbols that match resource class name strings.
package = sys.modules[__name__]
for resource_class in STANDARDS:
    setattr(package, resource_class, resource_class)


# NOTE(efried): This method was introduced in nova in commit
# c6231539a7d39dccf3e859eda54e9336bc164c9f and copied from nova in its current
# form as of 5a4863aa152f58f6de426b3908a75c2cc1b2efca
def normalize_name(name):
    """Converts an input string to a legal* custom resource class name.

    Legal custom resource class names are prefixed with CUSTOM_ and contain
    only the characters A-Z, 0-9, and _ (underscore).

    .. note:: Does not attempt to detect an existing ``CUSTOM_`` prefix, so
              results starting with ``CUSTOM_CUSTOM_`` (etc.) are possible.

    *Does not attempt to handle length restrictions.

    :param name: A string to be converted.
    :return: A legal* custom resource class name.
    """
    if name is None:
        return None
    # Replace non-alphanumeric characters with underscores
    norm_name = re.sub('[^0-9A-Za-z]+', '_', name)
    # Bug #1762789: Do .upper after replacing non alphanumerics.
    return CUSTOM_NAMESPACE + norm_name.upper()
