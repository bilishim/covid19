'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Veriler Işığında Plot Grafikleri
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''
from pandas import read_csv
from pandas import Series
from pandas import DataFrame
from matplotlib import pyplot
from pandas import TimeGrouper
from pandas import concat

#Günlük Onaylı Vaka Zaman Grafiği
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
series.plot()
pyplot.show()


#Günlük Ölüm Zaman Grafiği
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[3])
series.plot(style='k.')
pyplot.show()


#Günlük Vaka / Test Oran Dağılım Grafiği
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[9])
series.plot(kind='kde')
pyplot.show()


#Günlere Göre Test Miktarı
series = Series.from_csv('corona-virus-istatistikleri-resampled.csv', header=0)
one_year = series['2020']
groups = one_year.groupby(TimeGrouper('D'))
days = concat([DataFrame(x[1].values) for x in groups], axis=1)
days = DataFrame(days)
days.columns = range(1,22)
days.boxplot()
pyplot.show()



