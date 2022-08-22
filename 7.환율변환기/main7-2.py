from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.currencies)
print(cc.convert(1,'USD','KRW')) # 1336.1746568529938
# https://kr.investing.com/
# https://kr.investing.com/currencies/usd-krw 1,344.02
