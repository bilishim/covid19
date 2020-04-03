'''
* Zaman Serisi Tahmini Uygulamaları
* Görüldüğü gibi karekök transform daha çigisel ve eşit bir dağılım sunmaktadır.
* Corona Virüs Günlük Onaylı Vaka Karekök ve Log Transform
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import Series
from pandas import DataFrame
from numpy import sqrt
from matplotlib import pyplot
from numpy import log

series = Series.from_csv('corona-virus-istatistikleri-resampled.csv', header=0)
dataframe = DataFrame(series.values)
dataframe.columns = ['Gunluk Onayli Vaka']
pyplot.figure("Günlük Onaylı Vaka")
# line plot
pyplot.subplot(211)
pyplot.plot(dataframe['Gunluk Onayli Vaka'])
# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['Gunluk Onayli Vaka'])
pyplot.show()



#Karekök Transform
series = Series.from_csv('corona-virus-istatistikleri-resampled.csv', header=0)
dataframe = DataFrame(series.values)
dataframe.columns = ['Gunluk Onayli Vaka']
dataframe['Gunluk Onayli Vaka'] = sqrt(dataframe['Gunluk Onayli Vaka'])
pyplot.figure("Günlük Onaylı Vaka Karekök Transform")
# line plot
pyplot.subplot(211)
pyplot.plot(dataframe['Gunluk Onayli Vaka'])
# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['Gunluk Onayli Vaka'])
pyplot.show()


#Log Transform
dataframe = DataFrame(series.values)
dataframe.columns = ['Gunluk Onayli Vaka']
dataframe['Gunluk Onayli Vaka'] = log(dataframe['Gunluk Onayli Vaka'])
pyplot.figure("Günlük Onaylı Vaka Log Transform")
pyplot.subplot(211)
pyplot.plot(dataframe['Gunluk Onayli Vaka'])
# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['Gunluk Onayli Vaka'])
pyplot.show()






