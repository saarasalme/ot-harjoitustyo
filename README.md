# RoniPoika 

Pelissä on ideana keräillä pieniä herkkuja ja väistellä suuria herkkuja. Peli on yksinpeli, ja vaikenee pelin edetessä.

RoniPoika on ohjelmistotekniikan kurssin harjoitustyö.

## Huomio Python-versiosta

Ohjelma on testattu Python-versiolla '3.9.0'. Etenkin vanhempien Python-versioiden kanssa saattaa ilmetä ongelmia.

## Dokumentaatio

[Tuntikirjanpito](https://github.com/saarasalme/ot-harjoitustyo/blob/main/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

## Asennus

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


*Python projekti*
**Tekijä Saara Salmensaari**
