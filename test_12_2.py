from runner_and_tournament import Runner, Tournament
import unittest
from pprint import pprint


class TournamentTest(unittest.TestCase):
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

    def test_1(self):
        start_1 = Tournament(90, self.runner_1, self.runner_3)
        self.__class__.all_results.append(start_1.start())
        self.assertTrue(self.all_results[-1][2].name == 'Ник')

    def test_2(self):
        start_2 = Tournament(90, self.runner_2, self.runner_3)
        self.__class__.all_results.append(start_2.start())
        self.assertTrue(self.all_results[-1][2].name == 'Ник')

    def test_3(self):
        start_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.__class__.all_results.append(start_3.start())
        self.assertTrue(self.all_results[-1][3].name == 'Ник')

if __name__ == "__main__":
    unittest.main()
