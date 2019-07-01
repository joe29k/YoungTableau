def parse_word(v):
    """ Erstelle ein Young Table aus einem Word
        

        @param: v Ein String wo die einzelnen Elemente mit leerzeichen getrennt stehen als Wort
        @return: list eine Liste wo die Elemente fuer die Zeilen von oben nach unten stehen. Jedes Element(Zeile) hat als
        Unterelemente dabei die Eintraege der jeweiligen Zeile von links nach rechts - ValueError falls das Wort keine YoungTableau repraesentiert!
        """
    #print(v)
    elemnte = v.split() #Fuer jedes Element zur Liste
    elemnz = []
    for r in range (0, len(elemnte)):
        elemnz.append(int(elemnte[r]))

    #Algorithmus: Eine Zeile ist beendet sobald das monotone Wachstum gebrochen wird. Terminierung d Algs. sobald wir
    #nur noch 1 Element haben. Also: So lange zur aktuellen Reihe (am Anfang leer) das erste Element aus der Elementenliste
    #hinzufuegen und entfernen, bis ein kleineres Element ploetzlich kaeme.
    if v=='':
        return []
    fertigKomplett = False
    reihen = []
    while not fertigKomplett:
        reihe = []
        fertigReihe = False
        while not fertigReihe:
            if len(elemnz) == 1:
                reihe.append(elemnz.pop(0))
                fertigReihe = True
                fertigKomplett = True
            else:
                
                if elemnz[0] > elemnz[1]:#Das Vordere Element beendet die Reihe!!!
                    fertigReihe = True
                reihe.append(elemnz.pop(0)) #in jedem falle hinzu...
        reihen.append(reihe)

    #Liste umdrehen um Zeilen von oben nach unten zu erhalten daraus.
    reihen = list(reversed(reihen))
    #Pruefen obs ne Young Tableau ist. Die beiden Monotonien oben sind implizit erfuellt, also noch schauen,
    #ob es von Reihe zu Reihe, immer weniger oder genau so viele Elemente sind, wie davor.
    for i in range(0, len(reihen)-1):
        if len(reihen[i]) < len(reihen[i+1]): #Also steigung nach unten hin! -> Exception zu werfen.
            raise ValueError("no young tableau")
    #FEHLERMOEGLICHKEIT 2 - gleiche zahlen untereinander
    for y in range(1,len(reihen)):#erst ab 1. Zeile da 1. es automatisch erfüllt
        for x in range(0, len(reihen[y])):
            if reihen[y][x] <= reihen[y-1][x]:
                raise ValueError("no young tableau")
    return reihen

def parse(row, file):
    """ Greift auf die Datei file, wo pro Zeile ein Wort steht, zu, und wertet die Zeile Nummer row (erste Zeile hat row=0),
        gemaess dem Algorithmus in parse_word, aus

        @param: row Zeilennummer, erste Zeile ist Zeile 0
        @param: file Pfad zur Datei!
        @return: list das representierende YoungTableau via parse_word, also ValueError falls das Wort keine YoungTableau repraesentiert!

    """
    datei= open(file, 'r') #Datei laden aber nur fuer read
    woerter = datei.readlines()
    word = woerter[row]
    datei.close() #Datei schliesssen damit fuer andere Programme wieder verwendbaer
    return parse_word(word)
    
#if __name__ == "__main__": #Test sheetz aber dat wird nur ausgefuehrt wenn man des programm direkt runnt, yoo
    #print(parse_word("5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"))
    #Test cases zum hinzufuegen:
    #A) Value Errors
    #B) parse from file
    #print(parse(3, "komasaufen.bier"))
    #for i in range(0, 4):
        #print(parse(i, "komasaufen.bier"))


def main():
    import words
    


