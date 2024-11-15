from array import *


def stockprofit(arr,arr_size):
    profit = 0
    for i in range(1,arr_size):
       if arr[i] > arr[i - 1]:
          profit += arr[i]  - arr[i -1]
    return profit      
stocks = array("i", [100,230,300,500,280,600,239,290,645,900])
stock2 = array("i", [343,566,200,700,100,800,567,300,759,350,200])

print(stockprofit(stocks,10))
print(stockprofit(stock2,11))