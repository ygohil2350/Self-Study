# Add Function
# def sum(a, b):
#     return a + b

# print(sum(2, 5))


# Remove duplicates
# def remove_duplicates(initial_list=[]):
#     final_list = []
#     for x in initial_list:
#         if x not in final_list:
#             final_list.append(x)
#     return final_list

# initial_list = [1, 2, 3, 4, 4, 5, 6, 77, 7, 7, 8, 9]
# print(remove_duplicates(initial_list))


# Maximum Count of Positive Integer and Negative Integer
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

# def maximumcount(nums):
#     positive = 0
#     negative = 0
#     for x in nums:
#         if x > 0:
#             positive += 1
#         elif x < 0:
#             negative += 1
#     return positive if positive > negative else negative


# nums = [-3, -2, -1, 0, 0, 1, 2]
# print(maximumcount(nums))


# Two Sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# def twoSum(nums: list[int], target: int):
#     position = []
#     for x in range(len(nums)):
#         for y in range(x + 1, len(nums)):
#             if nums[x] + nums[y] == target:
#                 position.append(x)
#                 position.append(y)
#                 return position


# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))


# Palindrome Number
# def isPalindrome(x: int):
#     return True if str(x) == str(x)[::-1] else False

# print(isPalindrome(121))


# Min Cost Climbing Stairs
# Input: cost[] = [10, 15, 20]
# Output: 15
# Explanation: Cheapest option is to start at cost[1], pay that cost, and go to the top.


# def minCostClimbingStairs(cost):
#     length = len(cost)
#     if length == 0:
#         return 0
#     elif length == 1:
#         return cost[0]
#     arr = [0] * length
#     arr[0] = cost[0]
#     arr[1] = cost[1]

#     for x in range(2, length):
#         arr[x] = cost[x] + min(arr[x - 1], arr[x - 2])
#     return min(arr[-1], arr[-2])


# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# print(minCostClimbingStairs(cost))


# 0 - 1 Knapsack Problem
# Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
# Output: 3
# Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
# Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6]
# Output: 0
# Explanation: Every item has a weight exceeding the knapsack's capacity (3).
# Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3]
# Output: 80
# Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.


# def knapsack(W, val, wt):
#     updatedWTArr = []
#     updatedValArr = []
#     localValue = 0
#     for x in range(len(wt)):
#         if wt[x] <= W:
#             updatedValArr.append(val[x])
#             updatedWTArr.append(wt[x])
#     if len(updatedValArr):
#         finalArr = []
#         for x in range(len(updatedValArr)):
#             finalArr.append(
#                 {
#                     "val": updatedValArr[x],
#                     "wt": updatedWTArr[x],
#                     "multiplier": updatedValArr[x] / updatedWTArr[x],
#                 }
#             )
#         sortedArr = sorted(finalArr, key=lambda x: x["multiplier"], reverse=True)
#         print(sortedArr)
#         localW = W
#         for x in sortedArr:
#             if localW >= x["wt"]:
#                 localValue += x["val"]
#                 localW -= x["wt"]
#         return localValue
#     else:
#         return localValue


# W, val, wt = 5, [1, 9, 2, 9, 4, 4], [5, 2, 3, 4, 9, 6]
# print(knapsack(W, val, wt))


# anagrams problem
# input = ['cat','bat','tac','tab']
# output = [['cat','tac'],['bat','tab']]
# def checkForSameWord(current: str, new: str):
#     return sorted(current) == sorted(new)


# def checkForAnagrams(input: list[str]):
#     returnList = []
#     for x in input:
#         for y in input:
#             if x != y and checkForSameWord(x, y):
#                 print(x != y, checkForSameWord(x, y), x, y)
#                 returnList.append([x, y])
#                 input.remove(y)
#     return returnList


# print(checkForAnagrams(["cat", "bat", "tac", "tab"]))


# Longest Substring Without Repeating Characters
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# def lengthOfLongestSubstring(s: str) -> int:
#     subString = []
#     for x in range(len(s)):
#         currant = [s[x]]
#         for y in range(x + 1, len(s)):
#             if s[y] in currant:
#                 break
#             else:
#                 currant.append(s[y])
#         subString.append(len(currant))
#     return sorted(subString, reverse=True)[0]


# print(lengthOfLongestSubstring("pwwkew"))


# Example 1:
# Input: candies = [5,8,6], k = 3
# Output: 5
# Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

# Example 2:
# Input: candies = [2,5], k = 11
# Output: 0
# Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

# def maximumCandies(self, candies: list[int], k: int) -> int:
#     sumOfAllCandies= sum(candies)
#     if sumOfAllCandies<k:
#         return 0
#     pass


# Max subArray
# Input =[-2,7,-3,4]
# output= 8


# def findMaxSubArray(inputList: list[int]):
#     max = 0
#     for x in range(len(inputList)):
#         if inputList[x] > max:
#             max = inputList[x]
#         sum = inputList[x]
#         for y in range(x + 1, len(inputList)):
#             sum += inputList[y]
#             if sum > max:
#                 max = sum
#     return max


# print(findMaxSubArray([-2, 7, -3, 4]))


# nearly sorted List
# input = [6, 5, 3, 2, 8, 10, 9]
# k = 3


# def nearlySortedArray(inputList, k):
#     heap = []
#     sortedArr = []
#     for x in inputList:
#         heap.append(x)
#         if len(heap) > k:
#             sortedArr.append(min(heap))
#             heap.remove(min(heap))
#     while len(heap):
#         sortedArr.append(min(heap))
#         heap.remove(min(heap))
#     return sortedArr


# print(nearlySortedArray(input, k))
