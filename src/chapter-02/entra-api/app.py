from flask import Flask, request, jsonify
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

app = Flask(__name__)

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="YOUR ENDPOINT",
    azure_ad_token_provider=token_provider
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_content = data.get('content')

    if user_content:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_content},
            ]
        )
        return jsonify({"response": response.choices[0].message.content}), 200
    else:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello, World!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
