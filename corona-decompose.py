'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Test Miktarı Bileşenlerine Ayırma
* Observed, Trend, Seasonal, Residual
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose

series = Series.from_csv('corona-virus-istatistikleri-resampled.csv', header=0)
result = seasonal_decompose(series, model='multiplicative')
result.plot()
pyplot.show()




