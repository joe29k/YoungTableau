
def row_insert(T, x):
    for i in range(0, len(T.matrix)):#i startet bei 0 anders als im Text(dort bei 1)
        if max(T.matrix[i]) <= x: #"es gibt kein Element dass echt groesser ist"
            T.matrix[i].append(x)
            T.update_word()
            return T
        else:#linkestes aller echt groessern ist erstes echt groesseres
            for nz in range(0, len(T.matrix[i])):
                if T.matrix[i][nz] > x:
                    #an stelle nz nun x und y vertauschen
                    (T.matrix[i][nz], x) = (x, T.matrix[i][nz])
                    break
            
    #Wenn er hier hin kommt, ist die "naechste Reihe" leer!
    T.matrix.append([x])
    T.update_word()
    return T

def hassiiiid_row_insert(T,x,i=0):
    '''Die Funktion fügt ein neues Element x in ein YoungTabeau T ein
    @param: YoungTableau T, neues Element x, erste Zeile i =0
    @return: neue YoungTableau
    '''
    n = len(T)
    if i==n:	    #wenn das YoungTableau leer ist, wird das Element x einfach hinzugefügt
        T.append([str(x)])
        return T
    if echt_grosser(T[i],x)==False:	#falls x das größte Element ist, fügt x am Ende der Zeile hinzu
        T[i].append(str(x))
        return T
    else:
        y=echt_grosser(T[i],x)		#falls x kleiner als ein Element aus der Zeile, wird das Element = x eingesetzt
        T[i][y[0]]=str(x)
        return row_insert(T,int(y[1]),i+1)		#analog wird in den anderen Zeilen gemacht mit x ist das Element, das eingesetzt wurde.
        
        

def echt_grosser(l,x):
    '''Die Funktion prüfen ob ein Element echt grösser als alle andere Elemente in eine Zeile ist
    @param: eine Zeile aus dem YoungTableau, ein Element x
    @return: False wenn kein Element von der Zeile echt grösser als x ist
    '''
    found = 0
    for index in range(len(l)):
        if int(l[index])>x:
            return (index,l[index])
    return False

def multiplyMatrix(S,T):
    w_T = wordFromMatrix(T.matrix)
    xelems = w_T.split()
    for i in range(0, len(xelems)):
        S = row_insert(S,(int(xelems[i])))
    return S

def multiplyWord(word1, word2):
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
    return K_operation(wordlist, index, "1")
def K1_inv(wordlist, index):
    return K_operation(wordlist, index, "1_inv")
def K2(wordlist, index):
    return K_operation(wordlist, index, "2")
def K2_inv(wordlist, index):
    return K_operation(wordlist, index, "2_inv")

def K_operation(wordlist, index, typ):
    if (len(wordlist) < 3) or (index + 3 > len(wordlist)-1):
        throw_k_ex()
    else:
        a = wordlist[index]
        b = wordlist[index+1]
        c = wordlist[index+2]
        if typ="1":
            (a, b, c) = (y, z, x)
            if ((x < y) and (y <= z)):
                (y, z, x) = (y, x, z)
            else:
                throw_k_ex()
                
        elif typ="1_inv":
            (a, b, c) = (y, x, z)
            if ((x < y) and (y <= z)):
                (y, x, z) = (y, z, x)
            else:
                throw_k_ex()


        if typ="2":
            (a, b, c) = (x, z, y)
            if ((x <= y) and (y < z)):
                (x, z, y) = (z, x, y)
            else:
                throw_k_ex()
                
        elif typ="2_inv":
            (a, b, c) = (z, x, y)
            if ((x <= y) and (y < z)):
                (z, x, y) = (x, z, y)
            else:
                throw_k_ex()
    #Wort zur ausgabe konstruieren
    finalstring = ""
    for jj in range(0, wordlist):
        finalstring = finalstring + str(wordlist[jj]) + " "
    if len(wordlist) =! 0:
            finalstring = finalstring[-1] #letztes zeichen weg

    return finalstring


def throw_k_ex:#hilfsfunktion zur ausgabe fehlermeldung
    raise ValueError("K-operation impossible")



#"nicht geforderte" hilfsfunktion um code aus zu schlackern !
def wordFromMatrix(matrix): #young matrix list meiner form (erste zeile = 1. liste usw)
        word = ""
        matrix_rev = list(reversed(matrix))
        for zeile in range(0, len(matrix_rev)):
            for spalte in range(0, len(matrix_rev[zeile])):
                word+=(str(matrix_rev[zeile][spalte]))
                word+=" "
        if len(word) != 0:
            word = word[:-1]#letztes zeichen raus
        return word
    

