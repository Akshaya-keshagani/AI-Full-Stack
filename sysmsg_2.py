import ollama

response = ollama.chat(model='llama3.2:3b', messages=[
    {
        "role": "system",
        "content":"give the answer like you explaining to 5 years old kid give ans in 2-3 lines."
    },
    {
        'role': 'user',
        'content': 'explain ml'
    }
]
)
print(response['message']['content'])