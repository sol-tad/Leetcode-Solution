class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hmw2 = Counter()
        for word in words2:
            wordCount = Counter(word)
            for char in wordCount:
                hmw2[char] = max(hmw2[char], wordCount[char])
        
        print(hmw2)
        res = []

        for w in words1:
            currhm=Counter(w)
            flag=True

            for k in hmw2:
                if hmw2[k]>currhm[k]:
                    flag=False
                    break
            if flag: res.append(w)
        return res
