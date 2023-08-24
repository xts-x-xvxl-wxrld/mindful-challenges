import os
import openai

MODEL = "gpt-3.5-turbo"

openai.api_key = os.environ.get('OPENAI_API_KEY')


def generateChallenge():
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {'role': 'system', 'content': 'do not provide bullet points, split answers by paragraphs'
                                          'answer for time duration less than 100 characters,for title under 250 char'},
            {'role': 'user', 'content': 'Write me a meditation challenge that will have a title under 250 char,description'
                                        'under 500 char, brief benefits under 300 char, time duration under 100 char.'}
        ]
    )

    challengeList = response['choices'][0]['message']['content'].split('\n')
    gptAnsCleaned = [item for item in challengeList if item != ""]

    return gptAnsCleaned[0], gptAnsCleaned[1], gptAnsCleaned[2], gptAnsCleaned[3]
