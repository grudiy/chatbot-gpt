# Working on gpt-3.5-turbo

import openai
from openai import OpenAI
import os


class Chatbot():
    def __init__(self):
        openai.api_key = os.environ["OPENAI_API_KEY"]

    def get_response(self, user_input):
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )
        result = completion.choices[0].message.content
        return result


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write joke about whiskey")
    print(response)
