import anthropic

client = anthropic.Anthropic()

user_question = input("What would you like to ask? ")

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": user_question}]
)

print(message.content[0].text)
