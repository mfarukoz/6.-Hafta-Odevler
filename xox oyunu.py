# coding=utf-8
import random

tahta = [["___", "___", "___"],  #ekrana bastırılan tahta
["___", "___", "___"],
["___", "___", "___"]]

kazanma_durumu = [[[0, 0], [1, 0], [2, 0]], #kazanma durumlarının listesi
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

bos_liste = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]] #oyuncuların oynayabilecegi hamleler

koseler=[[0,0],[2,0],[0,2],[2,2]] #tahtanın koseleri

x_durumu = []   # oyuncunun hamlelerinin depolandıgı liste
o_durumu = []   # bilgisayarın hamlelerinin depolandıgı liste

print("\n"*15)
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)  # tahtanın ekrana ortalanıp satır satır yazdırılması

sira =random.randint(1,2)  # oyuna kimin baslayacagının random belirlenmesi

while True:
    kalan_boslar = [z for z in bos_liste if z not in x_durumu and z not in o_durumu]  #tahtada kalan bos hamleler
    if kalan_boslar==[]:  # kalan boslar listesi bos ise oyun biter
        print('KAZANAN YOK.')
        quit()

    if sira ==1:  # oyuncunun hamle sırası
        isaret = "X".center(3)  #isaret degiskeni oyuncu icin x
        x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))  #oyuncu hamlesi icin satır nosu girisi
        if x == "q":
            break
        y = input("soldan sağa [1, 2, 3]: ".ljust(30)) #oyuncu hamlesi icin sutun nosu girisi
        if y == "q":
            break
        x = int(x) - 1  #oyuncu koordinat giridlerini liste indisine gore ayarlar
        y = int(y) - 1

    else: # bilgisayarın hamle sırası
        isaret = "O".center(3)  #isaret degiskeni oyuncu icin o
        for i in kazanma_durumu:  #i degiskeni kazanma durumlarının herbir elemanı icin(herbir eleman tahtanın üç kutusuna karsılık gelir)
            ara_basamak1=[z for z in i if z in o_durumu] #kazanma durumlarının herbir elemanında o'ın oldugu kutuları depolar
            ara_basamak2=[z for z in i if z in x_durumu] #kazanma durumlarının herbir elemanında x'ın oldugu kutuları depolar

            if len(ara_basamak1)==2: #eger 48.satırdaki liste iki eleman iceriyorsa(yani kazanma listesinin herhangi bir elemanında iki o varsa)
                o=[n for n in i if n not in ara_basamak1 and n not in ara_basamak2] #47.satırdaki i'nin icinde-
                print (o)  #48. ve 49. satır elemanlarının olmadıgı kutuları o degiskenine ata

                if len(o)==1: #52.satırdaki o degiskeni 1 elemanlı ise(yani tahtada o o - durumu varsa)
                    x = o[0][0]  # o dagiskenin (ornegin; o=[[1,2]] olacagında) elemanının 0. ve 1. elemanını-
                    y = o[0][1]  #x ve y ye atama
                    sira=1 #sırayı oyuncuya verme
                    print ('1')

            elif len(ara_basamak2)==2: #49.satırdaki liste iki eleman iceriyorsa(yani kazanma listesinin herhangi bir elemanında iki x varsa)
                o = [n for n in i if n not in ara_basamak2 and n not in ara_basamak1] #47.satırdaki i'nin icinde-
                 #48. ve 49. satır elemanlarının olmadıgı kutuları o degiskenine ata
                if len(o)==1:  #52.satırdaki o degiskeni 1 elemanlı ise(yani tahtada x x - durumu varsa)
                    x=o[0][0] #56,57,58. satırlar ile aynı durum
                    y=o[0][1]
                    sira=1
                    print ('2')

        if sira==2: #45.satırdaki else bloguna girmediyse(o halde bilgisayar henuz hamle yapmadı)
            for b in kalan_boslar: #kalan boslar listesindeki herbir eleman icin
                ara_basamak1=[] # bu liste boslatılıyor
                for n in o_durumu: # bilg.ın yaptıgı hamlelerin listesinin herbir elemnı icin
                    for m in x_durumu:# oyuncunun yaptıgı hamlelerin listesinin herbir elemnı icin
                        ara_basamak1+=[z for z in kazanma_durumu if b in z and n in z and m not in z and z not in ara_basamak1]
                        #icinde bos ve o olan ama x olmayan kazanma durumu listesinden bir elemanı(yani uc kutu) ara_basamak1'e ekliyecek
                        #'z not in ara_basmak1' ile aynı elemanın tekrar alınması engelenmis oldu
                if len(ara_basamak1)==2: #74 teki liste iki elemanlıysa (yani 0 b -)
                    x = b[0]    # 70.satırdaki b ornekteki -->          (     - - -)
                    y = b[1]    # konumdaysa bilg. b'ye oynar           (     - o -)
                    sira=1
                    print ('3')
                elif len(o_durumu)==2:
                    o=random.choice(kalan_koseler)
                    x = o[0]
                    y = o[1]
                    sira = 1

            if len(x_durumu)==1 and len(o_durumu)==0:
                if [1,1] in kalan_boslar:
                    x=1
                    y=1
                    sira=1
                print ('5')

            elif len(x_durumu)==0 and len(o_durumu)==0:
                o=random.choice(koseler)
                x = o[0]
                y = o[1]
                sira = 1
                print (6)


            elif len(o_durumu)==1 and len(x_durumu)==1:
                kalan_koseler=[z for z in koseler if z not in x_durumu and z not in o_durumu]
                o=random.choice(kalan_koseler)
                x = o[0]
                y = o[1]
                sira =1
                print (7)

            if sira==2:
                print ('6')
                o=random.choice(kalan_boslar)
                x=o[0]
                y=o[1]
                print (8)

    print("\n" * 15)
    if [x,y] in kalan_boslar:
        tahta[x][y] = isaret

        if isaret == "X".center(3):
            x_durumu += [[x, y]]
            sira = 2

        elif isaret == "O".center(3):
            o_durumu += [[x, y]]
            sira = 1

    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n" * 2)

    for i in kazanma_durumu:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]

        if len(o) == len(i):
            print('RISE OF MACHINES')
            quit()

        if len(x) == len(i):
            print("TEBRİKLER, KAZANDIN!")
            quit()




