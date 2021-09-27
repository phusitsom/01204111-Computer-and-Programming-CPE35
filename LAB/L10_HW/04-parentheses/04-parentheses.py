class py_solution(object):
    
    def __init__(self, text) -> None:
        self.text = text
    
    def is_valid_parentheses(self) -> bool:
        
        out_dict = { '(':')', '[':']', '{':'}' }
        stack = []
        
        for char in self.text:
            if char in out_dict:
                stack.append(char)
            elif (not stack) or (char != out_dict[stack.pop()]):
                return False
            
        return stack == []
        
py_sol = py_solution(input('input: '))

print('valid parentheses' if py_sol.is_valid_parentheses() else 'invalid parentheses')