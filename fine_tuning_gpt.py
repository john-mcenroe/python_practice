import openai

# Set the API key
openai.api_key = "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"

# Define the dataset and the prompt
data = "Trend1: Generate ideas for cat videos"
prompt = 'Generate a text for trend1'

# Create the fine-tuning request
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    data=data
)

# Print the response
print(response)
