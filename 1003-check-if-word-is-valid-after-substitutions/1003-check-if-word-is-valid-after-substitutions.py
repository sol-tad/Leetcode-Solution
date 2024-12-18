class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for c in s:
            st.append(c)
            if st and st[-3:]== ['a', 'b', 'c']:
                for _ in range(3):
                    st.pop()
            
        if st==[]:return True
        else: return False


        