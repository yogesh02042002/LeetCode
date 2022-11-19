class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k=(1.80*celsius)+32
        f=celsius+273.15
        return f,k
