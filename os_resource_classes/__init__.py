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
ORDERED_CLASSES = [
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
]

# Namespace used for custom resource classes
CUSTOM_NAMESPACE = 'CUSTOM_'

def is_custom(resource_class):
    return resource_class.startswith(CUSTOM_NAMESPACE)


# Set symbols that match resource class name strings.
package = sys.modules[__name__]
for resource_class in ORDERED_CLASSES:
    setattr(package, resource_class, resource_class)
