'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Ölüm Miktarı Ortalama Kaydırma (Moving Average) Tahmini 
* Yüzde 75'lik eğitim seti oranı RMSE değerini en uygun veriyor (107)
* Tarih: 04 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''


from pandas import Series
from pandas import DataFrame
from pandas import concat
from statsmodels.tsa.ar_model import AR
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas import read_csv

# verisetini yükle
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[5])

# erteli verisetini olşutur
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t', 't+1']

# eğitim ve test setini ayır
X = dataframe.values
train_size = int(len(X) * 0.75)
train, test = X[1:train_size], X[train_size:]
train_X, train_y = train[:,0], train[:,1]
test_X, test_y = test[:,0], test[:,1]

# eğitim setinde kalıcı model
train_pred = [x for x in train_X]

# hata kalıntılarını hesapla
train_resid = [train_y[i]-train_pred[i] for i in range(len(train_pred))]

# eğitim seti kalıntılarını modelle
model = AR(train_resid)
model_fit = model.fit()

window = model_fit.k_ar
coef = model_fit.params

# test setinde ileri doğru adımla
history = train_resid[len(train_resid)-window:]
history = [history[i] for i in range(len(history))]
predictions = list()

for t in range(len(test_y)):
	# kalıcılık
	yhat = test_X[t]
	error = test_y[t] - yhat
	# tahmin hatası
	length = len(history)
	lag = [history[i] for i in range(length-window,length)]
	pred_error = coef[0]
	for d in range(window):
		pred_error += coef[d+1] * lag[window-d-1]
	# tahmini düzelt
	yhat = yhat + pred_error
	predictions.append(yhat)
	history.append(error)
	print('predicted=%d, expected=%d' % (yhat, test_y[t]))
	# hata
rmse = sqrt(mean_squared_error(test_y, predictions))
print('Test RMSE Karekök Hata Değeri: %.2d' % rmse)

# tahmin edilen hatayı plotla
pyplot.plot(test_y)
pyplot.plot(predictions, color='red')
pyplot.show()
