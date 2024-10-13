class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in range(len(sentences)):
            words=len(sentences[i].split())
            count=max(count,words)
        return count
