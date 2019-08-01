# coding=utf-8
print('''                ________________________________________________________________________________________
                |                                                                                        |
                |                         SAYI TAHMİN-3 OYUNUNA HOŞ GELDİNİZ.                            |
                |                                                                                        |
                |    Bu oyunda siz aklınızdan bir sayı tutacaksınız, bilgisayar bu sayıyı tahmin etmeye  |
                |    çalışacak. Bilgisayar sizin aklınızdan tuttuğunuz sayıyı beş denemede bilirse bilgi-|
                |    sayar bir puan kazanacak, eğer beş denemede bilemezse siz bir puan kazanacaksınız.  |
                |    En fazla beş defa oynanacak oyunlar neticesinde üç puan alan oyunu kazanmış olur.   |
                |                                                                                        |
                |    (Siz aklınızdan tutuğunuz sayıyı her turda bilgisayara girmelisiniz.)Bilgisayarın   |
                |    yaptığı tahmin sizin sayınızdan büyükse '-', küçükse '+' işaretleri ile bilgisayarı |
                |    yönlendirmelisiniz. Eğer bilgisayar sizin sayınızı tahmin ederse bilgisayara tebrik |
                |    mesajı ('Tebrikler, bildin.' gibi) gönderin.                                        |
                |                                                                                        |
                |                                     İYİ EĞLENCELER...                                  |
                ------------------------------------------------------------------------------------------\n\n\n''')
import random
skorOyuncu=0
skorBil=0

while True:
        oyuncuSayı=input(r'''Aklınızdan 1 ile 100 arası bir sayıyı tutunuz ve 'Enter'a basınız.''')
        print('\n'*15)
        sayac=0
        altSinir=1
        ustSinir=100

        while True:

                if sayac>5:
                        print('Bu defa sen kazandın!!!')
                        skorOyuncu += 1
                        print('Bil = ', skorBil, '\n', 'Oyuncu = ', skorOyuncu, sep='')
                        break


                tahmin=random.randint(altSinir,ustSinir)
                sayac+=1
                print(tahmin)

                while True:
                        oyuncu=input('''Biligisayarın yaptığı tahmin 
sayınızdan büyükse '-',
küçükse '+' basınız,
doğru tahmin ettiyse de 'Bildin' yazınız. = ''')
                        print('\n'*15)
                        oyuncu=oyuncu.capitalize()

                        if oyuncu in ('-','+','Bildin'):
                                break
                        else:
                                print ('Sizden istenen şekilde bir yorum yapınız.')

                if oyuncu=='-':
                        ustSinir=tahmin-1

                elif oyuncu=='+':
                        altSinir=tahmin+1

                else:
                        print('Ben kazandım!!!')
                        skorBil+=1
                        print('Bil = ',skorBil,'\n','Oyuncu = ',skorOyuncu,sep='')
                        break

        if skorBil==3:
                print('Oyun bitti, ben kazandım.')
                break

        elif skorOyuncu==3:
                print('Tebrikler, oyunu sen kazandın.')
                break








# ODEV 1: Sayi Tahmin
# 		-Kullanicidan aklindan 0-100 araliginda bir sayi tutmasini isteyin.
# 		-Yazdiginiz kod ile bu sayiyi tahmin etmeye calisin.
# 		-Tahmin sonucunda, kullanicidan alacaginiz input, pc'nin tahmin ettigi sayi kullanicinin belirledigi
# 		 sayidan buyukse kullanici daha dusuk sayi tahmin etmelisin manasinda "-" seklinde olsun, pc'nin tahmin
# 		 ettigi sayi kullanicinin belirledigi sayidan kucukse "+" seklinde olsun.
# 		-Pc'nin tahmini dogru oldugunda da kullanicidan bunu belirtebilecegi bir input isteyin.
# 		-Gelistireceginiz algoritma sayesinde kullanicinin belirledigi sayiyi en az hamlede bilmeye calisin :)
#
# 		Ornek:
#
# 			 Kullanicinin aklindan tuttugu sayi: 56 (kullanicidan bunun icin bir input almayacagiz sadece
# 			 aklinizdan bir sayi belirlemis iseniz oyunumuza baslayabiliriz seklinde bir input alabiliriz.
# 			 Yani belirledigi sayiyi sisteme girmesini istemiyoruz.)
#
# 			 Pc'nin tahmini = 89
# 			 Kullanicinin inputu = -
# 			 Pc'nin tahmini = 45
# 			 Kullanicinin inputu = +
# 			 Pc'nin tahmini = 56
# 			 Kullanicinin inputu = "Enter"

















