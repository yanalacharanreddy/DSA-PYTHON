def isBalanced(s):
    stk = []
    pairs = {'}': '{', ']': '[', ')': '('}  # Corrected the pairs dictionary
    
    for val in s:
        if val in '{[(':
            stk.append(val)
        elif val in ']})':
            if not stk or stk[-1] != pairs[val]:  # Check the last item in the stack
                return 'Not Balanced'
            else:
                stk.pop()
    
    return 'Balanced' if len(stk) == 0 else 'Not Balanced'

if __name__ == "__main__":
    s = input()  # Take input from the user
    print(isBalanced(s))
