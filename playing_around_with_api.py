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
prompt = 'Give me a video script and details of the visual look and feel for a tiktok video of the current trending topic about the company Stripe taking back retirement contributions after laying off 15% of their staff ealier this year'

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
