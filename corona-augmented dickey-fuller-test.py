'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Onaylı Vaka Augmented Dickey-Fuller Testi
* Test sonucunda AFD değerinin 2.015594 olduğunu, dolayısıyla verimizin non-stationary olduğunu görüyoruz
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import Series
from statsmodels.tsa.stattools import adfuller
from pandas import read_csv
from numpy import log

series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
X = series.values
result = adfuller(X)

print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')

for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
	

	
#Log Transformu ile yumuşatma, sonuçta AFD değeri -1.369473 ile nispeten daha iyi
X = log(X)
result = adfuller(X)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))



	
	