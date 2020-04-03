'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Onaylı Vaka Durağanlık Ölçümü
* Test sonucunda elimizdeki verinin non-stationary olduğunu görüyoruz 
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import Series
from matplotlib import pyplot
from numpy import log
from pandas import read_csv

#Test sonucunda non-stationary olduğunu görüyoruz elimizdeki verinin

series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
X = series.values
split = int(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))


series.hist()
pyplot.show()


# Log transform yaparak elimizdeki veriyi yumuşatıyoruz, değerler kısmen daha iyi

X = series.values
X = log(X)

split = int(len(X) / 2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))



pyplot.hist(X)
pyplot.show()

pyplot.plot(X)
pyplot.show()




