'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Onaylı Vaka sayısını 3 kademeli eğitim ve test setine ayrıştırma
* Tarih: 04 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

# tekrarlanan zaman serisi eğitim-test bölümlerini hesapla
from pandas import Series
from sklearn.model_selection import TimeSeriesSplit
from matplotlib import pyplot
from pandas import read_csv


series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
X = series.values
splits = TimeSeriesSplit(n_splits=3)
pyplot.figure(1)
index = 1

for train_index, test_index in splits.split(X):
	train = X[train_index]
	test = X[test_index]

	print('Gözlem: %d' % (len(train) + len(test)))
	print('Eğitim Gözlemi: %d' % (len(train)))
	print('Test Gözlemi: %d' % (len(test)))

	pyplot.subplot(310 + index)
	pyplot.plot(train)
	pyplot.plot([None for i in train] + [x for x in test])
	index += 1
	
pyplot.show()



