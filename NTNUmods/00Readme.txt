Katalogen inneholder dokumentasjon og verktøy for å modifisere de opprinnelige transkripsjonene i NB_Tale.

Skriptet trans2mlf.pl tar den originale transkripsjonen (.trans) og produserer i ei label-fil 
i HTK MLF-format med 50 distinkte fonemsymboler. 

Skriptet mlf2nist_all.pl konverterer ei mlf-fil til separate label-filer i NIST-format (som TIMIT, men med annet fonemsett).


Kjør trans2mlf.pl for å generere mlf-fil, deretter det skriptet du fikk tidligere
for å generere egne labelfiler for hver lydfil. NB! Skriptet fjerner alle glottal-stopp.


Et forslag til å redusere ytterligere ved å angi “don’t care”-grupper (dvs. at evalueringen ikke tar hensyn til 
feil dersom det er symboler innen samme gruppe som forveksles) er følgende:

a) {tS, S, C, rs} er ei slik gruppereduc
b) Grupper som setter likhet mellom lang og kort vokal
{A,A:}, {ae,ae:}, {O,O:}, {e,e:}, {i,i:}, {oe,oe:}, {u,u:}, {y,y:}, ou,ou:} 
Det skulle gi en reduksjon i antall klasser på 3+9=12, dvs totalt 38 klasser. 

Word-dokumentet Sampa_modifikasjoner_v5.doc inneholder en tabell over fonemsettene, og de foreslåtte endringene. 