'''
* Zaman Serisi Tahmini Uygulamaları
* Elimizdeki Mevcut Corona Virüs Günlük Verilerindeki Eksik Verilerin Enterpolasyon ile Tamamlanması 
* Sonuçta elde edilen veriler kullanılarak corona-virus-istatistikleri-resampled.csv hazırlanmıştır.
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import read_csv
from pandas import DataFrame
from pandas import Series
from matplotlib import pyplot


#Günlük Test Miktarının Enterpolasyon ile Yeniden Örneklenmesi
series = read_csv('corona-virus-istatistikleri.csv', header=0, usecols=[1])
temps = DataFrame(series.values)
sampled = temps.interpolate(method ='linear', limit_direction ='backward')
print(sampled)


#Yoğun Bakımdaki Hasta Sayısının Enterpolasyon ile Yeniden Örneklenmesi
series = read_csv('corona-virus-istatistikleri.csv', header=0, usecols=[6])
temps = DataFrame(series.values)
sampled = temps.interpolate(method ='linear', limit_direction ='backward')
print(sampled)


#Entube Hasta Sayısının Enterpolasyon ile Yeniden Örneklenmesi
series = read_csv('corona-virus-istatistikleri.csv', header=0, usecols=[7])
temps = DataFrame(series.values)
sampled = temps.interpolate(method ='linear', limit_direction ='backward')
print(sampled)


#İyileşen Hasta Sayısının Enterpolasyon ile Yeniden Örneklenmesi
series = read_csv('corona-virus-istatistikleri.csv', header=0, usecols=[8])
temps = DataFrame(series.values)
sampled = temps.interpolate(method ='linear', limit_direction ='backward')
print(sampled)



