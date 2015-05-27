"""Tests for smartchoices."""

import unittest

import smartchoices


class TestChoices(unittest.TestCase):
    """Tests for smartchoices.Choice objects."""

    def test_choice_defaults_to_0(self):
        """A Choice starts at."""

        class ChoiceObj(smartchoices.Choices):
            MY_CHOICE = smartchoices.Choice()

        self.assertEqual(0, ChoiceObj.MY_CHOICE)

    def test_choice_name_default(self):
        """A Choice has a human-readable name."""

        class ChoiceObj(smartchoices.Choices):
            MY_CHOICE = smartchoices.Choice()

        # We need the second element of the only tuple
        # from the choices.
        actual_name = ChoiceObj.choices[0][1]
        self.assertEqual('MY_CHOICE', actual_name)

    def test_choices_smart_name(self):
        """Choices have smart names."""

        class ChoiceObj(smartchoices.Choices):
            MY_CHOICE = smartchoices.Choice()

            class Meta:
                smart_names = True

        # We need the second element of the only tuple
        # from the choices.
        actual_name = ChoiceObj.choices[0][1]
        self.assertEqual('My Choice', actual_name)

    def test_choice_defined_name(self):
        """A Choice specifies a name."""
        name = "What's in a name?"

        class ChoiceObj(smartchoices.Choices):
            MY_CHOICE = smartchoices.Choice(name=name)

        # We need the second element of the only tuple
        # from the choices.
        actual_name = ChoiceObj.choices[0][1]
        self.assertEqual(name, actual_name)

    def test_choice_manual_numbering(self):
        """Choices can be set to custom numbering."""

        class ChoiceObj(smartchoices.Choices):
            HIGH_STARTING_CHOICE = smartchoices.Choice(1000)
            NEXT_CHOICE = smartchoices.Choice()

        self.assertEqual(1000, ChoiceObj.HIGH_STARTING_CHOICE)
        self.assertEqual(1001, ChoiceObj.NEXT_CHOICE)


if __name__ == '__main__':
    unittest.main()
