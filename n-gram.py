import numpy as np
import random
import string

word_list = words 

class TextGenerator:

    def __init__(self):
        pass

    def generate_sentence(self):
        global word_list
        # Удаление знаков препинания
        cleaned_words = [w for w in word_list if w not in string.punctuation]
        
        # Выбор случайного количества слов от 5 до 19
        count = random.randint(5, 19)
        selected = random.sample(cleaned_words, count)
        
        # Приведение всех слов к нижнему регистру
        selected = [word.lower() for word in selected]
        
        # Капитализация первого слова
        if selected:
            selected[0] = selected[0].capitalize()
        
        # Удаление второго слова, если оно существует
        if len(selected) > 1:
            del selected[1]
        
        # Удаление дубликатов, сохраняя порядок
        unique = []
        for word in selected:
            if word not in unique:
                unique.append(word)
        
        # Формирование предложения
        sentence = ' '.join(unique) + '.'
        return sentence

    def print_samples(self, sample_count=10):
        for _ in range(sample_count):
            while True:
                try:
                    print(self.generate_sentence())
                    break
                except IndexError:
                    word_list = words  # Повторное присвоение, если возникла ошибка

# Пример использования:
# генератор = TextGenerator()
# генератор.print_samples()
