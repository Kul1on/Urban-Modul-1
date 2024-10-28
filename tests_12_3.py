import unittest


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        pass

    @skip_if_frozen
    def test_run(self):
        pass

    @skip_if_frozen
    def test_walk(self):
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        pass
