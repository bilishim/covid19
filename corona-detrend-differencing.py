'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Detrend Differencing Yöntemiyle Trend akışının temizlenmesi
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import read_csv
from pandas import datetime
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
import numpy


print("\nGünlük Onaylı Vaka Zaman Grafiği\n")
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
series.plot()
pyplot.show()

print("\nGünlük Vakaların Trend Yükselişinin Ayıklanmış Gösterimi\n")
	
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])

# çizgisel modeli uyarla
X = [i for i in range(0, len(series))]
X = numpy.reshape(X, (len(X), 1))
y = series.values
model = LinearRegression()
model.fit(X, y)
# trendi hesapla
trend = model.predict(X)
# trendi plotla
pyplot.plot(y)
pyplot.plot(trend)
pyplot.show()
# detrend yap
detrended = [y[i]-trend[i] for i in range(0, len(series))]
# ayıklanmış trendi plotla
pyplot.plot(detrended)
pyplot.show()




