from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI


token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)


client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="YOUR ENDPOINT",
    azure_ad_token_provider=token_provider
)


response = client.chat.completions.create(
    model="gpt-4o", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the largest cities in the world?"},
    ]
)

print(response.choices[0].message.content)
