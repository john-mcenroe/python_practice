import os

# Set the API key as an environment variable
os.environ["API_KEY"] = "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"

# Import the OpenAI API client
import openai

# Get the API key
api_key = os.environ.get("API_KEY")

# Set the API key
openai.api_key = api_key

# Define the prompt
prompt = 'Give me a tiktok video for the trend about Kendall Jenner taking into account Devin Booker and Khloe Kardashian'

# Run the GPT-3 query
response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    max_tokens=150,
    temperature=0.5,
    n = 5
)

# Print the result
for i, choice in enumerate(response["choices"]):
    print(f'{i+1}. {choice["text"]}')
