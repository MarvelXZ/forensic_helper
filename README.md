Struktura IMEI broja i objašnjenje algoritma za poslednju cifru
IMEI (International Mobile Equipment Identity) je jedinstveni identifikacioni broj koji se dodeljuje svakom mobilnom telefonu. Njegova osnovna svrha je identifikacija uređaja u mobilnim mrežama i sprečavanje zloupotrebe.

Struktura IMEI broja
IMEI broj se sastoji od 15 cifara:

Prvih 14 cifara predstavljaju identifikaciju proizvođača i modela uređaja, kao i jedinstveni serijski broj telefona.

15-ta cifra je takozvana kontrolna cifra. Ova cifra ne sadrži informaciju o uređaju, već služi za proveru ispravnosti celog IMEI broja – kako bi se sprečilo greškom ili namerno unošenje pogrešnog broja.

Kako se računa kontrolna (poslednja) cifra?
Kontrolna cifra IMEI broja se računa pomoću međunarodno priznatog matematičkog algoritma pod nazivom Luhn algoritam (poznat i kao “modulus 10” algoritam).

Princip algoritma je sledeći:

Uzimaju se prvih 14 cifara IMEI broja, s leva na desno.

Svaka druga cifra (računajući od druge cifre) se množi sa dva.
Na primer, 2, 4, 6... i tako dalje.

Ako rezultat množenja daje dvocifren broj (npr. 12), cifre tog broja se sabiraju (1 + 2 = 3).

Svi brojevi dobijeni ovim postupkom se saberu zajedno sa ciframa koje nisu množenje.

Na kraju, bira se takva 15-ta cifra da ukupna suma svih 15 cifara (uključujući i kontrolnu cifru) bude deljiva sa 10.

Na ovaj način, svaki uređaj ima tačno definisan i proverljiv IMEI broj.

Zašto je važna kontrolna cifra?
Kontrolna cifra služi za otkrivanje grešaka u kucanju ili prenosu broja.
Ako se bilo koja cifra promeni greškom ili namerno, kontrolna cifra se više neće poklapati sa izračunatom, pa je lako otkriti nevažeći ili izmenjeni IMEI.

Kratak primer:
Ako je prvih 14 cifara IMEI broja:
49015420323751

Sledi postupak:

Svaka druga cifra (9, 1, 4, 0, 2, 7, 1) množi se sa 2.

Dobijeni brojevi (posle sabiranja cifara dvocifrenih rezultata): 92=18 (1+8=9), 12=2, 42=8, 02=0, 22=4, 72=14 (1+4=5), 1*2=2

Svi brojevi se saberu, ukupno se dobija 52.

Kontrolna (15-ta) cifra je broj koji treba dodati na 52 da bi zbir bio deljiv sa 10. U ovom slučaju to je 8 (jer 52 + 8 = 60, a 60 je deljivo sa 10).

Dakle, kompletan IMEI je 490154203237518.

Zaključak:
Sistem provere IMEI broja i njegova kontrolna cifra su standardizovani na globalnom nivou, i predstavljaju pouzdanu zaštitu od greške ili zloupotrebe u vezi sa identitetom uređaja.
