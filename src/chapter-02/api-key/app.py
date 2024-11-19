from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="YOUR ENDPOINT",
    api_key="YOUR KEY"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the largest cities in the world?"},
    ]
)

print(response.choices[0].message.content)