import ollama
response = ollama.chat(
     model="llama3.2:3b",
     messages = [
          {
          "role":"user",
          "content":"you are a python programmer."
          }
     ]
)
print(response["message"]["content"])