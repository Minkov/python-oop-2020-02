import unittest

from worker import Worker

class BaseTestCase(unittest.TestCase):
    def assertContains(self, value, text):
        self.assertTrue(value in str(text))

class WorkerTests(BaseTestCase):
    def test_init_when_correct_name_salary_energy_should_set_correct_attributes_and_money_0(self):
        name = 'Test User'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)

        self.assertEqual(worker.name, name)
        self.assertEqual(worker.salary, salary)
        self.assertEqual(worker.energy, energy)
        self.assertEqual(worker.money, 0)

    def test_rest_should_increment_energy(self):
        name = 'Test User'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)

        worker.rest()

        self.assertEqual(worker.energy, energy + 1)

    def test_work_when_energy_is_0_should_raise_error(self):
        name = 'Test User'
        salary = 1000
        energy = 0
        worker = Worker(name, salary, energy)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertIsNotNone(context.exception)
        self.assertContains(f'{name} does not have enough energy.', context.exception)

    def test_work_when_energy_is_greater_than_0_should_increase_money_by_salary(self):
        name = 'Test User'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.money, worker.salary)
        worker.work()
        self.assertEqual(worker.money, 2 * worker.salary)

    def test_work_when_energy_is_greater_than_0_should_decrease_energy(self):
        name = 'Test User'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)

        worker.work()

        self.assertEqual(worker.energy, energy - 1)

    def test_get_info_should_return_correct_result(self):
        name = 'Test User'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)
        expected = f'{name} has saved 0 money.'
        actual = worker.get_info()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
