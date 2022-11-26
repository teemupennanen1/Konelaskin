# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseinen sovellus on laskin, jolla pystyy laskemaan peruslaskutoimituksia. Laskutoimitusten koodaaminen toteutetaan itse, eikä käyttämällä pythonin valmiita kirjastoja.

## Käyttäjät

Tarkoituksena ei ole lisätä sovellukselle muita käyttäjiä, kuin pääkäyttäjä. Jos sovellusta tarvitsee laajentaa, käyttäjien lisäämistä voidaan harkita.

## Käyttöliittymäluonnos

Sovellukselle tulee vain yksi näkymä, joka aukeaa, kun sovellus käynnistetään. Laskutoimituksia varten luodaan näkymään buttoneita, jotta laskinta voi käyttää osoittimella. Jokaiselle numerolle ja laskutoimitukselle luodaan oma buttoninsa.

Näkymän yläosassa on tekstikenttä, johon laskutoimituksia voidaan tehdä näppäimistöllä. Tekstikenttä on oletuksella aktiivinen. Tekstikentän oikeaan alalaitaan tulee aina laskettavan laskutoimituksen tulos. Käyttäjä aktivoi tekstikentän klikkaamalla kenttää.

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

Painamalla näppäimistöllä "Enter"-painiketta lasketaan tekstikentässä oleva laskutoimitus. Jos tekstikentässä oleva kaava ei ole validi, tulee vastauskenttään teksti "Error".

## Jatkokehitysideoita

Sovellusta voidaan laajentaa graafiseksi laskimeksi.
