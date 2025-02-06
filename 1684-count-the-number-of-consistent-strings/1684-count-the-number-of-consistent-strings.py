class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alwset=set(allowed)
        count=0
        for i in range(len(words)):
            currset=set(words[i])
            if currset<=alwset:
                count+=1
        return count