class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        fmc = float('+inf')
        smc = float('+inf')
        for i in prices:
            if i < fmc:
                smc=fmc
                fmc = i

                continue
            if i < smc:
                smc = i
            
        if fmc+smc <= money:
            return money -(fmc+smc)
        return money