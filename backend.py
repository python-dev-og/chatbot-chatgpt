import openai
import os
from dotenv import load_dotenv

load_dotenv()


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, user_query):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'user', 'content': user_query}
                # {'role': 'system', 'content': persona}
            ],
            max_tokens=2000,
            temperature=0.4,
            user=os.getenv('USER')
        )
        return response.choices[0].message.content


sample_query_resume = "Can you write a job task for a python developer"

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response(sample_query_resume)
    print(response)
