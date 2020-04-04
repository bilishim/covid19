'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Ölüm Miktarı AutoRegression Tahmini
* 7 günlük window değeri 60 ile en optimal sonucu vermektedir
* Tarih: 04 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''


from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas import read_csv

# verisetini yükle
series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[8])
# veriyi bölümle
X = series.values
egitim, test = X[1:len(X)-7], X[len(X)-7:]
# egitim autoregression
model = AR(egitim)
model_fit = model.fit()
window = model_fit.k_ar
coef = model_fit.params

# test üzerinde ileri doğru adımla
tarihce = egitim[len(egitim)-window:]
tarihce = [tarihce[i] for i in range(len(tarihce))]
tahminler = list()

for t in range(len(test)):
	length = len(tarihce)
	lag = [tarihce[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	obs = test[t]
	tahminler.append(yhat)
	tarihce.append(obs)
	print('tahmin=%d, beklenen=%d' % (yhat, obs))

rmse = sqrt(mean_squared_error(test, tahminler))
print('Test RMSE Karekök Hata Oranı: %.2d' % rmse)

# plot
pyplot.figure('Günlük Vefat Miktarı Artışı AutoRegression')
pyplot.plot(test)
pyplot.plot(tahminler, color='red')
pyplot.show()
