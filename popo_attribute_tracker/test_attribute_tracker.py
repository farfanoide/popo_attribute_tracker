# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from unittest import TestCase

from .attribute_tracker import AttributeTrackerMixin, TrackerConfigurationError


class AttributeTrackerMixinTest(TestCase):

    def setUp(self):
        self.tracker = AttributeTrackerMixin()
        self.tracker.first_name = 'John'
        self.tracker.initialize_tracker(['first_name'])

    def test_it_saves_original_attrs_dict_as_copy(self):
        self.assertTrue(hasattr(self.tracker, '_original_attrs'))

    def test_it_doesnt_change_original_attrs_when_updated(self):
        self.tracker.first_name = 'Jane'
        self.assertEqual(self.tracker._original_attrs.get('first_name'), 'John')

    def test_it_knows_if_single_attr_has_changed(self):
        self.tracker.first_name = 'Lalala'
        self.assertTrue(self.tracker.has_changed('first_name'))

    def test_it_knows_if_no_attr_have_changed(self):
        self.assertFalse(self.tracker.has_changed())

    def test_it_knows_if_any_attr_has_changed(self):
        self.tracker.first_name = 'Jane'
        self.assertTrue(self.tracker.has_changed())

    def test_it_knows_how_to_return_previous_value_for_field(self):
        self.assertEqual(self.tracker.previous('first_name'), 'John')

    def test_it_knows_how_to_return_previous_value_for_field_after_it_has_changed(self):
        self.tracker.first_name = 'Jane'
        self.assertEqual(self.tracker.previous('first_name'), 'John')

    def test_it_can_reset_itself(self):
        self.tracker.first_name = 'Jane'
        self.tracker.reset_tracker()
        self.assertFalse(self.tracker.has_changed())

    def test_it_tracks_only_specified_attrs(self):
        self.tracker.initialize_tracker(['field', 'names', 'to', 'track'])
        self.assertEqual(self.tracker.TRACKED_ATTRS, ['field', 'names', 'to', 'track'])

    def test_it_doesnt_break_if_asked_about_nonexistent_attribute(self):
        self.tracker.initialize_tracker(['a'])
        self.assertFalse(self.tracker.has_changed('a'))

    def test_it_raises_error_if_not_configured_correctly(self):
        tracker = AttributeTrackerMixin()
        with self.assertRaises(TrackerConfigurationError):
            tracker.initialize_tracker()
