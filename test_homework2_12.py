import unittest
import homework2_12 as h


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.r_1 = h.Runner('Усэйн', 10)
        self.r_2 = h.Runner('Андрей', 9)
        self.r_3 = h.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(f'{key} {cls.all_results[key].name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        start_1 = h.Tournament(90, self.r_1, self.r_3)
        self.__class__.all_results = start_1.start()
        self.assertTrue(self.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        start_2 = h.Tournament(90, self.r_2, self.r_3)
        self.__class__.all_results = start_2.start()
        self.assertTrue(self.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        start_3 = h.Tournament(90, self.r_1, self.r_2, self.r_3)
        self.__class__.all_results = start_3.start()
        self.assertTrue(self.all_results[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()