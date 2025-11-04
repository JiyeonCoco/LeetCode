class Solution:
    def reverseWords(self, s: str) -> str:

        # return ' '.join(s.split()[::-1])

        words = []
        word = ''

        for c in s:
            if c != ' ':
                word += c
            elif word:
                words.append(word)
                word = ''
        if word:
            words.append(word)

        return ' '.join(words[::-1])
