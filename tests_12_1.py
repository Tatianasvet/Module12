import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        person = runner.Runner('name')
        for _ in range(10):
            person.walk()
        self.assertEqual(person.distance, 50)

    def test_run(self):
        person = runner.Runner('name')
        for _ in range(10):
            person.run()
        self.assertEqual(person.distance, 100)

    def test_challenge(self):
        person_1 = runner.Runner('name')
        person_2 = runner.Runner('name')
        for _ in range(10):
            person_1.run()
            person_2.walk()
        self.assertNotEqual(person_1.distance, person_2.distance)
if __name__ == "__main__":
    unittest.main()
