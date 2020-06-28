# Salyangoz

Salyangoz dili.

## Sözdizimi

### Değişken atama

````python
bir_değişken = 1
başka_bir_değişken = 2.54
bambaşka_bir_değişken = "Merhaba Dünya!"
sadece_değişken = bir_değişken
````

### Fonksiyon çağırma

````python
fonksiyon()
fonksiyon1(argüman)
fonksiyon2(argüman1, argüman2)
````

### Giriş/Çıkış

````python
isim = oku("Adın ne? > ")
yaz("Merhaba", isim + "!")
````

### Yorumlar

#### Tek satırlık yorum

````python
# bu bir yorum ve kod olarak algılanmıyor
a = 1 # bu da bir yorum
````

#### Blok yorum

````python
<- Bu yorum birden fazla satır devam edebilir
Blok yorumlar <- iç içe -> gömülebilir ->
````

### İşleçler

#### Aritmetik işleçler

````python
yaz(1 + 1)  # toplama
yaz(3 - 1)  # çıkarma
yaz(2**3)   # üs
yaz(5 / 2)  # bölme
yaz(10 * 7) # çarpma
yaz(3 // 2) # tam (kalansız) bölme
yaz(5 % 3)  # modülo (kalan)
````

#### Karşılaştırma işleçleri

````python
yaz(12 > 1)   # büyüktür
yaz(13 != 78) # eşit değildir
yaz(0 == 0)   # eşittir
yaz(5 < 4)    # küçüktür
yaz(3 >= 4)   # büyük eşittir
yaz(6 <= 2)   # küçük eşittir
````

### Akış kontrolü

#### Koşul Durumları

````python
eğer (1 == 1) ise {
	yaz("1, 1'e eşitir.")
}
````

````python
eğer (1 > 2) ise {
	yaz("Bir, ikiden büyüktür")
} değilse {
	yaz("Bir, ikiden büyük değildir.")
}
````

````python
isim = oku("Merhaba! Adın ne?\n > ")
eğer (uzunluk(isim) <= 3) ise { # gömülü fonksiyon "uzunluk"
	yaz("Adın çok kısaymış.")
} değilse (uzunluk(isim) <= 7) ise {
	yaz("Adın çok da uzun değilmiş.")
} değilse {
	yaz("Adın çok uzunmuş.")
}
````

### Döngüler

````python
i = 0
(i < 5) iken {
	yaz(i)
}
````


## Lisans

Lisans hakkında ayrıntılı bilgi için [LICENSE](LICENSE) dosyasına başvurun.