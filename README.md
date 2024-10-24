# Rule Engine for Dynamic Evaluation

## Description

This project implements a rule engine that dynamically creates, combines, and evaluates rules using an Abstract Syntax Tree (AST). The rule engine supports logical operators (`AND`, `OR`) and can evaluate user data against these rules.

## Setup

1. Clone the repository:
   
    git clone https://github.com/Harisudhan23/Rule-engine.git
    ```bash
    cd Rule-engine
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate      
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python Rule_engine.py
    ```

## Usage

1. To run the rule engine, make sure you have Python installed (version 3.7+ recommended).
2. Follow the setup steps above to install the required packages.
3. Modify the `Rule_engine.py` file to define the rules and input data.
4. Run the program:
    ```bash
    python Rule_engine.py
    ```

## Examples

### Defining and Evaluating Rules

Here’s an example of how to define rules and evaluate them with the rule engine:

```python
# Import necessary functions
from rule_engine import create_rule, evaluate_rule

# Define rules
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

# Parse rules into ASTs
ast_rule1 = create_rule(rule1)
ast_rule2 = create_rule(rule2)

# Evaluate rule for a sample user
user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result_rule1 = evaluate_rule(ast_rule1, user_data)
print(f"Evaluation result for rule1: {result_rule1}")

# Combine rules and evaluate them together
from rule_engine import combine_rules

combined_ast = combine_rules(ast_rule1, ast_rule2, "AND")

# Evaluate the combined rule with another user
user_data2 = {"age": 28, "department": "Marketing", "salary": 45000, "experience": 6}
result_combined = evaluate_rule(combined_ast, user_data2)
print(f"Evaluation result for combined rule: {result_combined}")
```
## License
   This project is licensed under the MIT License. See the LICENSE file for more details.
