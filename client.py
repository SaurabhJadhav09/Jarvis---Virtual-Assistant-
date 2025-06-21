# 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
from openai import OpenAI

client = OpenAI(
    api_key="#"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa or Google Assistant."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
