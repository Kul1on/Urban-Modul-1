# tests_12_4.py
import unittest
import logging
from runner import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            with self.assertRaises(ValueError):
                runner = Runner("TestRunner", -10)  # Передаем отрицательное значение в speed
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            with self.assertRaises(TypeError):
                runner = Runner(123, 10)  # Передаем не строку в name
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
