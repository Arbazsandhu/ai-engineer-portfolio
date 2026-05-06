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
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user",
         "content": "Explain what an AI Engineer does in 2 sentences."}
    ]
)

#Print response
print(response.choices[0].message.content)