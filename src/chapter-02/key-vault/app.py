from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI

credential = DefaultAzureCredential()
client = SecretClient(vault_url="YOUR KV ENDPOINT",
credential=credential)

api_key=client.get_secret("apikey").value

client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="YOUR ENDPOINT",
    api_key=api_key
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the largest cities in the world?"},
    ]
)

print(response.choices[0].message.content)
