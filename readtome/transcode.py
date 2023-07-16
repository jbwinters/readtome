'''
read.py

Reads a local file into a text buffer, then sends it to GPT-4 for translation into an English string that is easily understood by humans.
The string is sent to Eleven Labs for trancoding into audio, which is then played back to the user.
'''

import openai
import elevenlabs
import json
import os
import sys
import time
import datetime

# OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Eleven Labs API key
elevenlabs.api_key = os.environ['ELEVENLABS_API_KEY']

elevenlabs.set_api_key(elevenlabs.api_key)


# OpenAI engine ID
engine = 'gpt-4-0613'


def read_file(file):
    with open(file, 'r') as f:
        text = f.read()
    return text


def summarize_with_llm(filename, text, **kwargs):
    # Summarize text with OpenAI GPT-4
    prompt = '''
    You are part of a team that translates written code into easily understandable audio transcriptions. You are to take the prompt given as input, which may include code or technical formulas, and write a translation that is understandable when read aloud in English, providing useful context where possible along the way. The goal is to provide an audible method for reading and comprehending code, so detail is important.

    File: {filename}

    Input: 
    {text}
    '''

    prompt = prompt.format(text=text, filename=filename)

    if 'model' not in kwargs:
        kwargs['model'] = engine

    response = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": prompt}],
        **kwargs
    )

    message = response["choices"][0]["message"]['content']

    print(message)

    return message


def convert_to_audio(text, voice='Adam', model='eleven_monolingual_v1', stream=False):
    # Convert text to audio with Eleven Labs
    audio = elevenlabs.generate(
      text=text,
      voice=voice,
      model=model,
      stream=stream
    )

    return audio

def play_audio(audio):
    elevenlabs.play(audio)

def read_aloud(file):
    # Read file
    text = read_file(file)

    # Summarize text
    summary = summarize_with_llm(text, file, temperature=0.9, max_tokens=2000)

    # Convert text to audio
    stream = convert_to_audio(summary, stream=True)

    # Play audio
    elevenlabs.stream(stream)

if __name__ == '__main__':
    main()
