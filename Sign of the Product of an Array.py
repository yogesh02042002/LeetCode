class Solution:
    def arraySign(self, nums: List[int]) -> int:
        import numpy as np
        product=1
        for i in nums:
            product=mul(i,product)
        return np.sign(product)
