import unittest
import test_homework1_12
import test_homework2_12

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_homework2_12.TournamentTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_homework1_12.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)