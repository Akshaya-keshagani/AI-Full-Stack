import ollama

response = ollama.chat(model='llama3.2:3b', messages=[
    {
        'role': 'user',
        'content': 'explain ai in 3 lines and explain about three main types of ai in bullet points'
    }
]
)
print(response['message']['content'])