from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hm=dict(Counter(chars))
        count=0
        for i in range(len(words)):
            currhm=dict(Counter(words[i]))
            flag=1
            for key in currhm:
                if key not in hm or currhm[key] >hm[key]:
                    flag=0
            if flag:
                count+=len(words[i])
        return count




        