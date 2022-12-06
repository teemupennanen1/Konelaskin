# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseinen sovellus on laskin, jolla pystyy laskemaan peruslaskutoimituksia.

## Käyttäjät

Tarkoituksena ei ole lisätä sovellukselle muita käyttäjiä, kuin pääkäyttäjä. Jos sovellusta tarvitsee laajentaa, käyttäjien lisäämistä voidaan harkita.

## Käyttöliittymäluonnos

Tekstikäyttöliittymä. Kun sovellus käynnistetään, tulostuu merkkijono "Anna lauseke: ". Käyttäjä voi laskea yhteen-, vähennys-, kerto- ja jakolaskuja. Jos kaavan lopusta puuttuu "=", laskin muistuttaa käyttäjää tästä tulostamalla "Muista = merkki loppuun". tehty

Syöttämällä "Anna lauseke: " perään tyhjän merkkijonon, tulostuu "Suljetaanko? K/e". Vastaamalla K tai k ja painamalla Enter, laskin sulkeutuu. Vastaamalla E tai e, laskimen käyttö jatkuu (laskin tulostaa "Anna lauseke: "). Vastaamalla jotain muuta, laskin tulostaa "Sopimaton komento", ja jatkaa seuraavalla rivillä "Suljetaanko? K/e", kunnes vastataan E, e, K tai k. tehty

Laskimella voidaan laskea myös kertomia.

Käyttäjä voi käyttää myös aiempaa tulosta laskutoimituksen osana. 

## Jatkokehitysideoita

### Graafinen käyttöliittymä

Laskimelle luodaan graafinen käyttöliittymä, jonka kautta laskutoimituksia laskinta voi käyttää osoittimella. Jokaiselle numerolle ja laskutoimitukselle luodaan oma buttoninsa. 

Buttoneita vastaavat seuraavat merkkijonot:

1 = "1"
2 = "2"
3 = "3"
4 = "4"
5 = "5"
6 = "6"
7 = "7"
8 = "8"
9 = "9"
0 = "0"
/ = "/"
* = "*"
- = "-"
+ = "+"
= = "="

### Vanhojen laskujen tallentaminen

Vanhat laskut voidaan tallentaa repositorioon, josta niitä pystyy käydä tarkastelemassa. 