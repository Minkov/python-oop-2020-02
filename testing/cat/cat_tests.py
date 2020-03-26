import unittest

from cat import Cat


class CatTest(unittest.TestCase):
    def test_eat_should_increase_size(self):
        name = 'Test cat'
        cat = Cat(name)
        original_size = cat.size
        cat.eat()

        self.assertEqual(cat.size, original_size + 1)

    def test_eat_should_set_sleepy_to_True(self):
        name = 'Test cat'
        cat = Cat(name)
        original_size = cat.size
        cat.eat()

        self.assertTrue(cat.sleepy)

    def test_eat_when_already_fed_should_raise_error(self):
        name = 'Test cat'
        cat = Cat(name)
        cat.eat()

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertIsNotNone(context.exception)

    def test_sleep_when_NOT_fed_should_raise_error(self):
        name = 'Test cat'
        cat = Cat(name)

        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_sleep_when_fed_should_set_sleepy_to_False(self):
        name = 'Test cat'
        cat = Cat(name)

        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


