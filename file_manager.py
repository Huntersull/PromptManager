import os
import re
from bs4 import BeautifulSoup

class FileManager:
    def __init__(self, file_path='data/prompts.html'):
        self.file_path = file_path

    def add_prompt(self, title, text):
        soup = self._get_soup()

        # Create a new prompt div
        new_prompt = soup.new_tag('div')
        new_prompt['id'] = f"prompt-{len(soup.find_all('div')) + 1}"
        new_prompt['data-title'] = title
        new_prompt['data-text'] = text

        # Add the new prompt to the soup
        soup.append(new_prompt)

        # Write the soup back to the file
        self._write_soup(soup)

    def get_prompts(self):
        soup = self._get_soup()
        prompts = []
        for div in soup.find_all('div'):
            prompts.append((div['data-title'], div['data-text']))
        return prompts

    def get_prompt(self, prompt_id):
        soup = self._get_soup()
        div = soup.find(id=f"prompt-{prompt_id}")
        return (div['data-title'], div['data-text']) if div else None

    def fill_prompt(self, prompt_id, tokens):
        title, text = self.get_prompt(prompt_id)
        for token_id, value in tokens.items():
            text = text.replace(f"{{{token_id}}}", value)
        return text

    def _get_soup(self):
        if not os.path.exists(self.file_path):
            open(self.file_path, 'w').close()
        with open(self.file_path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
        return soup

    def _write_soup(self, soup):
        with open(self.file_path, 'w') as f:
            f.write(str(soup))
