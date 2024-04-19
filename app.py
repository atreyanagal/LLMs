from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="your_api_key"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    selected_model = request.form['model']  # Get selected model from form

    completion = client.chat.completions.create(
        model=selected_model,  # Use selected model
        messages=[{"role": "user", "content": message}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response

if __name__ == '__main__':
    app.run(debug=True)
