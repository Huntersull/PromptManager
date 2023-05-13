import re
from file_manager import FileManager

class PromptManager:
    def __init__(self):
        self.file_manager = FileManager()

    def add_prompt(self, title, text):
        self.file_manager.add_prompt(title, text)
        self.sync_with_github()

    def get_prompts(self):
        return self.file_manager.get_prompts()

    def get_prompt(self, prompt_id):
        return self.file_manager.get_prompt(prompt_id)

    def fill_prompt(self, prompt_id, tokens):
        return self.file_manager.fill_prompt(prompt_id, tokens)

    def parse_tokens(self, text):
        # Matches {#}[Token Label]
        matches = re.findall(r"\{(\d+)\}\[(.*?)\]", text)
        return matches

    def sync_with_github(self):
        g = Github("<personal access token>")
        repo = g.get_user().get_repo("<repo name>")

        with open('data/prompts.html', 'r') as file:
            content = file.read()

        contents = repo.get_contents("data/prompts.html")
        repo.update_file(contents.path, "update prompts.html", content, contents.sha)