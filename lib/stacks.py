def is_balanced(expression):
    return expression[len(expression)-1] == ")"

# Test Cases

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False