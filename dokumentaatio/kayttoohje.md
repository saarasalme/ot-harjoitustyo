# Käyttöohje

Lataa projektin viimeisin lähdekoodi [täältä](https://github.com/saarasalme/ot-harjoitustyo/releases/tag/1.0).

## Ohjelman käynnistäminen

Ohjelman käynnistämistä varten täytyy asentaa *Poetry* työkalu. Asennusohjeet löytyy [täältä](https://python-poetry.org/docs/)

Jos Poetry ei jostakin syystä toimi suoraan komentoriviltä, voi työkalun UNIX järjestelmillä käynnistää suoraan komennolla

```
python3 ~/.poetry/bin/poetry {komento}
```

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Aloitusruutu

Peli käynnistyy aloitusnäkymään:

![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kaytto_ohje_aloitusnaytto.png)

Pelin ohje -näkymän voi avata painamalla O-näppäintä.

Pelin parhaat tulokset -näkymän voi avata painamalla S-näppäintä.

Uuden pelin voi aloittaa painamalla välilyöntiä.

## Ohjeruutu

O-näppäintä painettua avautuu ohjeruutu:

![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kayttoohjeet_ohjeruutu.png)

Pelin ideana on kerätä pienempiä herkkuja ja väistellä isompia.

Taulukosta näkee minkälaisia herkkuja voi syödä milläkin tasolla.

Voit palata aloitusnäkymään painamalla O-näppäintä tai aloittaa pelin painamalla välilyöntiä.

## Peliruutu
Välilyöntiä painettua avautuu peliruutu:

![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kayttoohjeet_peliruutu.png)

Pelaaja liikuttaa hahmoa nuolinäppäimillä. Jokaisesta pienemmästä herkusta saa pisteen. Kymmenen pisteen välein taso nousee,
ja pelaaja voi kerätä uusia herkkuja. Jos pelaaja osuu liian isoon herkkuun tai saa kerättyä 30 herkkua, peli päättyy.

## Loppuruudut
Häviöruutu:

![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kayttoohjeet_havioruutu.png)

Voittoruutu:

![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kayttoohjeet_voittoruutu.png)

Kuten aloitusruudussa, pelaaja voi katsoa ohjeet painamalla O-näppäintä, avata parhaat tulokset S-näppäimellä tai aloittaa uuden pelin 
painamalla välilyöntiä. 

## Parhaat tulokset -ruutu
Pelaaja voi siirtyä parhaat tulokset ruudulle S-näppäimellä kaikista muista näytöistä paitsi pelinäytöstä. 

Parhaat tulokset -ruutu:

![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kayttoohjeet_parhaat_tulokset-ruutu.png)

Tulokset päivittyvät aina pelin päätyttyä. 

Pelin voi sulkea milloin tahansa painamalla esc-näppäintä tai sulkemalla ikkunan.


