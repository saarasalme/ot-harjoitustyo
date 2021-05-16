# RoniPoika 

Pelissä on ideana keräillä pieniä herkkuja ja väistellä suuria herkkuja. Peli on yksinpeli, ja vaikenee pelin edetessä.

RoniPoika on ohjelmistotekniikan kurssin harjoitustyö.

## Huomio Python-versiosta

Ohjelma on testattu Python-versiolla '3.9.0'. Ainakin versiosta '3.6' uudemmat toimivat.

## Dokumentaatio

[Käyttöohje](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Tuntikirjanpito](https://github.com/saarasalme/ot-harjoitustyo/blob/main/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

## Asennus

Ohjelman käynnistämistä varten täytyy asentaa *Poetry* työkalu. Asennusohjeet löytyvät [täältä](https://python-poetry.org/docs/)

Jos Poetry ei jostakin syystä toimi suoraan komentoriviltä, voi työkalun UNIX järjestelmillä käynnistää suoraan komennolla

```
python3 ~/.poetry/bin/poetry {komento}
```

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.


### Pylint

Pylintin pystyy suorittamaan komennolla

```bash
poetry run invoke lint
```


*Python projekti*
**Tekijä Saara Salmensaari**
