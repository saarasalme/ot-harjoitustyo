
# Sovellusarkkitehtuuri
 
## Rakenne
 
![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/package_diagram.png)
 
Sovellus koostuu kolmesta pakkauksesta. UI sisältää käyttöliittymään kuuluvat luokat, Logic sisältää sovelluksen logiikkaan liittyvät luokat ja Entities sisältää pelin eri otusten luokat.
 
## Käyttöliittymä
 
Sovelluksen käyttöliittymä koostuu kuudesta näkymästä:
 
	Aloitusnäyttö - Pelin aloitus
	Pistenäyttö - Parhaat tulokset pelissä
	Ohjenäyttö - Ohjeet pelin pelaamiseen
	Pelinäyttö - Itse peli
	Voittonäyttö - Pelin voittamisen jälkeen näytettävä näkymä
	Häviönäyttö - Pelin häviämisen jälkeen näytettävä näkymä
 
![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/RonipoikaNaytot.png)
 
Sovellus käynnistyy aina Aloitusnäyttöön, josta voi kulkea Pistenäyttöön ja Ohjenäyttöön. Näistä kolmesta pystyy myös siirtymään Pelinäyttöön. Pelinäytöstä siirrytään joko Voittonäyttöön, tai Häviönäyttöön, joista molemmista pääsee Pistenäyttöön ja Pelinäyttöön. Häviönäytöstä pääsee myös siirtymään Ohjenäyttöön.
 
Kaikki näkymät sisältyvät Game-luokkaan omina metodeinaan.
 
### Sovellluslogiikka
 
Sovelluksen laskentalogiikka kuuluu *logic* kansioon. Kansio sisältää *mover* ja *collision* luokat. Mover -luokka sisältää pelaajan ja *Snack* olioiden liikuttamiseen liittyvän logiikan. Collision -luokka sisältää pelaajan ja *Snack* olioiden välisten törmäysten laskentaan kuuluvan logiikan.
 
![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/RoniPoikaLogiikka.png)
 
### Pisteiden tallentaminen
 
Pelaajien pisteet tallennetaan CSV tiedostoon joka sijaitsee sovelluksen *resources* kansiossa. Pisteet kirjataan tiedostoon muodossa`{pisteet},{aika sekunteina}`. Pisteet luetaan Pistenäyttöä varten ja järjestellään suurimman pistemäärän ja pienimmän ajan mukaisesti näytettäväksi.
 
## Peli-loopin kulku
 
![](https://github.com/saarasalme/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/RonipoikaSekvenssi.png)
 
Peli alkaa *roni_poika* tiedostosta loop metodilla. Metodi sisältää pelin toiminnot, Game -luokan *handle_events* ja *draw_screen*. Metodi *handle_events* hoitaa kaikkien pelissä tapahtuvien tapahtumien käsittelyn ja *draw_screen* -luokka hoitaa näytön piirtämisen pelin tapahtumien mukaisesti.
