import requests
import re

# Create your views here.

with open(r'C:\Users\Вероника\Desktop\курсы\it academy\MyDjango\src\test_bd\text.txt') as f:
    tx = f.readlines()
    #print(tx)
    safari = 'Safari'
    data1 = '17/May'

#запросы на 17 мая через Firefox
    firefox =  'Firefox'
    baza = {}
    full_request = []
    list_firefox = []
    for line in tx:
        if firefox in line:
            if data1 in line:
                full_request.append(line)
                list_firefox.append(firefox)
    #print(full_request)
    #print(list_firefox)

    ip_data17 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    all_ip = []
    ind = 0
    for ip in full_request:
        ip = re.findall(ip_data17, full_request[ind])
        all_ip.append(ip)
        ind +=1
    #print(all_ip)