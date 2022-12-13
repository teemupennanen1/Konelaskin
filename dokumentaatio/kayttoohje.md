# Käyttöohje

## Ohjelman käynnistäminen

Käynnistä virtuaaliympäristö komennolla:

```bash
poetry shell
```

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä ohjelma komennolla:

```bash
poetry run invoke start
```

## Ohjelman käyttäminen

Ohjelma osaa laskea kahden vakion laskutoimituksia. Ohjelma tunnistaa seuraavat merkit:

- Numerot: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
- Operaattorit: [+, -, *, /, =]
- 

Ohjelman käynnistettyä ruudulle printataan:

```bash
Anna lauseke: 
```

Ohjelmalle annetaan laskettava laskutoimitus, jonka perässä on "="-merkki, esim:

```bash
2+2=
```

Tämän kirjoitettua painamalla "Enter"-painiketta, ohjelma ilmoittaa liukulukuna vastauksen, tässä tapauksessa:

```bash
4.0
```

Ohjelma osaa käsitellä peräkkäisiä "+"- ja "-"-merkkejä. Esim. lauseke:

```bash
2--2=
```

Antaa vastaukseksi:

```bash
4.0
```

Jos käyttäjä antaa lausekkeeksi tyhjän merkkijonon, tulostuu:

```
Suljetaanko? K/e
```

Ohjelma voidaan sulkea merkillä K tai k, tai ohjelman käyttöä voidaan jatkaa kirjaimilla E tai e. Jälkimmäisellä komennolla tulostuu jälleen:

```bash
Anna lauseke: 
```

jolloin käyttäjä voi jatkaa ohjelman käyttöä yllä kuvatun mukaisesti