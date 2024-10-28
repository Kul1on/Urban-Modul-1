import unittest
from tests_12_3 import RunnerTest, TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
