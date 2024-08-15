from runner_and_tournament import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        person = Runner('name')
        for _ in range(10):
            person.walk()
        self.assertEqual(person.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        person = Runner('name')
        for _ in range(10):
            person.run()
        self.assertEqual(person.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        person_1 = Runner('name')
        person_2 = Runner('name')
        for _ in range(10):
            person_1.run()
            person_2.walk()
        self.assertNotEqual(person_1.distance, person_2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
       for results in cls.all_results:
            print(results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        start_1 = Tournament(90, self.runner_1, self.runner_3)
        self.__class__.all_results.append(start_1.start())
        self.assertTrue(self.all_results[-1][2].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        start_2 = Tournament(90, self.runner_2, self.runner_3)
        self.__class__.all_results.append(start_2.start())
        self.assertTrue(self.all_results[-1][2].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        start_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.__class__.all_results.append(start_3.start())
        self.assertTrue(self.all_results[-1][3].name == 'Ник')

if __name__ == "__main__":
    unittest.main()
