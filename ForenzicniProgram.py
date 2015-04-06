crna_barva_las = "CCAGCAATCGC"
rjava_barva_las = " GCCAGTGCCG"
barva_las_korencek = "TTAGCTATCGC"

obraz_kvadraten = "GCCACGG"
obraz_okrogel = "ACCACAA"
obraz_ovalen = "AGGCCTCA"

barva_oci_modra = "TTGTGGTGGC"
barva_oci_zelena = "GGGAGGTGGC"
barva_oci_rjava = "AAGTAGTGAC"

spol_moski = "TGCAGGAACTTC"
spol_zenski = "TGAAGGACCTTC"

rasa_belec = "AAAAACCTCA"
rasa_crnec = "CGACTACAG"
rasa_azijec = "CGCGGGCCG"

datoteka = open("dna.txt", "r")
dna = datoteka.read()


if dna.find(barva_las_korencek) and dna.find(barva_oci_rjava) and dna.find(obraz_okrogel) and dna.find(rasa_belec)!= 0:
    print("Ziga je pojedel sladoled!")
elif dna.find(barva_oci_modra) and dna.find(crna_barva_las) and dna.find(obraz_ovalen) and dna.find(rasa_belec) != 0:
    print("Matej je pojedel sladoled!")
elif dna.find(barva_oci_zelena) and dna.find(rjava_barva_las) and dna.find(obraz_kvadraten) and dna.find(rasa_belec)!=0:
    print ("Miha je pojedel sladoled!")
else:
    print ("Le zakaj sem pustil dokaze za seboj?!")
print("Pa smo te ujeli!")
datoteka.close()





