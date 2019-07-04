from words  import *
from visual import *
from ytmath import *

class youngtableau:
    """
        Klasse youngtableau.
        Attribute:
        string wort - das Wort, dass das youngtableau repraesentiert (urspruengl. nicht gefordert, hier zur Vereinfachung im Code eingefuehrt! - notwendig!)
        list matrix - Youngtableau in Matrixschreibweise so wie in parse_word erzeugt...
        Methoden s.u.
        Parameter:
        string word - das Wort, aus dem ein Young Tableau erstellt werden soll
    
    """
    def __init__(self, word):
        self.wort = word
        self.matrix = parse_word(word)
    
    def row_insert(self, x):
        """ Gibt das Young Tableau (self <- x) zurueck

        @param: int x - Das Element, das dem Young Tableau hinzugefuegt werden soll gemaess Algorithmus aus Aufgabenstellung
        @return: youngtableau das Youngtableau, das bei der Einfuegeoperation entsteht (neues Objekt!!!)
        
        """
        return youngtableau(wordFromMatrix(row_insert(self.matrix, x)))       

    def visual(self,boxlength, file):
        """ Speichert die Visualisierung in der Datei file ab.

        @param: int boxlength - die Seitenlaenge eines Kaestchens in der Latex Datei
        @param: string file - Dateiname der Datei, die ausgegeben werden soll
        
        """
        print_tex(self.matrix, boxlength, file)
            
    def word(self):
        """ Gibt das zur Young Tableau gehoerende Wort als Objekt der Klasse word zurueck.

        @return: word das zum Youngtableau gehoerende Wort als Objekt der Klasse word
        
        """
        return word(self.wort) #als Objekt!!!


class word:
    """
        Klasse word. Speichert ein Wort ueber die Natuerlichen Zahlen >=1 als Liste
        Attribute:
        string wort - das Wort, dass das youngtableau repraesentiert (urspruengl. nicht gefordert, hier zur Vereinfachung im Code eingefuehrt! - notwendig!)
        list wordlist - Liste, deren Elemente die Elemente des Wortes enthalten
        Methoden s.u.
        Parameter:
        string wordstring - das Wort als String, das als Liste gespeichert werden soll
    
    """
    def __init__(self, wordstring=""):
        self.wort = wordstring #benoetigt fuer youngtableau funct.

        #Alle Elemente ausm String splitten und ab in eine Liste damit
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
        """ Gibt (w quer) hoch minus 1 von self quer als Young Tableau zurueck

        @return: youngtableau das Youngtableau, das das Wort repraesentiert
        
        """
        #zunaechst noch w quer zu bilden!!!
        return youngtableau(get_wyt(self.wort))

def create_from(row,file):
    """ Young Tableau aus File erstellen

        @param: int row die Zeile aus der Datei, in der das Wort steht(start by 0)
        @param: file der Dateiname der Datei, aus der das Wort exportiert werden soll
        @return: youngtableau das resultierende Youngtableau als objekt der Klasse youngtableau
        
    """
    
    return youngtableau(wordFromMatrix(parse(row, file)))

def multiply(S, T):
    """ Multipliziert zwei als youngtableau objekt uebergebene Young Tableaus und gibt das Ergebnis ebenfalls als youngtableau objekt aus

        @param: youngtableau S YoungTableau 1
        @param: youngtableau T YoungTableau 2
        @return: youngtableau das resultierende Youngtableau als objekt der Klasse youngtableau
        
    """
    return youngtableau(wordFromMatrix(multiplyMatrix(S.matrix, T.matrix)))

def mult_classes(word1, word2):
    """ Gibt einen Repraesentanten des Wortes aus, das bei Multiplikation der Quotientenmengen von word1 und word2 entstehen
        Waehlen frei den Repraesentanten, der das zugehoerige Youngtableau repraesentiert

        @param: word word1 erstes Wort
        @param: word word2 zweites Wort
        @return: word ein repraesentant, als word obj
    """
    return word(multiplyWord(word1.wort, word2.wort))

def are_equiv(word1, word2):
    """ Gibt True aus falls word1 aequivalent word2 gemaess Relation Tilde K; sonst false
        
        @param: word word1 erstes Wort
        @param: word word2 zweites Wort
        @return: bool Ob aeqivalent
    """
    if word1.youngtableau().wort == word2.youngtableau().wort:
        return True
    else:
        return False

    

def get_wyt(wortstring):
    """ Ermittelt das zu einem Wort aequivalente Wort, dass ein korrektes Young Tableau reprasentiert

        @param: string wortstring das Wort
        @return: string das wort, dass die YoungTableau repraesentiert
        
        """
    wordlist_str = wortstring.split()
    #alle elemente in ein zunaechst leeres young tableaux einfuegen!
    yt = [] #young tableau in listen form
    for i in range(0,len(wordlist_str)):
        yt = row_insert(yt, int(wordlist_str[i]))
    return wordFromMatrix(yt)
    
