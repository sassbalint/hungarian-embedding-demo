kkkt = kakukktojás

# TODO (current)

 - [ ] **adatbázis** felhúzása, feladatok adatbázisban tárolása, előszedése!
XXX XXX XXX

# TODO (short term)

 - [ ] **UI design:** rögtön jöjjön ki egy fela (a sorszámával)\
balra: nehézség (1/2/3) (esetleg piktogrammal) + 'random' gomb\
jobbra: textbox/legördülők sorszámválasztáshoz + 'ezt kérem' gomb\
**működés:** random: létrehozza, sorszámot ad neki, kirakja\
ezt kérem: megnézi, hogy az sqlite-ban benne van-e az adott sorszám,
ha nincs létrehozza azzal a sorszámmal (elteszi az sqlite-ba), és kirakja\
a rendszer **reakciója** a tippre:\
zöld pipa vagy piros x (ekkor mutassa meg a jót vmi nyíllal!)\
plusz: visszajelzési lehetőség: rendben volt vs rossz a feladat +
textbox-ba komment + 'ezt gondolom' gomb

 - [ ] **nehézség:** 1/2/3 -- x, x/2 x/5 távolságra van a kkkt a többitől,
ilyesmi... + kikutatni, hogy mifélét bír jól megoldani és mifélét nem! :)

 - [ ] **log**olni mindent:\
két tanulság: felhasználók viselkedése, ill. mennyire jók a feladványok
(= mennyire lehet embeddinggel jó kkkt feladatokat csinálni)!

 - [ ] hogy működik :arrow_right: README.md

 - [ ] logó: ilyesmi: ooOo

 - [ ] `http://www.nytud.hu/kakukktojas` URL-t intézni

# INFO

 - [ ] az **embedding** milyensége\
ragozott szavak akadnak benne: krumplit, azt, fogja, embert

 - [ ] *ami rossz:*
paradicsom,paprika,répa,alma :arrow_right: paradicsom;
kutya,macska,disznó,farkas :arrow_right: disznó;
kutya,cica,disznó,farkas :arrow_right: cica;
levél,fa,virág,rózsaszín :arrow_right: levél (Máty. Sz.) -- sztem a 2 jelentése miatt!

 - [ ] *ami jó:*
növény,fa,virág,rózsaszín :arrow_right: rózsaszín (ez már jó!);
Tibor,Gábor,Péter,Noémi :arrow_right: Noémi;
alma,körte,padlizsán,szőlő :arrow_right: padlizsán (Szab. E.)

# TODO (long term)

 - [ ] angol nyelvű felület

 - [ ] bolgba sztori + link oda-vissza

 - [ ] kkkt-csináló:
1. 3 ua mellé mondjon egy 4-diket, ami a kkkt lesz
2. 2 ua + egy kkkt mellé mondjon még egy beleillőt :arrow_right: "küldhetem másnak"
3. feladat egy szó megadásával :arrow_right: "magamnak"
4. mind a 4 (vagy több) szót adhassam meg én :) + ilyenkor ellenőrzés kell,
hogy jól oldja-e meg, és ha igen, csak akkor menjen az adatbázisba! :)

 - [ ] jobb embeddinget csinálni, nagyobb korpuszból?

 - [ ] OOV szavak kezelése
jelenleg az OOV szavakkal nem tud mit kezdeni, ki kell hagyni őket!
sajnos csomó minden nincs benne: megragasztjuk, nyaklánc, fülbevaló, kantár
kék,piros,sárga,megcsinál :arrow_right: sárga (mert OOV!)

 - [ ] daemon -- válaszidő most: 2s

# DONE

 - [x] hogy kell használni :arrow_right: README.md

 - [x] deploy on _heroku_! :)
-- "fejl: oli + éles: juni + Iván segít a dockeresítésben" _helyett_

 - [x] _flask_ webapp kész: [`odd-one-out-basic.py`](odd-one-out-basic.py)
-- Iván tanácsára használom a flask-et! :)

 - [x] basic script: [`ooo.py`](ooo.py)

 - [x] fork

