"""A smart choices interface for Django apps."""

__all__ = ['Choice', 'Choices']


def _smart_namify(name):
    """Translate the name into a more user friendly name."""
    name = name.replace('_', ' ').title()
    return name


class Choice(object):
    """A representation of a single choice."""
    order = 0

    def __init__(self, value=None, name=None):
        if value:
            self.value = Choice.order = value
        else:
            self.value = Choice.order
        Choice.order += 1

        self.name = name


class ChoicesMeta(type):
    """A metaclass for Choices."""

    def __getitem__(self, key):
        """Returns the value of the choice by its human-readable name.

        For example:
            JayZProblems['FOES_THAT_WANNA_MAKE_SURE_MY_CASKETS_CLOSED']
            will return 0.
        """
        try:
            choice_tuple_match = filter(lambda x: x[1] == key, self.choices)
            # choice_tuple_match will be something like ((0, 'book'))
            # and we only want the integer value in the tuple.
            return choice_tuple_match[0][0]
        except IndexError:
            raise KeyError(key)

    def __new__(cls, name, bases, attrs):
        Choice.order = 0  # Reset Choice.order for every new Choices class.
        choices = []

        # Normally, we'd want to iterate through the base classes. We don't, so Choices
        # won't support inheritance. Since we control the implementation, we can be
        # naive about this.
        fields = {}
        for key, val in attrs.iteritems():
            if isinstance(val, Choice):
                fields[key] = val

        for key, val in fields.iteritems():
            if isinstance(val, Choice):
                if val.name:
                    choices.append((val.value, val.name))
                else:
                    Meta = attrs.get('Meta')
                    if Meta and Meta.smart_names:
                        choices.append((val.value, _smart_namify(key)))
                    else:
                        choices.append((val.value, key))
                attrs[key] = val.value

        choices = sorted(choices, key=lambda x: x[0])
        attrs['choices'] = tuple(choices)
        return super(ChoicesMeta, cls).__new__(cls, name, bases, attrs)


class Choices(object):
    """A representation of a collection of Choices."""
    __metaclass__ = ChoicesMeta

    class Meta:
        smart_names = False
