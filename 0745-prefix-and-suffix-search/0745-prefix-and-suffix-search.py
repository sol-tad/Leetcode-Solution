class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = defaultdict(set)
        self.suffix = defaultdict(set)
        self.weight = {}

        for idx, val in enumerate(words):
            pre = ''
            suf = ''
            for char in [''] + list(val):
                pre += char
                self.prefix[pre].add(val)
            
            for char in [''] + list(val[::-1]):
                suf += char
                self.suffix[suf[::-1]].add(val)

            self.weight[val] = idx
        

    def f(self, pref: str, suff: str) -> int:
        w = -1
        for word in self.suffix[suff] & self.prefix[pref]:
            if self.weight[word] > w:
                w = self.weight[word]
        return w
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)