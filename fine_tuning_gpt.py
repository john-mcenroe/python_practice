import openai

# Set the API key
openai.api_key = "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"

# Define the dataset and the prompt
data = "Trend1: This is an example of a trend that you want the model to learn"
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
