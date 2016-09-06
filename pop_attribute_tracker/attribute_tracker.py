# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

__all__ = (
    'AttributeTrackerMixin',
    'TrackerConfigurationError',
)


class TrackerConfigurationError(Exception):

    msg = "Need TRACKED_FIELDS attribute."

    def __str__(self):
        return self.msg


class AttributeTrackerMixin(object):

    def _track_fields(self):
        for attr_name in self.TRACKED_FIELDS:
            self._original_attrs[attr_name] = self.__dict__.get(attr_name)

    def reset_tracker(self):
        self._track_fields()

    def initialize_tracker(self, fields=None):

        if fields:
            self.TRACKED_FIELDS = fields

        if not hasattr(self, 'TRACKED_FIELDS'):
            raise TrackerConfigurationError

        self._original_attrs = {}

        self._track_fields()

    def _field_changed(self, field):
        return self._original_attrs.get(field) != getattr(self, field)

    def has_changed(self, field=None):

        if field:
            return self._field_changed(field)

        return any(self._field_changed(f) for f in self._original_attrs.keys())

    def previous(self, field):
        return self._original_attrs.get(field)

