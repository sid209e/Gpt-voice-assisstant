# GPT Voice Assistant

GPT Voice Assistant is a Python program that utilizes Amazon Polly, Whisper API, and OpenAI to create a question-answering humanoid robot capable of answering questions using natural language processing. The assistant listens to user voice commands, processes them, and responds using speech synthesis.

## Usage

To use the GPT Voice Assistant, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/sid209e/gpt-polly-voice-assistant.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```


3. Set up an OpenAI API key and add it as an environment variable named `OPENAI_API_KEY`.

4. Ensure you have an Amazon Web Services (AWS) account with access to Amazon Polly. Set up your AWS credentials, including the `aws_access_key_id`, `aws_secret_access_key`, and `region_name`.

5. Run the `main.py` script to start the GPT Voice Assistant:

```bash
python main.py
```


6. Once the script is running, you can interact with the voice assistant using voice commands.

## Configuration

You can configure the following settings in the `main.py` file:

- `aws_access_key_id`: Your AWS access key ID.
- `aws_secret_access_key`: Your AWS secret access key.
- `region_name`: The AWS region to use.
- `default_voice`: The default voice to use for Amazon Polly.
- `openai.api_key`: Your OpenAI API key.
- `recognizer.energy_threshold`: The minimum energy threshold for the microphone to detect speech.

Additionally, you can configure settings in the `openai.Completion.create()` function to fine-tune the behavior of the natural language processing:

- `model`: The OpenAI model to use for language processing.
- `prompt`: The prompt to use for generating responses.
- `temperature`: The temperature to control the randomness of the generated responses.
- `max_tokens`: The maximum number of tokens to generate for each response.
- `top_p`: The top-p value to use for generating responses.
- `frequency_penalty`: The frequency penalty to use for generating responses.
- `presence_penalty`: The presence penalty to use for generating responses.

## Future Works

There are several planned improvements and features for the GPT Voice Assistant, including:

- Implementing speech-to-text in multiple languages.
- Adding support for text-to-speech in multiple voices.
- Incorporating sentiment analysis capabilities.
- Enhancing the assistant with chatbot functionality.
- Implementing custom commands and user-specific interactions.

## Contributions

Contributions to this project are welcome! If you find a bug or have a suggestion for a new feature, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

