#brute force soultion

prices=[7,1,5,3,6,4]
def maxProfit(prices):
    max_profit=0
    profit=0
    for i in range(0,len(prices)):
        profit=0
        for j in range(i,len(prices)-1):
            profit=max(profit,prices[j+1]-prices[i])
        max_profit=max(max_profit,profit)
    return max_profit

print(maxProfit(prices))

#now try optimal solution

def max_profit_optimal_solution(prices):
    min_buy_price=float("inf")
    max_price=0

    for i in range(0,len(prices)):
        min_buy_price=min(min_buy_price,prices[i])
        max_price=max(max_price,prices[i]-min_buy_price)

    return max_price

print(max_profit_optimal_solution(prices))
        