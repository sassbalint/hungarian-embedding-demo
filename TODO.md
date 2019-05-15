kkkt = kakukktojás

# TODO (short term)

 - [ ] UI design: rögtön jöjjön ki egy fela (a sorszámával)\
balra: nehézség (1/2/3) (esetleg piktogrammal) + 'random' gomb\
jobbra: textbox/legördülők sorszámválasztáshoz + 'ezt kérem' gomb\
**működés:** random: létrehozza, sorszámot ad neki, kirakja\
ezt kérem: megnézi, hogy az sqlite-ban benne van-e az adott sorszám,
ha nincs létrehozza azzal a sorszámmal (elteszi az sqlite-ba), és kirakja\
a rendszer **reakciója** a tippre:\
zöld pipa vagy piros x (ekkor mutassa meg a jót vmi nyíllal!)\
plusz: visszajelzési lehetőség: rendben volt vs rossz a feladat
+ textbox-ba komment + 'ezt gondolom' gomb

 - [ ] nehézség: 1/2/3 -- x, x/2 x/5 távolságra van a kkkt a többitől,
ilyesmi...

 - [ ] logolni mindent:\
két tanulság: felhasználók viselkedése, ill. mennyire jók a feladványok
(= mennyire lehet embeddinggel jó kkkt feladatokat csinálni)!

 - [ ] melyik gépre lehet tenni

 - [ ] (http://www.nytud.hu/kakukktojas)[http://www.nytud.hu/kakukktojas]
URL-t intézni

 - [ ] logó: ilyesmi: ooOo

 - [ ] ragozott szavak vannak az embeddingben vagy lemmák?

 - [ ] mi történik az OOV szavakkal?

 - [ ] hogy működik -> README.md

 - [ ] hogy kell használni -> README.md

# TODO (long term)

 - [ ] angol nyelvű felület

 - [ ] bolgba sztori + link oda-vissza

 - [ ] ooo.py: `['kék', 'piros', 'sárga', 'megcsinál']` -- ez miért 'sárga'?

 - [ ] jobb embeddinget csinálni

 - [ ] kkkt-csináló:\
1. 3 ua mellé mondjon egy 4-diket, ami a kkkt lesz\
2. 2 ua + egy kkkt mellé mondjon még egy beleillőt -> "küldhetem másnak"\
3. feladat egy szó megadásával :arrow_right: "magamnak"

 - [ ] daemon -- válaszidő most: 2s

# DONE

 - [x] basic script: [`ooo.py`](ooo.py)

 - [x] fork

