def isValid( s: str) -> bool:
    stack = []
    # Map closing parenthesis to closing ones
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        # if current char is an opening parenthesis, put it on the stack
        if char in mapping.values():
            x = char
            stack.append(char)
        # if current char is a closing parenthesis, check if
        # stack is not empty or
        elif char in mapping.keys():
            x = char
            #if len(stack) == 0 or stack.pop() != mapping[char]:
                #return False
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0


isValid("()()()[[]]")

