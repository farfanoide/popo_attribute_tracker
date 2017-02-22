POPO Attribute Tracker
======================

This is a simple mixin to ease tracking of attribute changes in any :shit: POPO
(Plain Old Python Object). It's designed to be as simple and unobtrusive as
possible.

[![Build Status](https://travis-ci.org/farfanoide/popo_attribute_tracker.svg?branch=master)](https://travis-ci.org/farfanoide/popo_attribute_tracker)

Installation
------------

Download from github or via pip:

```bash
pip install popo_attribute_tracker
```

Usage
-----

Simply inherit from `AttributeTrackerMixin`, configure the `TRACKED_ATTRS`
as a list of attribute names to track and initialize the tracker.

While initializing the tracker you may optionally send an iterable containing
names of attributes to track in case you need to get them dynamically

```python
# Example

from popo_attribute_tracker.attribute_tracker import AttributeTrackerMixin

class Alice(AttributeTrackerMixin):

    TRACKED_ATTRS = ('name', 'last_name')

    def __init__(self, *args, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        self.initialize_tracker()

alice = Alice(name='Alice', last_name='Liddell')

# Ask if any attribute changed
alice.has_changed()       #=> False

alice.name = 'Bob'
alice.has_changed()       #=> True

# You can also ask if a specific attribute has changed
alice.has_changed('name') #=> True

# Get previous value for changed attribute
alice.previous('name')    #=> 'Alice'

# Reset the tracker, normally after saving to a DB
alice.reset_tracker()
```

Django compatibility
--------------------

If you want to use it in a django model you could use django [Signals][] to
initialize and reset the tracker.

```python
@receiver(signals.post_init, sender=SomeDjangoModel)
def initialize_tracker(sender, instance, **kwargs):
    instance.initialize_tracker()
```

```python
@receiver(signals.post_save, sender=SomeDjangoModel)
def reset_tracker(sender, instance, **kwargs):
    instance.reset_tracker()
```

[Signals]: https://docs.djangoproject.com/en/dev/topics/signals/

Tests
-----

Install requirements and run `py.test`

```bash
pip install -r requirements.txt

py.test
```

Contributing
------------

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

License
-------

See the [LICENSE](LICENSE).
