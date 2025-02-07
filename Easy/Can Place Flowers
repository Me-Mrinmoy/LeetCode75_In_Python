605. Can Place Flowers
# Question--
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

# Answer--
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0  # Count of flowers we can plant
        length = len(flowerbed)
        
        for i in range(length):
            # Check if the current spot is empty and both adjacent spots are empty or out of bounds
            if flowerbed[i] == 0:
                # Check previous and next plots
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # Plant a flower here
                    count += 1
                    if count >= n:  # If we've planted enough flowers, return True
                        return True
        
        return count >= n  # Return True if we can plant enough flowers

# Example usage
solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
