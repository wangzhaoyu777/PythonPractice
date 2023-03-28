# Zhaoyu Wang developed
# time: 2023-03-26 11:10 a.m.
import math
import urllib.request
import schedule
import time

# print(dir(math))
# print(math.pi)
# print(math.pow(2, 4))
# print(urllib.request.urlopen('http://www.google.com').read)

def job():
    print('ok-----')
schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
