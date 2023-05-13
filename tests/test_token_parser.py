import unittest
from app import parse_tokens

class TestTokenParser(unittest.TestCase):
    
    def test_parse_tokens(self):
        prompt_text = "You are a master {0}[Specialty], and I need you to create {1}[Project Description]"
        expected_output = [("0", "Specialty"), ("1", "Project Description")]

        self.assertEqual(parse_tokens(prompt_text), expected_output)

if __name__ == "__main__":
    unittest.main()
