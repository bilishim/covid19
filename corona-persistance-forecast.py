'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Onaylı Vaka Kalıcılık Tahmin Testi,
* Toplam verinin yüzde 66'sı eğitim, yüzde 33 veri test veri setine bölünüyor.
* Tarih: 04 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from math import sqrt

	
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])

# Erteli veriyi oluştur
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t', 't+1']

print(dataframe)

# veriyi eğitim ve test setlerine bölümle
X = dataframe.values
train_size = int(len(X) * 0.66)
train, test = X[1:train_size], X[train_size:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]


# kalıcılık modeli
def model_persistence(x):
	return x

# ileri-adımlama ile geçerlilik testi
tahminler = list()
for x in test_X:
	yhat = model_persistence(x)
	tahminler.append(yhat)
	
#kalıcılık modeli, t+1 zamanının verisi t ile öğrenilen basit ama etkin bir yöntemdir.
print(tahminler)

rmse = sqrt(mean_squared_error(test_y, tahminler))

print('Test RMSE Karekök Hata Oranı: %.2d' % rmse)

# sonuçları ekrana plotla
# mavi çizgi eğitim, yeşil çizgi test, kırmızı çizgi ise tahmin
pyplot.plot(train_y)
pyplot.plot([None for i in train_y] + [x for x in test_y])
pyplot.plot([None for i in train_y] + [x for x in tahminler])
pyplot.show()