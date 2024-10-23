import unittest
from Rule_engine import create_ast, evaluate_rule, combine_rule

class TestRuleEngine(unittest.TestCase):

    def setUp(self):
        # This will run before each test
        self.rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        self.rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        self.user_data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        self.user_data2 = {"age": 28, "department": "Marketing", "salary": 45000, "experience": 6}

    def test_create_rule(self):
        # Test if rules are properly created into ASTs
        ast_rule1 = create_ast(self.rule1)
        ast_rule2 = create_ast(self.rule2)
        self.assertIsNotNone(ast_rule1)
        self.assertIsNotNone(ast_rule2)

    def test_evaluate_rule(self):
        # Test evaluation of rule1
        ast_rule1 = create_ast(self.rule1)
        result_rule1 = evaluate_rule(ast_rule1, self.user_data1)
        self.assertTrue(result_rule1)

        # Test evaluation of combined rules
        ast_rule2 = create_ast(self.rule2)
        combined_ast = combine_rule(ast_rule1, ast_rule2, "AND")
        result_combined = evaluate_rule(combined_ast, self.user_data1)
        self.assertFalse(result_combined)

    def test_rule_fails(self):
        # Test with failing conditions
        ast_rule1 = create_ast(self.rule1)
        result_rule1 = evaluate_rule(ast_rule1, {"age": 20, "department": "Marketing", "salary": 40000, "experience": 1})
        self.assertFalse(result_rule1)

if __name__ == "__main__":
    unittest.main()
