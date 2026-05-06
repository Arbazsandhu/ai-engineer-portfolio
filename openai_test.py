from openai import OpenAI
from dotenv import load_dotenv
import os
#Load environment variables
load_dotenv()

#Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

#Create OpenAI client
client = OpenAI(
    api_key=api_key
)

#Send request to OpenAI API

print("AI Engineer Bot - type 'quit' to exit\n ")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", "content": "You are a helpful assistant who explains AI engineering concepts clearly and concisely."
            },
            {
                "role": "user", "content": user_input
            }
        ]
    )

    #Print response
    print(f"Bot: {response.choices[0].message.content}\n")