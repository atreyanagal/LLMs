# AI Chat Bots with Flask and OpenAI

This project implements a simple AI chatbot interface using Flask, HTML, CSS, and OpenAI's GPT-3.5 model through Nvidia's integration API. Users can interact with the chatbot by typing messages into an input field and selecting a model from the provided options. The chatbot will then respond based on the selected model's AI capabilities.

## Features

- **Model Selection**: Choose from a variety of pre-trained AI models to power the chatbot's responses.
- **Real-time Interaction**: Messages are sent to the server and processed by the AI model in real-time, providing instant responses.
- **Customizable Styling**: The interface is styled with CSS, providing a clean and modern look.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Nvidia API key obtained from the Nvidia Developer Portal.
- OpenAI API key obtained from the OpenAI platform.

## Setup

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your_username/ai-chat-bots.git
   ```

2. Navigate to the project directory.

   ```bash
   cd ai-chat-bots
   ```

3. Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

4. Set your Nvidia API key and OpenAI API key as environment variables.

   ```bash
   export NVIDIA_API_KEY='your_nvidia_api_key'
   export OPENAI_API_KEY='your_openai_api_key'
   ```

## Usage

1. Run the Flask application.

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the chatbot interface.

3. Type a message into the input field, select a model from the dropdown list, and click "Send" to interact with the chatbot.

## Customization

You can customize the project in the following ways:

- **Styling**: Modify the CSS in the `index.html` file to change the appearance of the chatbot interface.
- **Model Selection**: Add or remove AI models from the `<select>` element in the HTML file to customize the available options.

## Credits

This project was created by Atrey. It utilizes the following technologies:

- Flask: A lightweight WSGI web application framework in Python.
- OpenAI: A leading artificial intelligence research laboratory.
- Nvidia: A multinational technology company specializing in GPUs and AI.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

