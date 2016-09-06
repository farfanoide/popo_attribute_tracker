# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

__all__ = (
    'AttributeTrackerMixin',
    'TrackerConfigurationError',
)


class TrackerConfigurationError(Exception):

    msg = "Need TRACKED_ATTRS attribute."

    def __str__(self):
        return self.msg


class AttributeTrackerMixin(object):

    def _track_attrs(self):
        self._original_attrs = {}

        for attr in self.TRACKED_ATTRS:
            self._original_attrs[attr] = self.__dict__.get(attr, None)

    def reset_tracker(self):
        self._track_attrs()

    def initialize_tracker(self, attrs=None):

        if attrs:
            self.TRACKED_ATTRS = attrs

        if not hasattr(self, 'TRACKED_ATTRS'):
            raise TrackerConfigurationError

        self._track_attrs()

    def _attr_changed(self, attr):
        return self._original_attrs.get(attr) != getattr(self, attr, None)

    def has_changed(self, attr=None):

        if attr:
            return self._attr_changed(attr)

        return any(self._attr_changed(attr) for attr in self.TRACKED_ATTRS)

    def previous(self, attr):
        return self._original_attrs.get(attr)




