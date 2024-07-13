import time
from openai import OpenAI

client = OpenAI()

# create the assistant
assistant = client.beta.assistants.create(
    name = "Study Buddy",
    model = "gpt-3.5-turbo",
    instructions = "You are a studdy partner for students who are new to technology. When you answer prompts use simple language that will help someone new to web development learn",
    tools=[]
)
thread = client.beta.threads.create()

user_input = input("You: ")

message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    content = user_input
)

run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
)

while True:
    time.sleep(2)
    run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id
    )
    if run.status == "completed":
        break

thread_messages = client.beta.threads.messages.list(
    thread_id = thread.id
)

message_for_user = thread_messages.data[0].content[0].text.value

print("\nAssistant: " + message_for_user + "\n")