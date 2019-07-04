
def row_insert(T, x):
    """ Fuegt in uebergebene als List repraesntiertes Young Tableau, das Element x gemaess Einfuegeoperation ein und gibt das Ergebnis wieder als List zurueck.

        @param: list T YoungTableau
        @param: int x das einzufuegende Element
        @return: list die so resultierende YoungTableau
        
        """
    for i in range(0, len(T)):#i startet bei 0 anders als im Text(dort bei 1)
        if max(T[i]) <= x: #"es gibt kein Element dass echt groesser ist"
            T[i].append(x)
            return T
        else:#linkestes aller echt groessern ist erstes echt groesseres
            for nz in range(0, len(T[i])):
                if T[i][nz] > x:
                    #an stelle nz nun x und y vertauschen
                    (T[i][nz], x) = (x, T[i][nz])
                    break            
    #Wenn er hier hin kommt, ist die "naechste Reihe" leer!
    T.append([x])
    return T


def multiplyMatrix(S,T):
    """ Multipliziert zwei als List uebergebene YoungTableaux durch wiederholte Einfuegeoperationen (siehe Text) und gibt das Ergebnis wieder als List zurueck.

        @param: list S YoungTableau 1
        @param: list T YoungTableau 2
        @return: list das resultierende Young Tableau
        
        """
    w_T = wordFromMatrix(T)
    xelems = w_T.split()
    for i in range(0, len(xelems)):
        S = row_insert(S,(int(xelems[i])))
    return S

def multiplyWord(word1, word2):
    """ Multipliziert zwei als String uebergebene Woerter durch Konkatenierung

        @param: string word1 erstes Wort
        @param: string word2 zweites Wort
        @return: string das bei Multiplikation resultierende Wort
        
        """
    #Falls neutrales Element konkateniert werden soll, ist das neue Wort das andere
    #Fall "beide Woerter leer" automatisch enthalten-- das leere wort wird folgerichtig ausgegeben
    if word1 == "":
        return word2
    elif word2 == "":
        return word1
    #Sonst konkatenieren und leerzeichen dazwischen
    return word1 + " " + word2

#Wordlist hat form [1, 2, 5, 6]
def K1(wordlist, index):
    """ Betrachte das Unterwort self[index:index+3] der Länge 3 und gebe das durch K1 modifizierte Wort zurueck falls die Voraussetzungen
        erfuellt sind, oder wirft einen ValueError("K-operation impossible")

        @param: list wordlist Elemente des zu modifizierenden Wortes als Liste. Index bei dem das Unterwort startet
        @param: int index Index bei dem das Unterwort startet
        @return: list das modifizierte Wort
        
        """
    return K_operation(wordlist, index, "1")
def K1_inv(wordlist, index):
    """ Betrachte das Unterwort self[index:index+3] der Länge 3 und gebe das durch K1_inv modifizierte Wort zurueck falls die Voraussetzungen
        erfuellt sind, oder wirft einen ValueError("K-operation impossible")

        @param: list wordlist Elemente des zu modifizierenden Wortes als Liste. Index bei dem das Unterwort startet
        @param: int index Index bei dem das Unterwort startet
        @return: list das modifizierte Wort
        
        """
    return K_operation(wordlist, index, "1_inv")
def K2(wordlist, index):
    """ Betrachte das Unterwort self[index:index+3] der Länge 3 und gebe das durch K2 modifizierte Wort zurueck falls die Voraussetzungen
        erfuellt sind, oder wirft einen ValueError("K-operation impossible")

        @param: list wordlist Elemente des zu modifizierenden Wortes als Liste. Index bei dem das Unterwort startet
        @param: int index Index bei dem das Unterwort startet
        @return: list das modifizierte Wort
        
        """
    return K_operation(wordlist, index, "2")
def K2_inv(wordlist, index):
    """ Betrachte das Unterwort self[index:index+3] der Länge 3 und gebe das durch K2_inv modifizierte Wort zurueck falls die Voraussetzungen
        erfuellt sind, oder wirft einen ValueError("K-operation impossible")

        @param: list wordlist Elemente des zu modifizierenden Wortes als Liste. Index bei dem das Unterwort startet
        @param: int index Index bei dem das Unterwort startet
        @return: list das modifizierte Wort
        
        """
    return K_operation(wordlist, index, "2_inv")

def K_operation(wordlist, index, typ): #Hilfsfunktion die die K-operation ausfuehrt

    
    if (len(wordlist) < 3) or (index + 2 > len(wordlist)-1): #Wort ist zu kurz oder Unterwort schiesst ueber die laenge hinaus (ex. nicht) - fehler
        throw_k_ex()

    
    else:
        #Entsprechend der gegebenen Umwandlungsvorschriften die Umwandlung durchfuehren und vorher die Groessenrelation abchecken noch, fehler werfen falls diese nicht erfuellt
        a = wordlist[index]
        b = wordlist[index+1]
        c = wordlist[index+2]
        if typ=="1":
            (y, z, x) = (a, b, c)
            if ((x < y) and (y <= z)):
                (a, b, c) = (y, x, z)
            
            else:
                throw_k_ex()
                
        elif typ=="1_inv":
            (y, x, z) = (a, b, c)
            if ((x < y) and (y <= z)):
                (a, b, c) = (y, z, x)
            else:
                throw_k_ex()


        if typ=="2":
            (x, z, y) = (a, b, c)
            if ((x <= y) and (y < z)):
                (a, b, c) = (z, x, y)
            else:
                throw_k_ex()
                
        elif typ=="2_inv":
            (z, x, y) = (a, b, c)
            if ((x <= y) and (y < z)):
                (a, b, c) = (x, z, y)
            else:
                throw_k_ex()

    #modifiziertes unterwort in das wort einfuegen
    wordlist[index] = a
    wordlist[index+1] = b
    wordlist[index+2] = c
    return wordFromMatrix([wordlist]) #Umwandlung liste -> WordString ("Betrachtet als einzeiliges Youngtableau"


def throw_k_ex(): #hilfsfunktion zur ausgabe fehlermeldung
    raise ValueError("K-operation impossible")


#"
def wordFromMatrix(matrix): #young matrix list meiner form 
        """ nicht geforderte" hilfsfunktion um code aus zu schlackern ! Konvertiert eine uebergebene YoungMatrix als List "meiner" Form
        (erste zeile = 1. unterliste usw) in das zugehoerige Wort.

        @param: list matrix umzuwandelde Matrix in meiner Form

        @return: string das Wort als String
        
        """
        word = ""
        matrix_rev = list(reversed(matrix))
        for zeile in range(0, len(matrix_rev)):
            for spalte in range(0, len(matrix_rev[zeile])):
                word+=(str(matrix_rev[zeile][spalte]))
                word+=" "
        if len(word) != 0:
            word = word[:-1]#letztes zeichen raus
        return word
    

