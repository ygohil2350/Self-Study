# input = "aabbcdeee"
# output = "2a2b1c1d3e"


# def stringChecker(initialStr: str) -> str:
#     currentWord = ""
#     currentCount = 0
#     outputStr = ""
#     for x in initialStr:
#         if currentWord != x:
#             if currentCount > 0:
#                 outputStr += str(currentCount) + currentWord
#             currentWord = x
#             currentCount = 1
#         elif currentWord == x:
#             currentCount += 1
#     outputStr += str(currentCount) + currentWord
#     return outputStr


# print(stringChecker("aabbcdeee"))


# Coin Change (Minimum Coins)

# Input: coins[] = [25, 10, 5], sum = 30
# Output: 2
# Explanation: Minimum 2 coins needed, 25 and 5

# Input: coins[] = [9, 6, 5, 1], sum = 19
# Output: 3
# Explanation: 19 = 9 + 9 + 1

# Input: coins[] = [5, 1], sum = 0
# Output: 0
# Explanation: For 0 sum, we do not need a coin

# Input: coins[] = [4, 6, 2], sum = 5
# Output: -1
# Explanation: Not possible to make the given sum.


# def minCoins(coins, sum):
#     def f(ind, target):
#         if target == 0:
#             return 0
#         if ind >= n:
#             return float("inf")
#         if dp[ind][target] != -1:
#             return dp[ind][target]
#         p1 = float("inf")
#         if target >= coins[ind]:
#             p1 = 1 + f(ind, target - coins[ind])
#         p2 = f(ind + 1, target)
#         dp[ind][target] = min(p1, p2)
#         return min(p1, p2)

#     n = len(coins)
#     coins.sort()
#     dp = [[-1] * (sum + 1) for _ in range(n)]
#     return f(0, sum) if f(0, sum) != float("inf") else -1


# print(minCoins([3, 6, 8], 9))


# Minimum Jumps
# Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3
# Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last.
# Input: arr = [1, 4, 3, 2, 6, 7]
# Output: 2
# Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
# Input: arr = [0, 10, 20]
# Output: -1
# Explanation: We cannot go anywhere from the 1st element.


def minJumps(arr: list[int]) -> int:
    currantStep = 0
    jump = 0
    while currantStep < len(arr):
        if arr[currantStep] == 0:
            return -1
        else:
            maxJump = 0
            index = 0
            for x in range(currantStep + 1, arr[currantStep] + 1):
                print(currantStep + 1, arr[currantStep] + 1)
                if arr[x] > maxJump:
                    maxJump = arr[x]
                    index = x
            jump += 1
            currantStep = index
            print(maxJump)
    print(jump)


minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])
