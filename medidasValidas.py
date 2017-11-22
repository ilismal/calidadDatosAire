from __future__ import print_function
import glob
for fichero in glob.glob('*.txt'):
    print("Analizando datos: ", fichero)
    with open(fichero, 'r') as mes:
        validas=0
        invalidas=0
        for line in mes:
            primerValor=25
            for i in range (0,24):
                if line[primerValor+(i*6)]=="V":
                    validas+=1
                else:
                    invalidas+=1
    total = validas + invalidas
    print(total,"lecturas")
    print(validas," validas (", round(validas*100.00/total,2),"%)",sep="")
    print(invalidas," invalidas (", round(invalidas*100.00/total,2),"%)",sep="")
