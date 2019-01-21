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
        self.assertEqual('VCPU', rc.STANDARDS[0])
        self.assertEqual('DISK_GB', rc.STANDARDS[2])

    def test_id_mapping_symbols(self):
        self.assertEqual(rc.VCPU, rc.STANDARDS[0])
        self.assertEqual(rc.DISK_GB, rc.STANDARDS[2])

    def test_standards_tail(self):
        """A sanity check that developers are paying attention.

        When one or more standard classes are added, change the expected
        last class to the last one added and the length to the new length
        of rc.STANDARDS.

        If you arrive here because you've run the tests and they've failed
        it's possible you've added some standard classes and not thought
        about their order. You _must_ add new standard classs at the end
        of the STANDARDS list, otherwise database ids will get confused
        in the placement service.
        """
        expected_last_class = rc.PCPU
        expected_length = 15
        self.assertEqual(expected_last_class, rc.STANDARDS[-1])
        self.assertEqual(expected_length, len(rc.STANDARDS))
