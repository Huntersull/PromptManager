import unittest
from app import FileManager

class TestFileManager(unittest.TestCase):
    
    def setUp(self):
        self.file_manager = FileManager()

    def test_add_prompt(self):
        title = "Test Title"
        text = "Test Text with a {0}[Token]"
        self.file_manager.add_prompt(title, text)

        prompts = self.file_manager.get_prompts()
        self.assertIn((title, text), prompts)

    def test_get_prompt(self):
        title = "Test Title"
        text = "Test Text with a {0}[Token]"
        self.file_manager.add_prompt(title, text)

        prompt_id = len(self.file_manager.get_prompts())
        self.assertEqual(self.file_manager.get_prompt(prompt_id), (title, text))

    def test_fill_prompt(self):
        title = "Test Title"
        text = "Test Text with a {0}[Token]"
        self.file_manager.add_prompt(title, text)

        prompt_id = len(self.file_manager.get_prompts())
        filled_text = self.file_manager.fill_prompt(prompt_id, {"0": "Filled Token"})
        self.assertEqual(filled_text, "Test Text with a Filled Token")

if __name__ == "__main__":
    unittest.main()
