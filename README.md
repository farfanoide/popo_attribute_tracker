POPO Attribtue Tracker
======================

This is a simple mixin to ease tracking of attribute changes in any python
object. It's designed to be as simple as possible.

Usage
-----

Simply inherit from `POPOAttributeTrackerMixin`, configure the `TRACKED_ATTRS`
as a list of attribute names to track and initialize the tracker.

```python
# Example

from popo_attribute_tracker import AttributeTrackerMixin

class Alice(AttributeTrackerMixin):

    TRACKED_ATTRS = ('name', 'last_name')

    def __init__(self, *args, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        self.initialize_tracker()

alice = Alice(name='Alice', last_name='Liddell')

# Ask if any attribute changed
alice.has_changed() # => False

alice.name = 'Bob'
alice.has_changed()       # => True

# You can also ask if a specific attribute has changed
alice.has_changed('name') # => True

# Get previous value for changed attribute
alice.previous('name')    # => 'Alice'

# Reset the tracker, normally after saving to a DB
alice.reset_tracker()
```

If you wanted to use it in a django model you could use django Signals to
initialize and reset the tracker.

```python
@receiver(signals.post_init, sender=SomeDjangoModel)
def initialize_tracker(sender, instance, **kwargs):
    instance.initialize_tracker()
```

```python
@receiver(signals.post_init, sender=SomeDjangoModel)
def initialize_tracker(sender, instance, **kwargs):
    instance.initialize_tracker()
```

