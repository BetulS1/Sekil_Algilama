import numpy as np
import cv2

img = cv2.imread('ucgen.jpg')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Görüntüyü ikili görüntüye dönüştürme
# (yalnızca siyah beyaz görüntü).

deger , sınır = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
sekil , durum = cv2.findContours(sınır, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#aynı renk veya yoğunlukta bölge seçerek görüntüdeki şekilleri algılama

for cevre in sekil: #şeklin kenarlarının piksel taraması için döngü 
    kenar = cv2.approxPolyDP(cevre, 0.01* cv2.arcLength(cevre, True), True)
    cv2.drawContours(img, [kenar], 0, (0, 0, 0), 5)
    x = kenar.ravel()[0]
    y = kenar.ravel()[1] - 5
    if len(kenar) == 3:
        cv2.putText( img, "Ucgen", (x, y), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 0) )
    else: 
        cv2.putText( img, "Ucgen Degil", (x, y), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 0) )

cv2.imshow('! UCGEN MI KONTROLU !', img)
cv2.waitKey(0)
cv2.destroyAllWindows()