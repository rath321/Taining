# app.py (using Flask)

from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_gpt_response', methods=['POST'])
def get_gpt_response():
    user_input = request.form['user_input']
    response = get_chatgpt_response(user_input)
    return jsonify({'response': response})

def get_chatgpt_response(prompt):
    # Use OpenAI API to get ChatGPT response
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    app.run(debug=True)
