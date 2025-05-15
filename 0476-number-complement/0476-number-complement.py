class Solution:
    def findComplement(self, num: int) -> int:
        bitlen=num.bit_length()
        val=(2**bitlen)-1
        return ((num^val))