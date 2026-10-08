class Solution:
    def isPalindrome(self, s: str) -> bool:
        last = len(s)-1
        first = 0
        while first < last:
            
            if not s[last].isalnum() and not s[first].isalnum():
                last-=1
                first+=1
            elif not s[last].isalnum():
                last-=1
            elif not s[first].isalnum():
                first+=1
            else:
                if s[last].lower() != s[first].lower():
                    return False
                last-=1
                first+=1

        return True
        
        