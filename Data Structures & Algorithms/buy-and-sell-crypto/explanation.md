# BRUTE FORCE METHOD
as we cannot sell before buying the stock first we will use 2 pointers method where one loop runs from 0th index to last but one and second loop runs from i+1 index to last element
so if the prices[i]<prices[j] then we can consider it as buy and update the profit to max_val-min_val if we get a value bigger in j loop the we will update the profit accordingly .

Algorithm
Initialize res = 0 to store the maximum profit.
Loop through each day i as the buy day.
For each buy day, loop through each day j > i as the sell day.
Calculate the profit prices[j] - prices[i] and update res.
Return res after checking all pairs.
