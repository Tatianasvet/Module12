import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            person = Runner('name', speed=-5)
            logging.info(f'"test_walk" выполнен успешно')
            for _ in range(10):
                person.walk()
            self.assertEqual(person.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            person = Runner(2)
            logging.info(f'"test_run" выполнен успешно')
            for _ in range(10):
                person.run()
            self.assertEqual(person.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        person_1 = Runner('name')
        person_2 = Runner('name')
        for _ in range(10):
            person_1.run()
            person_2.walk()
        self.assertNotEqual(person_1.distance, person_2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")
