from flask import Flask, render_template, request, redirect, url_for
from prompt_manager import PromptManager

app = Flask(__name__)
prompt_manager = PromptManager()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        prompt_manager.add_prompt(title, text)
        return redirect(url_for('index'))
    else:
        prompts = prompt_manager.get_prompts()
        return render_template('index.html', prompts=prompts)

@app.route('/use_prompt/<int:prompt_id>', methods=['GET', 'POST'])
def use_prompt(prompt_id):
    if request.method == 'POST':
        filled_text = prompt_manager.fill_prompt(prompt_id, request.form)
        # Copy filled_text to clipboard (to be implemented)
        return redirect(url_for('index'))
    else:
        prompt = prompt_manager.get_prompt(prompt_id)
        tokens = prompt_manager.parse_tokens(prompt[1])
        return render_template('use_prompt.html', prompt=prompt, tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)
