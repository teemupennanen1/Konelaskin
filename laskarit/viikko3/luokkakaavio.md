# Monopoli

## Luokkakaavio

```mermaid
classDiagram
    Pelilauta "*" --> "40" Ruutu
    Pelaajat "*" --> "2...8" Pelaaja
    Ruutu "*" --> "1" Pelaaja
    Pelaaja "*" --> Pelaaja

    Pelilauta : List<Ruutu> ruudut 
    Pelilauta : tuple<Noppa, Noppa> Nopat
    
    class Noppa{
    + heita()
    }
    class Ruutu{
    +int edellinen
    +int seuraava
    +Pelaaja pelaaja
    }
    class Pelaajat{
        +List<Pelaaja> pelaajat 
    }
    class Pelaaja{
        +String nappula
        +liiku()
    }
```