import re

# Define Node class for AST
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})"


# Convert infix to postfix using the shunting-yard algorithm
def parse_tokens(tokens):
    precedence = {'=': 1, '>': 1, '<': 1, 'AND': 2, 'OR': 2}
    stack = []
    output = []

    for token in tokens:
        if token in ('AND', 'OR'):
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
        else:
            output.append(token)

    while stack:
        output.append(stack.pop())

    return output


def create_ast(parsed_tokens):
    stack = []

    for token in parsed_tokens:
        if token in ('AND', 'OR', '=', '>', '<'):
            if len(stack) >= 2:  # Ensure there are at least two operands
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(type='operator', left=left, right=right, value=token))
            else:
                print(f"Error: Not enough operands for operator '{token}'")
                return None  # Not enough operands, return None
        else:
            # Strip quotes if token is a string
            if token.startswith("'") and token.endswith("'"):
                token = token[1:-1]
            stack.append(Node(type='operand', value=token))

    if len(stack) == 1:
        return stack.pop()
    else:
        print("Error: Stack did not resolve to a single AST node.")
        return None  # Return None if the AST cannot be created


def evaluate_rule(ast, user_data):
    if ast is None:  # If AST is None, return False
        return False

    if ast.type == 'operand':
        return user_data.get(ast.value)
    elif ast.type == 'operator':
        left_value = evaluate_rule(ast.left, user_data)
        right_value = evaluate_rule(ast.right, user_data)

        if ast.value == 'AND':
            return left_value and right_value
        elif ast.value == 'OR':
            return left_value or right_value
        elif ast.value == '=':
            return left_value == right_value
        elif ast.value == '>':
            return left_value > right_value
        elif ast.value == '<':
            return left_value < right_value


# Example tokens
tokens1 = [
    '(', '(', 'age', '>', '30', 'AND', 'department', '=', "'Sales'", ')',
    'OR', '(', 'age', '<', '25', 'AND', 'department', '=', "'Marketing'", ')',
    ')', 'AND', '(', 'salary', '>', '50000', 'OR', 'experience', '>', '5', ')'
]

tokens2 = [
    '(', '(', 'age', '>', '30', 'AND', 'department', '=', "'Marketing'", ')',
    ')', 'AND', '(', 'salary', '>', '20000', 'OR', 'experience', '>', '5', ')'
]

# Parse tokens
parsed_tokens1 = parse_tokens(tokens1)
parsed_tokens2 = parse_tokens(tokens2)

# Output parsed tokens for debugging
print(f"Parsed Tokens for Rule 1: {parsed_tokens1}")
print(f"Parsed Tokens for Rule 2: {parsed_tokens2}")

# Create AST
ast_rule1 = create_ast(parsed_tokens1)
ast_rule2 = create_ast(parsed_tokens2)

# Output AST
print("\nAST for Rule 1:")
print(ast_rule1)
print("\nAST for Rule 2:")
print(ast_rule2)

# Combined AST (Rule 1 AND Rule 2)
combined_ast = Node(type='operator', left=ast_rule1, right=ast_rule2, value='AND') if ast_rule1 and ast_rule2 else None

# Example user data
user_data1 = {'age': 32, 'department': 'Sales', 'salary': 60000, 'experience': 6}
user_data2 = {'age': 28, 'department': 'Marketing', 'salary': 15000, 'experience': 4}

# Evaluate rules for user 1
print("\nEvaluating Rules for User 1:")
result_rule1 = evaluate_rule(ast_rule1, user_data1)
print(f"Evaluation Result of Rule 1 for User 1: {result_rule1}")

result_rule2 = evaluate_rule(ast_rule2, user_data1)
print(f"Evaluation Result of Rule 2 for User 1: {result_rule2}")

combined_result = evaluate_rule(combined_ast, user_data1) if combined_ast else False
print(f"Evaluation Result of Combined Rule for User 1: {combined_result}\n")

# Evaluate rules for user 2
print("Evaluating Rules for User 2:")
result_rule1 = evaluate_rule(ast_rule1, user_data2)
print(f"Evaluation Result of Rule 1 for User 2: {result_rule1}")

result_rule2 = evaluate_rule(ast_rule2, user_data2)
print(f"Evaluation Result of Rule 2 for User 2: {result_rule2}")

combined_result = evaluate_rule(combined_ast, user_data2) if combined_ast else False
print(f"Evaluation Result of Combined Rule for User 2: {combined_result}")
