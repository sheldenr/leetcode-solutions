class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # This was the initial solution I came up with to find min stock price
	# minPrice = float("inf")
        # maxProfit = 0

        # for price in prices:
            # minPrice = min(minPrice, price)
            # maxProfit = max(price - minPrice, maxProfit)

        # return maxProfit
	
	# Solution after learning more about leetcode and greedy approach
	minPrice, maxProfit, curr_price = prices[0], float("-inf"), 0

	for price in prices:
    		if price < minPrice:
		        minPrice = price
            
		if price - minPrice > maxProfit:
                	maxProfit = price - minPrice

        return maxProfit

	# got it first try no way !!!
