from ollama import chat, ChatResponse

response: ChatResponse = chat(model="gemma3:4b", messages=[
    {
        "role": "user",
        "content": "urgay",
    },
])
print(response['message']['content'])
print(response.message.content)