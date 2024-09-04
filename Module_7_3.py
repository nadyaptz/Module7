from pprint import pprint


class WordsFinder():
    def __init__(self, *file_titles):
        self.file_names = []
        self.file_titles = file_titles
        for i in range(0, len(file_titles)):
            self.file_names.append(self.file_titles[i])

    def get_all_words(self):
        '''
        get_all_words - подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        Где:
        'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
        ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        '''

        all_words: dict = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text = file.read()
                # print(text)
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(symbol, ' ')
                # print(text.lower().split())
            all_words[name] = text.lower().split()
        # print(all_words)
        return all_words

    def find(self, word):
        '''
        Метод, где word - искомое слово.
        Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

        '''
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                result[name] = words.index(word.lower()) + 1  # порядковый номер на 1 больше, чем индекс :)
        return result

    def count(self, word):
        '''
        Метод, где word - искомое слово.
        Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.

        '''
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word.lower())
        return result

# проверка из текста задачи
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# проверка из дополнительного задания

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
