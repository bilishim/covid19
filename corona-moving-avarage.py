'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Verisi Ortalama Yumuşatma (Moving Average) ile Öngörü Analizi
* Değerler sonraki analizler için daha düzgün dağılıma sahip olmaktadır
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from math import sqrt
from pandas import Series
from pandas import DataFrame
from numpy import mean
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
from pandas import read_csv


series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
# prepare situation
X = series.values
dataframe = DataFrame(series.values)
dataframe.columns = ['Gunluk Onayli Vaka']

window = 3
history = [X[i] for i in range(window)]
test = [X[i] for i in range(window, len(X))]
predictions = list()

# walk forward over time steps in test
for t in range(len(test)):
	length = len(history)
	yhat = mean([history[i] for i in range(length-window,length)])
	obs = test[t]
	predictions.append(yhat)
	history.append(obs)
	print('öngörülen=%d, bulunan=%d' % (yhat, obs))

rmse = sqrt(mean_squared_error(test, predictions))
print('Test Karekök Ortalama Hata Düzeyi: %.2d' % rmse)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()



