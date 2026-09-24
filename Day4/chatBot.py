import ollama
msgs=[{
    "role": "system", 
     "content": "Act as proffesor and give me ans in 2 lines "

}]
while True:
    question = input("Ask you question: ")
    if question.lower() == "exit":
        break
    msgs.append(
        {"role": "user", 
         "content": question}
         )
    response = ollama.chat(
        model='llama3.2:3b', 
        messages=msgs   
    )
    msgs.append({"role": "assistant",
                  "content": response['message']['content']})
    print("AI:",response['message']['content'])
print("---chat History---\n")
for msg in msgs:
    if msg["role"] == "system":
        break   
    print(msg['role'],":",msg['content'])
