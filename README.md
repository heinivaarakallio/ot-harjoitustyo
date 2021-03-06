# Asteroids
Sovellus on yksin pelattava Asteroids-peli. Pelissä ohjataan yhtä avaruussukkulaa, jolla ammutaan asteroideja. Avaruussukkulan suuntaa ja nopeutta voi itse säädellä.
## Python-versio
Sovellus on tehty Python-versiolle `3.8`.
## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/heinivaarakallio/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/heinivaarakallio/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/heinivaarakallio/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/heinivaarakallio/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
## Komentorivitoiminnot
Sovellus käynnistetään komennolla:
```bash
poetry run invoke start
```
Testaus suoritetaan komennolla:
```bash
poetry run invoke test
```
Testikattavuusraportin näkee komennolla:
```bash
poetry run invoke coverage report
```
Pylint:
```bash
poetry run invoke lint
```
