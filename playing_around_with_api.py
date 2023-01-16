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
    temperature=0.7
)

# Print the result
print(response["choices"][0]["text"])
