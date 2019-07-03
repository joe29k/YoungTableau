from words  import *
from visual import *
from ytmath import *

class youngtableau:
    def __init__(self, word):
        self.wort = word
        self.matrix = parse_word(word)

    def __str__(self):
        return self.matrix
    
    def row_insert(self, x):
        return youngtableau(wordFromMatrix(row_insert(self.matrix, x)))
        

    def visual(self,boxlength, file):
        print_tex(self.matrix, boxlength, file)
            
    def word(self):
        return word(self.wort) #als Objekt!!!


class word:
    def __init__(self, wordstring=""):
        self.wort = wordstring #benoetigt fuer youngtableau funct.
        wordlist_str = self.wort.split()
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
        return youngtableau(get_wyt(self.wort))

def create_from(row,file):
    #Young Tableau aus File erstellen
    return youngtableau(wordFromMatrix(parse(row, file)))

def multiply(S, T):
    return youngtableau(wordFromMatrix(multiplyMatrix(S.matrix, T.matrix)))

def mult_classes(word1, word2):
    return word(multiplyWord(word1.wort, word2.wort))

def are_equiv(word1, word2):
    if word1.youngtableau().wort == word2.youngtableau().wort:
        return True
    else:
        return False

    

def get_wyt(wortstring):#Ermittelt das zu word aequivalente Wort, dass ein korrektes Young Tableau reprasentiert
    wordlist_str = wortstring.split()
    #alle elemente in ein zunaechst leeres young tableaux einfuegen!
    yt = [] #young tableau in listen form
    for i in range(0,len(wordlist_str)):
        yt = row_insert(yt, int(wordlist_str[i]))
    return wordFromMatrix(yt)
    
