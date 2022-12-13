# Testausdokumentti

Automaattisen testauksen ulkopuolelle on rajattu käyttöliittymän testaus, eli testit testaavat vain laskutoimitusten toimivuutta.

## Testausmenetelmät

### Laskutoimitusten oikeellisuuden testaus

Testeillä testataan, toimivatko yhteen-, vähennys-, kerto- ja jakolaskuoperaattorit halutulla tavalla.

Näiden lisäksi testataan, saadaanko perättäisillä yhteen- ja vähennyslaskuoperaattoreilla haluttuja tuloksia:

- Jos "-"-operaattoreita on parillinen määrä, kyseessä on yhteenlasku
- Jos "-"-operaattoreita on pariton määrä, kyseessä on vähennyslasku

### Käyttöliittymän testaus

Sovelluksen käyttöliittymä on suoritettu manuaalisesti. Yrityksen ja erehdyksen kautta ohjelma on saatu toimimaan toivotulla tavalla

## Ongelmat

Ohjelma hyväksyy muitakin merkkejä yllä mainittujen lisäksi. Muita kuin sallittuja merkkejä käyttämällä ohjelma ei tiedä, miten sen tulisi menetellä, jolloin ohjelma kaatuu.