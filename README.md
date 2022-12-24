# Konelaskin

Sovellus on laskin, jota käytetään terminaalista käsin (tekstikäyttöliittymä). 

## Huomioita Python-versiosta

Sovellus toimii Python 3.8 versiolla. Aiemmilla tai uudemmilla versioilla sovelluksen toiminnassa voi olla ongelmia.

## Dokumentaatio

- [Arkkitehtuuri](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Käyttöohje](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Testaus](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

## Komentorivitoiminnot

Sovellus hyväksyy kaavoissa merkit: 
- "0" 
- "1"
- "2"
- "3"
- "4"
- "5"
- "6"
- "7"
- "8"
- "9"
- "+"
- "-"
- "*"
- "/"
- "="
- "."

"" merkki herättää sammutustoiminnon, jolloin ohjelma tulostaa "Suljetaanko? K/e". Tähän voidaan vastata merkkijonoilla "K", "k", "E" ja "e". Muut merkkijonot tuottavat virheilmaisun "Sopimaton komento". Sammutustoiminnosta pääsee eteenpäin vain hyväksytyillä merkkijonoilla. "K" ja "k" sammuttavat laskimen, kun taas "E" ja "e" jatkavat laskimen käyttöä.

"ohjeet" komento tulostaa laskimen käyttöohjeet:

Voit laskea laskutoimituksia kirjoittamalla ne Anna lauseke: merkkijonon perään
ja painamalla Enter-näppäintä. Muista lisätä laskutoimituksen perään =-merkki!
Kirjoittamalla ohjeet ja painamalla Enter-näppäintä ohjelma tulostaa tämän näkymän
Tyhjä rivi ja Enter-näppäin käynnistää laskimen sammutustoiminnon
Vastaamalla K tai k, laskin sammutetaan
Vastaamalla E tai e jatketaan laskimen käyttöä

Ohjelma pitää muistissa edellisen laskutoimituksen tuloksen. Kirjoittamalla laskutoimitukseen vakion tilalle "ans", voidaan edellistä tulosta käyttää laskutoimituksessa.

### Ohjelman suorittaminen

Käynnistä sovellus komennolla
```bash
poetry run invoke start
```

### Testaus

Suorita testit komennolla:
```bash
poetry run invoke test
```
### Testikattavuus

Coverage ajetaan komennolla 
```bash
poetry run invoke coverage
```

Testikattavuusraportti generoidaan komennolla
```bash
poetry run invoke coverage-report
```
Tämän komennon käyttäminen ajaa myös coveragen

Coverage raportti generoituu htmlcov hakemiston index.html-tiedostoon. Tiedoston voidaan avata juurihakemistossa komennolla 
```bash
poetry run invoke html-report
```
Tämä komento suorittaa myös coverage-report komennon, joka puolestaan suorittaa myös coveragen. 

Pylint ajetaan komennolla
```bash
poetry run invoke lint
```