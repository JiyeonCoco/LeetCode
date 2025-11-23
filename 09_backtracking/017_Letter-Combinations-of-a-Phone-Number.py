class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                 "7": "pqrs", "8": "tuv", "9": "wxyz"}

        outputs = []

        def dfs(letter, idx):

            if idx == len(digits):
                outputs.append(letter)
                return

            for c in phone[digits[idx]]:
                dfs(letter+c, idx+1)

        dfs("", 0)

        return outputs
