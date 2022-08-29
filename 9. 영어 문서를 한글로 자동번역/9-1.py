import googletrans

traslator = googletrans.Translator()

str1 = "행복하세요"
result1 = traslator.translate(str1, dest='en', src='auto')
print(f"행복하세요 ======> {result1.text}")


str2 = "I am happy"
result2 = traslator.translate(str2, dest='ko', src='en')
print(f"I am happy ======> {result2.text}")

# 9-2.py 사용 가능한 언어
lang = googletrans.LANGCODES
print(lang)

