class Solution:
    def equalFrequency(self, word: str) -> bool:
        hm = Counter(word)
        fequCount = Counter(hm.values())

        if len(fequCount) == 1:
            if 1 in fequCount:
                return True
            else:
                return False

        elif len(fequCount) == 2:

            minFreq = min(fequCount.keys())
            maxFreq = max(fequCount.keys())

            if minFreq == 1 and fequCount[minFreq] == 1:
                return True
            if maxFreq - minFreq == 1 and fequCount[maxFreq] == 1:
                return True

        return False
