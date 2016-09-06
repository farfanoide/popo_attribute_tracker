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

    def _track_fields(self):
        self._original_attrs = {}

        for attr in self.TRACKED_ATTRS:
            self._original_attrs[attr] = self.__dict__.get(attr, None)

    def reset_tracker(self):
        self._track_fields()

    def initialize_tracker(self, fields=None):

        if fields:
            self.TRACKED_ATTRS = fields

        if not hasattr(self, 'TRACKED_ATTRS'):
            raise TrackerConfigurationError

        self._track_fields()

    def _field_changed(self, field):
        return self._original_attrs.get(field) != getattr(self, field, None)

    def has_changed(self, field=None):

        if field:
            return self._field_changed(field)

        return any(self._field_changed(field) for field in self.TRACKED_ATTRS)

    def previous(self, field):
        return self._original_attrs.get(field)



