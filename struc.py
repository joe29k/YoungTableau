from words  import *
from visual import *
from ytmath import *

class youngtableau:
    def __init__(self, word):
        self.word = word
        self.matrix = parse_word(word)
    def row_insert(self, x):
        return row_insert(self.matrix, x)

    def visual(self,boxlength, file):
        print_tex(self.matrix, boxlength, file)
            
    def word(self):
        return word(self.word) #als Objekt!!!


class word:
    def __init__(self, wordstring=""):
        self.wordstring = wordstring #benoetigt fuer youngtableau funct.
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

    def youngtableau(self):
        #zunaechst noch w quer zu bilden!!!
        return youngtableau(self.wordstring)

def create_from(row,file):
    #Young Tableau aus File erstellen
    return parse(row, file)

def multiply(S, T):
    return youngtableau(wordFromMatrix(multiplyMatrix(S, T)))

def mult_classes(word1, word2):
    return multiplyWord(word1.wordstring, word2.wordstring)

def are_equiv(word1, word2):
    w_yt_1 = get_wyt(word1)
    w_yt_2 = get_wyt(word2)
    if w_yt_1 == w_yt_2:
        return True
    else:
        return False

def get_wyt(wortstring):#Ermittelt das zu word aequivalente Wort, dass ein korrektes Young Tableau reprasentiert
    wortobjekt = word(wortstring)
    #alle elemente in ein zunaechst leeres young tableaux einfuegen!
    yt = [] #young tableau in listen form
    for i in range(0,len(wortobjekt.wordlist)):
        yt = row_insert(yt, wortobjekt.wordlist[i])
    return wordFromMatrix(yt)
    
    
    
if __name__ == "__main__": #Test sheetz aber dat wird nur ausgefuehrt wenn man des programm direkt runnt, yoo
    print(parse_word("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"))
    multiply(create_from(8, "ttest.txt"), create_from(8, "ttest.txt")).visual(1,"777.tex")
