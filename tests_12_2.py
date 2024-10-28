import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_and_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner2, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(max(self.all_results) in results and results[max(self.all_results)] == "Ник")

if __name__ == '__main__':
    unittest.main()
