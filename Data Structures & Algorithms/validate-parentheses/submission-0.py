class Solution:
    def isValid(self, s: str) -> bool:
        
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        the_list = []
        for c in s:
            
            if c in matching.values():
                the_list.append(c)
            elif c in matching.keys():
                if not the_list:
                    return False
                x = the_list.pop()
                if matching[c] != x:
                    return False
        return not the_list 
                    
                    



