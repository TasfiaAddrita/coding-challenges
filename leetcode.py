'''
--- 122. Best Time to Buy and Sell Stock II --- 
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and 
sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

--- Questions --- 
Are the prices in ints or floats?
Is the question asking what the max profit is between two days or all the days? 

--- My approach ---
I drew out the prices array in a notebook and looked for any patterns.

7 1 5 3 6

7 -> 1 -- lose $6 if I buy this stock on the first day
1 -> 5 -- gain $4 
5 -> 3 -- gain $2
3 -> 6 -- gain $3 dollars

As I was calculating the differences for each day, I noticed that you only want to buy when you reach a low number and 
sell when you're on a high number. 
'''

def max_profit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        diff = prices[i] - prices[i + 1]
        if diff < 0:
            # print(f"Bought ${prices[i]} on day {i + 1}")
            profit += (-1) * diff
        # else:
        #     print(f"Sold ${prices[i]} on day {i + 1}")
    return profit


# lst = [7, 1, 5, 3, 6, 4]
# lst = [1, 2, 3, 4, 5]
# lst = [7, 6, 4, 3, 1]

print(max_profit(lst))

'''
--- 4. Median of Two Sorted Arrays ---
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

--- Questions --- 
Are the arrays sorted ascending or descending or both?
Should the return be in float or int?

--- My approach --- 
First I figured it'd be useful to figure out the median index by adding the lengths of both lists 
and dividing them by two. 

I knew I had to combine the arrays in order to find the median. Originally I planned on looping through the 
two arrays through a while loop but then remembered that python has a .extend function. I used the .extend
function and sorted the new array after it. From there, I would return the median number from the indexes
I calculated earlier.

If I wasn't able to use the .extend function, I would loop through the second array and append each element
to the first array. 

This is a decent solution since it runs O(log(m+n)), but I wonder if I built a new array through the while
would be more efficient because I can end the sorting when we reach the median index (so we don't have to 
traverse through all of the elements in both arrays). But this requires a lot of conditionals and keeping 
track of values which can risk the code breaking.
'''

def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    combined_nums = sorted(nums1)
    mid_index = len(combined_nums) // 2

    if len(combined_nums) % 2 == 0:
        return (combined_nums[mid_index] + combined_nums[mid_index - 1]) / 2
    else:
        return combined_nums[mid_index]
