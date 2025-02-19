class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs.values(): # si char se encuentra es un valor de apertura
                stack.append(char)
            elif char in pairs:# si char no es un valor de apertura, se revisa que char sea un valor de cierre
                if not stack or stack.pop() != pairs[char]: # (si el stack está vacío return false) o (si el último char es distinto al valor de apertura de char return false)
                    return False

        return not stack # si el stack está vacío return true

sol = Solution()

s = '(()[]{)'
result = sol.isValid(s)
print(result)
