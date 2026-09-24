import ollama
msgs = [
    {
        "role": "system",
        "content": "act like a friendly, funny chatbot and give answers in two lines only"
    }
]
while True:
    question = input("you: ")
    if question.lower() == "exit":
        break
    msgs.append(
        {"role": "user",
         "content": question}
    )

    response = ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append(
        {"role": "assistant",
        "content": response["message"]["content"]}
    )
print("\n chat history:")
for msg in msgs:
    print(f"{msg["role"]}:{msg["content"]}")

print("AI:", response["message"]["content"])

    