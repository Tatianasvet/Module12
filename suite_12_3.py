import unittest
import tests_12_3

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

suite = unittest.TextTestRunner(verbosity=2)
suite.run(testST)
