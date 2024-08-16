import homework1_12
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r = homework1_12.Runner('Maria')
        for _ in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = homework1_12.Runner('Maria')
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r_1 = homework1_12.Runner('Maria')
        r_2 = homework1_12.Runner('Andrei')
        for _ in range(10):
            r_1.run()
            r_2.walk()
        self.assertEqual(r_1.distance, r_2.distance)


if __name__ == '__main__':
    unittest.main()
