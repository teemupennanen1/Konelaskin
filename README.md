# Konelaskin

Sovellus on laskin, jota käytetään terminaalista käsin (tekstikäyttöliittymä)

## Huomioita Python-versiosta

Sovellus toimii Python 3.8 versiolla. Aiemmilla tai uudemmilla versioilla sovelluksen toiminnassa voi olla ongelmia.

## Dokumentaatio

- [Arkkitehtuuri](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.png)
- [Changelog](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/changelog.md)
- [Käyttöohje](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/vaatimusmaarittely.md)

## Komentorivitoiminnot

Sovellus hyväksyy kaavoissa merkit "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "=", "". 

"" merkki herättää sammutustoiminnon, jolloin ohjelma tulostaa "Suljetaanko? K/e". Tähän voidaan vastata merkkijonoilla "K", "k", "E" ja "e". Muut merkkijonot tuottavat virheilmaisun. Sammutustoiminnosta pääsee eteenpäin vain hyväksytyillä merkkijonoilla. "K" ja "k" sammuttavat laskimen, kun taas "E" ja "e" jatkavat laskimen käyttöä.

### Ohjelman suorittaminen

Käynnistä sovellus komennolla

poetry run invoke start

### Testaus

Suorita testit komennolla:

poetry run invoke test

### Testikattavuus

Testikattavuusraportti generoidaan komennolla

poetry run invoke coverage-report

Raportti generoituu htmlcov hakemiston index.html-tiedostoon. Tiedoston voidaan avata juurihakemistossa komennolla 

poetry run invoke html-report

Pylint ajetaan komennolla

poetry run invoke pylint
