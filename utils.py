from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  

client = OpenAI()

def generate_description(input):
    messages = [
        {
            "role": "system",
            "content": """As A product description generator, generate multi paragraph text produc description."""
        },
        {
            "role": "user",
            "content": f"{input}"
        }
    ]

    chat = client.chat.completions.create( # type: ignore
        model="gpt-3.5-turbo-0125",
        messages=messages, # type: ignore
        stream=True
    )

    reply = chat.choices[0].message.content 

    return reply

    