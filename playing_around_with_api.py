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
prompt = 'Give me 5 detailed ideas for TikTok videos that captialize on the trend: Lionel Messi accepts offer from Saudi Arabian club'

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
