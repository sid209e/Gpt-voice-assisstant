# Gpt-voice-assisstant  
This repository contains code for a voice assisstant that answers questions using Amazon Polly, OpenAI, and whisper speech recognition. The code allows the user to change the robot's voice, and it automatically detects the language of the user's question and responds in the appropriate language. The code is licensed under the MIT license.


**GPT Voice Assistant**  
GPT Voice Assistant is a Python program that uses Amazon Polly, Whisper API and OpenAI to create a question-answering humanoid robot that can answer your questions using natural language processing. It uses a microphone to listen to the user's voice, and then uses Amazon Polly to synthesize speech to respond to the user's questions.

**Usage**  
To use the GPT Voice Assistant, simply run the main.py script in your terminal or IDE of choice. Once the script is running, you can use voice commands to interact with the assistant.  

**Prerequisites**  
Before you can use GPT Voice Assisstant, you need to have the following prerequisites installed on your system:  

Python 3.6 or later  
SpeechRecognition library  
PyAudio library  
boto3 library  
pygame library  
OpenAI API key  
Amazon Web Services (AWS) account with access to Amazon Polly  

**Installation**  
1. Clone this repository to your local machine.  
2. Install the required dependencies using ***pip install -r requirements.txt***.  
3. Set up an OpenAI API key and set it as an environment variable named OPENAI_API_KEY.  
4. Run ***main.py*** to start the assistant.  

**Configuration**  
You can configure the following settings in the main.py file:

* ***aws_access_key_id***: Your AWS access key ID  
* ***aws_secret_access_key***: Your AWS secret access key  
* ***region_name***: The AWS region to use  
* ***default_voice***: The default voice to use for Amazon Polly  
* ***openai.api_key***: Your OpenAI API key  
* ***recognizer.energy_threshold***: The minimum energy threshold for the microphone to detect speech  

You can also configure the following settings in the openai.Completion.create() function:  

* ***model***: The OpenAI model to use for natural language processing  
* ***prompt***: The prompt to use for generating the response  
* ***temperature***: The temperature to use for generating the response  
* ***max_tokens***: The maximum number of tokens to generate for the response  
* ***top_p***: The top p value to use for generating the response  
* ***frequency_penalty***: The frequency penalty to use for generating the response  
* ***presence_penalty***: The presence penalty to use for generating the response  

**Future Works**  
1. Implement speech-to-text in multiple languages.

2. Implement text-to-speech in multiple voices.

3. Implement sentiment analysis.

4. Implement chatbot functionality.

5. Implement custom commands.







**Contributions**  
Contributions to this project are welcome. If you find a bug or have a suggestion for a new feature, feel free to create an issue or a pull request.

**License**  
This project is licensed under the MIT License.
