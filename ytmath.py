
def row_insert(T, x):
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
    w_T = wordFromMatrix(T)
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
    if (len(wordlist) < 3) or (index + 2 > len(wordlist)-1):
        throw_k_ex()
    else:
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


    wordlist[index] = a
    wordlist[index+1] = b
    wordlist[index+2] = c
    return wordFromMatrix([wordlist]) #Umwandlung liste -> WordString
    #Wort zur ausgabe konstruieren
    #finalstring = ""
    #for jj in range(0, len(wordlist)):
   #     finalstring = finalstring + str(wordlist[jj]) + " "
  #  if len(wordlist) != 0:
 #           finalstring = finalstring[-1] #letztes zeichen weg
#
    #return finalstring


def throw_k_ex(): #hilfsfunktion zur ausgabe fehlermeldung
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
    

