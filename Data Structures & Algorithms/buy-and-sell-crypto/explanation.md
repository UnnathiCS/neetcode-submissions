# BRUTE FORCE METHOD - O(n^2)
as we cannot sell before buying the stock first we will use 2 pointers method where one loop runs from 0th index to last but one and second loop runs from i+1 index to last element
so if the prices[i]<prices[j] then we can consider it as buy and update the profit to max_val-min_val if we get a value bigger in j loop the we will update the profit accordingly .

Algorithm
Initialize res = 0 to store the maximum profit.
Loop through each day i as the buy day.
For each buy day, loop through each day j > i as the sell day.
Calculate the profit prices[j] - prices[i] and update res.
Return res after checking all pairs.


# TWO POINTER METHOD - USING SINGLE WHILE LOOP - O(n)
instead of using nested for loops as we dont really need to keep track of the buy item continuously once we intialize it will remain same as long as we not find a value less than that 
item for that we can use the condition say first check if right pointer is greater than left one i.e 0 if yes then we can make profit otherwise we found cheaper stock value to buy so we update the L pointer to right's value so we reduce O(n^2) to O(n) complexity

Algorithm
Set two pointers:
l = 0 (buy day)
r = 1 (sell day)
maxP = 0 to track maximum profit
While r is within the array:
  If prices[r] > prices[l], compute the profit and update maxP.
  Otherwise, move l to r (we found a cheaper buy price).
  Move r to the next day.
Return maxP at the end.
