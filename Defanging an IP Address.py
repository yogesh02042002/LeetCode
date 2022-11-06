class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        for i in address:
            x=address.replace(".", "[.]")
        return x
