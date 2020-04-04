'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Onaylı Vaka Tahminlerdeki Hata Artığı Gösterimi
* Tarih: 04 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

# line plot of residual errors
from pandas import Series
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
from pandas import read_csv


series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])


# erteli (lagged) veri setini oluştur
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t', 't+1']

# eğitim ve test setlerine ayır
X = dataframe.values
train_size = int(len(X) * 0.66)
train, test = X[1:train_size], X[train_size:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

# kalıcılık modeli
predictions = [x for x in test_X]

# artık hataları hesapla
residuals = [test_y[i]-predictions[i] for i in range(len(predictions))]
residuals = DataFrame(residuals)

# hata artıklarını göster
residuals.plot()
pyplot.show()