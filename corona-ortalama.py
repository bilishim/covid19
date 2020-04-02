'''
* Zaman Serisi Tahmini Uygulamaları
* Corona Virüs Günlük Vaka ve Günlük Ölüm Ortalama Verileri
* Tarih: 03 Nisan 2020
* Hazırlayan: Bilishim Siber Güvenlik ve Yapay Zeka
* Bu çalışmalar yalnızca ARGE ve bilgiyi geliştirmek maksadıyla hazırlanmış olup, herhangi bir resmi temsil ya da bağlayıcılığı yoktur.
'''

from pandas import Series
from pandas import DataFrame
from pandas import concat
from pandas import read_csv


print("\nGünlük Vakaların Ortalama Değerleri\n")

series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[2])
temps = DataFrame(series.values)
shifted = temps.shift(1)
window = shifted.rolling(window=2)
means = window.mean()
dataframe = concat([means, temps], axis=1)
dataframe.columns = ['ortalama(t-1,t)', 't+1']
print(dataframe)


print("\nGünlük Ölümlerin Ortalama Değerleri\n")

series = read_csv('corona-virus-istatistikleri-resampled.csv', header=0, usecols=[3])
temps = DataFrame(series.values)
shifted = temps.shift(1)
window = shifted.rolling(window=2)
means = window.mean()
dataframe = concat([means, temps], axis=1)
dataframe.columns = ['ortalama(t-1,t)', 't+1']
print(dataframe)





