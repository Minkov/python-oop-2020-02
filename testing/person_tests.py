import unittest

from person import Student


class StudentTests(unittest.TestCase):
    def test_get_info__when_name_is_correct__should_return_with_correct_name(self):
        # arrange
        name = 'Test User'
        s = Student(name)
        expected = f'Hello, I am {name}'

        # act
        actual = s.get_info()

        # assert
        self.assertEqual(actual, expected)

    def test_get_info__when_name_is_None__should_raise_exception(self):
        with self.assertRaises(Exception) as context:
            Student(None)

        self.assertTrue('Name cannot be None' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
