===============================
os-resource-classes
===============================

A list of standardized resource classes for OpenStack.

A resource class is a distinct type of inventory that exists in
a cloud environment, for example ``VCPU``, ``DISK_GB``. They are
upper case with underscores. They often include a unit in their
name.

This package provides a collection of symbols representing those
standard resource classes which are expected to be available in
any OpenStack deployment.

There also exists a concept of custom resource classes. These
are countable types that are custom to a particular environment.
The OpenStack `placement API`_ provides a way to create these. A
custom resource class always begins with a ``CUSTOM_`` prefix.

* Free software: Apache license
* Documentation: https://docs.openstack.org/os-resource-classes/latest
* Source: https://git.openstack.org/cgit/openstack/os-resource-classes
* Bugs: https://bugs.launchpad.net/nova

.. _placement API: https://developer.openstack.org/api-ref/placement/
