import unittest
import logging
from homework4_12 import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r = Runner('name', speed=-5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                r.walk()
                self.assertEqual(r.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r = Runner(2)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                r.run()
                self.assertEqual(r.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf8', filename='runner_tests.log',
                        format="%(asktime)s | %(levelname)s | %(message)s")
