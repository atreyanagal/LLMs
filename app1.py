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
    temperature = float(request.form['temperature'])
    top_p = float(request.form['top_p'])
    max_tokens = int(request.form['max_tokens'])
    stream = request.form.get('stream', type=bool)

    completion = client.chat.completions.create(
        model=selected_model,  # Use selected model
        messages=[{"role": "user", "content": message}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        stream=stream
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response

if __name__ == '__main__':
    app.run(debug=True)
