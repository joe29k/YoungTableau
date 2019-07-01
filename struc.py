from words  import *
from visual import *
from ytmath import *

class youngtableau:
    def __init__(self, word):
        self.word = word
        self.matrix = parse_word(word)
    def row_insert(self, x):
        return row_insert(youngtableau(self.word), x)


    def visual(self,boxlength, file):
        print_tex(self.matrix, boxlength, file)


            
    def word(self):
        self.update_word()
        return self.word

    

    def update_word(self): #nur eine hilfs funktion...
        self.word = wordFromMatrix(self.matrix)

    def set_matrix(self, matrix):
        self.matrix = matrix
        self.update_word()




def create_from(row,file):
    #Objekt erstellen, die matrix setzen, dadurch oben autom. auch das Word gesetzt.
    yt = youngtableau("")
    yt.set_matrix(parse(row, file))
    return yt

def multiply(S, T):
    return multiplyMatrix(S, T)
    

