import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation + ' -'))
                        words.extend(line.split())
                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return all_words

    def find(self, word):
        word = word.lower()
        results = {}

        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1

        return results

    def count(self, word):
        word = word.lower()
        results = {}

        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            results[file_name] = words.count(word)

        return results

finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
