import unittest
from flask import url_for
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_prompt(self):
        response = self.client.post(url_for('index'), data={"title": "Test Title", "text": "Test Text with a {0}[Token]"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Title", response.data)

    def test_use_prompt(self):
        # Add a prompt
        self.client.post(url_for('index'), data={"title": "Test Title", "text": "Test Text with a {0}[Token]"}, follow_redirects=True)
        
        # Use the prompt
        response = self.client.get(url_for('use_prompt', prompt_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Title", response.data)

if __name__ == "__main__":
    unittest.main()
