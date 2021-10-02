
def countHighlyProfitableMonths(stockPrices, k):
    # Write your code here
    count = 0
    for i in range(len(stockPrices) - k + 1):
        if stockPrices[i:i+k] == sorted(stockPrices[i:i+k]):
            count += 1
    return count
stocks = [5, 3, 5, 7, 8]
k = 3
print(countHighlyProfitableMonths(stocks, k))
