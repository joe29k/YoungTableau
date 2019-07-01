from words  import *
from visual import *


class youngtableau:
    def __init__(self, word):
        self.word = word
        self.matrix = parse_word(word)

    def visual(self,boxlength, file):
        print_tex(self.matrix, boxlength)

    def 

    def row_insert(self, x):
        for i in range(0, len(self.matrix)):#i startet bei 0 anders als im Text(dort bei 1)
            if max(self.matrix[i]) < x: #"es gibt kein Element dass echt groesser ist"
                self.matrix[i].append(x)
                return youngtableau(self.matrix

        #Update the word
                
