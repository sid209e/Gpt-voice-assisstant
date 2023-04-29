import speech_recognition as sr
import boto3
import os
import pygame
import openai
import langdetect

# fetch audio from microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()
recognizer.energy_threshold = 300

openai.api_key = "your openai_api-key"

# Initialize Amazon Polly client and set default voice
polly_client = boto3.Session(
aws_access_key_id="your_aws_access_key_id",
aws_secret_access_key="your_aws_secret_access_key",
region_name="your_region_name"
).client('polly')

voices = polly_client.describe_voices(LanguageCode='en-US')['Voices']
default_voice = 'Matthew'

# Greet the user when the program starts
response = polly_client.synthesize_speech(VoiceId=default_voice,
                                          Text="Hello! I'm your GPT Voice Assisstant, a humanoid robot that answers your questions.",
                                          OutputFormat='mp3')
with open('hello.mp3', 'wb') as f:
    f.write(response['AudioStream'].read())

# Play the greeting

pygame.init()
pygame.mixer.music.load('hello.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

try:
    # Adjust for background noise
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(recognizer.energy_threshold))
    while True:
        print("Say Something!")
        # Listen to the user's voice
        with microphone as source:
            audio = recognizer.listen(source)
        print("Recognizing...")

        try:
            # speech recognition using whisper api
            OPENAI_API_KEY = "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"
            value = recognizer.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
            print("You said:{}".format(value))
            if "change voice" in value.lower():
                # Change voice based on the command
                for voice in voices:
                    if voice['Name'].lower() in value.lower():
                        default_voice = voice['Id']
                        response = polly_client.synthesize_speech(
                            Text=f"Changed voice to {voice['Name']}",
                            VoiceId=default_voice,
                            OutputFormat='mp3'
                        )
                        audio_file = open('voice_change.mp3', 'wb')
                        audio_file.write(response['AudioStream'].read())
                        audio_file.close()
                        os.system('mpg123 voice_change.mp3')
                        break
            else:
                # Speak the response using Amazon Polly
                response_gpt = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"GPT Voice Assisstant is a humanoid robot that answers to all your questions. It will change its character based on the question. You: {value}\n Your Voice Assistant:",
                    temperature=0.5,
                    max_tokens=100,
                    top_p=0.3,
                    frequency_penalty=0.5,
                    presence_penalty=0.0
                )

                # Determine the language of the response
                response_language = langdetect.detect(response_gpt.choices[0].text)

                # Print the detected language
                print("Detected language: {}".format(response_language))

                # Print OpenAI API response
                print("Response: {}".format(response_gpt.choices[0].text))

                # Set the language code for Amazon Polly
                language_code = None
                if response_language == 'en':
                    language_code = 'en-US'
                    default_voice = 'Matthew'
                elif response_language == 'hi':
                    language_code = 'hi-IN'
                    default_voice = 'Kajal'
                # Add more language codes here as needed

                if language_code:
                    # Speak the response using Amazon Polly
                    response = polly_client.synthesize_speech(
                        Text=response_gpt.choices[0].text,
                        VoiceId=default_voice,
                        Engine="neural",
                        LanguageCode=language_code,
                        OutputFormat='mp3'
                    )
                    print(response_gpt)
                    audio_file = open('response.mp3', 'wb')
                    audio_file.write(response['AudioStream'].read())
                    audio_file.close()
                    os.system('mpg123 response.mp3')
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error: {}".format(e))

except KeyboardInterrupt:
    pass
