# Konelaskin

Tämä sovellus on laskin, jolla voidaan laskea erilaisia laskutoimituksia. Laskinta voidaan käyttää graafisen käyttöliittymän kautta osoittimella, tai näppäimistöllä.

## Huomioita Python-versiosta

Sovellus toimii Python 3.8 versiolla. Aiemmilla tai uudemmilla versioilla sovelluksen toiminnassa voi olla ongelmia.

## Dokumentaatio

- [Arkkitehtuuri](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/changelog.md)
- [Käyttöohje](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/teemupennanen1/ot-harjoitustyo/blob/main/konelaskin/dokumentaatio/vaatimusmaarittely.md)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Käynnistä sovellus komennolla

poetry run invoke start

### Testaus

Suorita testit komennolla:

poetry run invoke test

### Testikattavuus

Testikattavuusraportti generoidaan komennolla

poetry run invoke coverage-report

Raportti generoituu htmlcov-hakemistoon.
