from urllib import response
import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0',
    #     'Content-Type': 'text/html; charset=utf-8'
    # }
    
    # {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    my_headers = {
    'User-Agent' : 'PostmanRuntime/7.29.2',
    'Accept' : '*/*',
    'Connection' : 'keep-alive',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie':'__cf_bm=o5rtg2t4W6w6qZRwvXjfYjRESMdvF83jt5VvCYIX1kc-1661167606-0-AaC9d14xExrzU+6C0a3q7Lkj2q1L774s4GG0iovFs68EFNDd8OsD097+GOcVBRq3CW1+45A4so5BU45Zq1oqNy4=; firstUdid=1; smd=26e2a6d752fb6d5449be84b00f2afe18-1661167606; udid=26e2a6d752fb6d5449be84b00f2afe18; __cflb=02DiuF9qvuxBvFEb2qB1U5CGcm1MTgrGUztExvBaaBBwa'
}
    
    headers={'User-Agent': 'Mozilla/5.0'}
    # https://kr.investing.com/currencies/usd-krw
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers = headers)
    response2 = requests.get("https://kr.investing.com/currencies/usd-krw")
    print('response>> ',response)
    print('response2>> ',response2)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test':'instrument-price-last'})
    print(containers)

get_exchange_rate('usd','krw')