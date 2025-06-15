345. Reverse Vowels String
#Question--

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

#Answer--
class Solution:
    def reverseVowels(self, s):
        # Define the set of vowels (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")
        # Convert the string into a list for mutability
        s_list = list(s)
        # Initialize two pointers
        left, right = 0, len(s_list) - 1

        while left < right:
            # Move the left pointer to the next vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move the right pointer to the previous vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            # Move both pointers inward
            left += 1
            right -= 1

        # Convert the list back to a string
        return ''.join(s_list)

# Example usage
solution = Solution()
s1 = "IceCreAm"
s2 = "leetcode"

print(solution.reverseVowels(s1))  # Output: "AceCreIm"
print(solution.reverseVowels(s2))  # Output: "leotcede"
