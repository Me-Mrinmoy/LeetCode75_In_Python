# Question--
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 
Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

# Answer--
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1, str2):
        # If str1 + str2 is not equal to str2 + str1, then no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor (GCD) of the lengths of str1 and str2
        gcd_length = self.gcd(len(str1), len(str2))
        
        # The string that divides both str1 and str2 is the substring of str1 of length gcd_length
        return str1[:gcd_length]

# Example usage
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""
