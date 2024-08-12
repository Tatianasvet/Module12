import runner_and_tournament as rt
import unittest
from pprint import pprint


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(f'{key} {cls.all_results[key].name}')

    def test_1(self):
        start_1 = rt.Tournament(90, self.runner_1, self.runner_3)
        self.__class__.all_results = start_1.start()
        self.assertTrue(self.all_results[2].name == 'Ник')

    def test_2(self):
        start_2 = rt.Tournament(90, self.runner_2, self.runner_3)
        self.__class__.all_results = start_2.start()
        self.assertTrue(self.all_results[2].name == 'Ник')

    def test_3(self):
        start_3 = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.__class__.all_results = start_3.start()
        self.assertTrue(self.all_results[3].name == 'Ник')

if __name__ == "__main__":
    unittest.main()
