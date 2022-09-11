import numpy as np
from random import choice, sample
from string import punctuation
s = words


class N-model():

    def __init__(self):

    def generatetext():
        global s
        s1 = list(filter(lambda x: x not in punctuation, s))
        s2 = ((' '.join((sample(s1, choice(range(5, 20)))))).lower()).split()
        for i in s2:
            s2.insert(0, i[0].upper() + i[1:])
            break
        s2.remove(s2[1])
        for i in s2:
            if s2.count(i) != 1:
                del s2[' '.join(s2).rfind(i)]
        return ' '.join(s2) + '.'

    def sample(self):
        kolvo_strok = 10
        for i in range(kolvo_strok):
            flag = True
            while flag:
                try:
                    print(generatetext())
                    flag = False
                except IndexError:
                    s = words


