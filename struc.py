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


class word:
    def __init__(self, wordstring=""):
        wordlist_str = self.wordstring.split()
        self.wordlist = []
        for i in range(0, len(wordlist_str)):
            self.wordlist.append(int(wordlist_str[i]))

    def K1(self, index):
        return K1(self.wordlist, index)
    def K1_inv(self, index):
        return K1_inv(self.wordlist, index)
    def K2(self, index):
        return K2(self.wordlist, index)
    def K2_inv(self, index):
        return K2_inv(self.wordlist, index)

def create_from(row,file):
    #Objekt erstellen, die matrix setzen, dadurch oben autom. auch das Word gesetzt.
    yt = youngtableau("")
    yt.set_matrix(parse(row, file))
    return yt

def multiply(S, T):
    return multiplyMatrix(S, T)
    

