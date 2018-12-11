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

"""
test_os_resource_classes
----------------------------------

Tests for `os_resource_classes` module.
"""

import os_resource_classes as rc
from os_resource_classes.tests import base


class TestOs_resource_classes(base.TestCase):

    def test_id_mapping_strings(self):
        self.assertEqual('VCPU', rc.ORDERED_CLASSES[0])
        self.assertEqual('DISK_GB', rc.ORDERED_CLASSES[2])

    def test_id_mapping_symbols(self):
        self.assertEqual(rc.VCPU, rc.ORDERED_CLASSES[0])
        self.assertEqual(rc.DISK_GB, rc.ORDERED_CLASSES[2])
