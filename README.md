#  Smart Choices

## A better choices interface for Django apps


A common Django pattern is to create this complicated tuple list of tuples that
represent key/value pairs. The utilities here help make that a bit easier.


### The basics

To use, implement a `Choices` class like this:

```python
    class KennyRogers(choices.Choices):
        HOLD_EM = choices.Choice()
        FOLD_EM = choices.Choice()
        WALK_AWAY = choices.Choice()
        RUN = choices.Choice()
```

Then reference it in a model choices field like this:

    gambler = models.IntegerField(choices=KennyRogers.choices)

All values provided from a smartchoices Choices object will be intergers, so
the Django field needs to be an `IntegerField`. This is smarter for your database, too.

### Smart names

Optionally, if you'd like to expose nicer looking names for the choices, you can specify
them in the Choice creation, like so:

```python
    Choice(name="The Quick Brown Fox")
```

Or you may turn on `smart_names` in the Meta class of the Choices object like this:

```python
    class TypingClass(choices.Choices):
        class Meta:
            smart_names = True
        THE_QUICK_BROWN_FOX = choices.CHOICE()
```

### Set values like an enum

Just like enums, you may also choose to manually set the value of a choice.

```python
    class JayZProblems(choices.Choices):
        FOES_THAT_WANNA_MAKE_SURE_MY_CASKETS_CLOSED = choices.Choice()
        YOUNG = choices.Choice()
        BLACK = choices.Choice()
        HATS_REAL_LOW = choices.Choice()

        THE_B_WORD = choices.Choice(100)
        MONEY = choices.Choice()
```

Just like an enum, the counting starts 0, 1, 2, 3 and then jumps to 100, and continues on
with a value of 101 for MONEY.

