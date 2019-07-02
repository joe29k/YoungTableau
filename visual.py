import subprocess
def print_tex(matrix, boxlenght, filename='visual.tex'):
    """ Uebergebene Young Matrix visualisieren in Form einer LATEX File, in die Datei visual.tex

        @param: list matrix Die Young Matrix als matrix reprasentation, jedes Element ist eine Zeile von oben nach unten, jedes Unterelement dann die Elemente der jew. Zeile von links nach rechts
        @param: int boxlenght Die laenge eines Quadratischen Kaestchens
        
        """



    #Vorbereiten der TEX Datei - jedes Element dass wir lines hinzufuegen, wird spaeter eine
    #Zeile der Datei.

    #Kopf der Datei - aus von uns vorgefertigtem Template - Datei template_head.ctex - ziehen
    datei= open("template_head.ctex", 'r') #Datei laden aber nur fuer read
    lines = datei.readlines()
    datei.close() #Datei schliesssen damit fuer andere Programme wieder verwendbaer


    #MITTE DER DATEI - hier fuer jedes Kastchen kommt nen Box dazu

    lines.append("\\begin{tikzpicture} % boxlength=" + str(boxlenght)) #Dann kann der Anwender spaeter nachvollziehen wie gross die Boxlenght war - DOPPELBACKSLASH DA PYTHON SYNTAX SONST DEN ERSTEN BUCHSTABEN KAPUTT HAUT
    #Letze reihe beginnt beim Koordinatenursprung also muessen von unten nach
    #oben bauen aber unsere Matrix ist von oben nach unten, also einmal umdrehen
    matrix_rev = list(reversed(matrix))

    

    #KOS bauen wir wie folgt via hilfsfunktion auf. Y - horizontal, Reihen. Starten bei 0, unterste zeile, hochiterieren, dabei jeweils die X starten bei 0
    #fuer die Elemente in den Zeilen, also koennen direkt mit den Indizes der Liste arbeiten!!
    for y in range(0, len(matrix_rev)):
        lines.append("%ZEILE NR. " + str(y) + " (von unten)\n")
        lines.append("\n")
        for x in range(0, len(matrix_rev[y])):
            lines.append("%ELEMENT IN SPALTE NR. " + str(x) + " (von links)\n")
            lines = lines + getBoxTexCode(x, y, matrix_rev[y][x], boxlenght)
            lines.append("")

        lines.append("\n")
        lines.append("\n")
        lines.append("\n")


    #Ende der Datei - aus von uns vorgefertigtem Template - Datei template_tail.ctex - ziehen
    datei= open("template_tail.ctex", 'r') #Datei laden aber nur fuer read
    lines = lines + datei.readlines() #zu unserem rest hinten ran
    datei.close() #Datei schliesssen damit fuer andere Programme wieder verwendbaer


   
    #Datei ueberschreiben bzw erstellen falls nicht existent- dies alles macht w+
    file = open(filename, 'w+')
    for line in lines: #Alle Zeilen in die Datei hinein schreiben! 
        file.write(line)

    file.close()

    subprocess.call(['pdflatex', filename], stdout=subprocess.DEVNULL)



def getBoxTexCode(x, y, wert, boxlen):
    """ Hilfsfunktion Gibt zu dem entspr. Uebergebenen Wert und den Koordinaten den Code aus der dann zur Box im latex fuehrt

        @param: int x x Representationswert KOS Element in Matrix
        @param: int y y Representationswert KOS Element in Matrix
        @param: int wert der Wert der aktuellen Box
        @param: int boxlen Laenge der Box wie oben
        @return: list Liste die als Elemente die Hinzuzufuegenden Zeilen Enthaelt
        
        """

    ausgabe = []
    xstart = x*boxlen
    xend = (x+1)*boxlen
    xtext = (x+0.5)*boxlen
    ystart = y*boxlen
    yend = (y+1)*boxlen
    ytext = (y+0.5)*boxlen
    koord_start = "(" + str(xstart) + "," + str(ystart) + ")"
    koord_end = "(" + str(xend) + "," + str(yend) + ")"
    koord_text = "(" + str(xtext) + "," + str(ytext) + ")"
    str_wert = str(wert)
    #zunaechst noch start
    
    # DOPPELBACKSLASHES DA PYTHON SYNTAX SONST DEN ERSTEN BUCHSTABEN KAPUTT HAUT, \n fuer Line Endings noch jeweils hinzu zu fuegen.
    ausgabe.append("\\draw [ultra thick] " + koord_start + " rectangle " + koord_end + ";\n") #Box drawen
    ausgabe.append("\\node at ($" + koord_text + "$) {$" + str_wert + "$};\n") #Zahl drawen in die Mitte der Box
    ausgabe.append("\n")
    return ausgabe
    



if __name__ == "__main__": #Test sheetz aber dat wird nur ausgefuehrt wenn man des programm direkt runnt, yoo
    import words
    print_tex([['1', '2', '2', '3', '3', '5'], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 1)
    print_tex([[1, 2, 2, 3, 3, 5], ['2', '3', '5', '5'], ['4', '4', '6', '6'], ['5', '6']], 1)
    print_tex([[1, 2, 3]], 1)
