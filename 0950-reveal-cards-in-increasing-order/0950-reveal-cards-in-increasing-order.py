class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque()
        for card in reversed(deck):
            if dq:
                dq.appendleft(dq.pop())  
            dq.appendleft(card)
        
        return list(dq)
